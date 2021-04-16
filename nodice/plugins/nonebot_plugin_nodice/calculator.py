import random
import re
from typing import Optional

from .exception import DiceException

# 基础 Calculator 类
class Calculator:
    type = "base"

    def __init__(self, expression: str = "", default_dice: int = 100):
        if expression == "":
            expression = f"1D{default_dice}"
        self.expression = expression
        self.source = expression
        self.detail = expression
        self.default_dice = default_dice

    def __add__(self, other):
        result = self.new(expression=self.expression + "+" + other.expression)
        result.detail = self.detail + "+" + other.detail
        result.result = self.result + other.result
        return result

    def __sub__(self, other):
        result = self.new(expression=self.expression + "-" + other.expression)
        result.detail = self.detail + "-" + other.detail
        result.result = self.result - other.result
        return result

    def __mul__(self, other):
        result = self.new(expression=self.expression + "*" + other.expression)
        result.detail = self.detail + "*" + other.detail
        result.result = self.result * other.result
        return result

    def __truediv__(self, other):
        result = self.new(expression=self.expression + "/" + other.expression)
        result.detail = self.detail + "/" + other.detail
        result.result = self.result / other.result
        return result

    def __pow__(self, other):
        result = self.new(expression=self.expression + "^" + other.expression)
        result.detail = self.detail + "^" + other.detail
        result.result = self.result ** other.result
        return result

    def __str__(self):
        return f"{self.source}{' = ' + self.detail if self.show_detail else ''} = {int(self.result)}"

    def new(
        self,
        type: Optional[str] = None,
        expression: Optional[str] = None,
        default_dice: Optional[int] = None,
    ) -> "Calculator":
        if type is None:
            type = self.type

        if expression is None:
            expression = self.expression

        if default_dice is None:
            default_dice = self.default_dice

        if type == "base":
            calculator = Calculator(expression, default_dice)
        elif type == "coc":
            calculator = CocCalculator(expression, default_dice)
        elif type == "wod":
            calculator = WodCalculator(expression, default_dice)
        elif type == "fate":
            calculator = FateCalculator(expression, default_dice)

        return calculator

    def run(self, show_detail: bool = True) -> str:
        self.show_detail = show_detail
        result = ""
        self.__extract_roundnum_and_reason()
        for i in range(self.round_num):
            self.expression = self.source
            result += "\n" + str(self.__calculate_with_bracket())
        return result

    def calculate(self) -> int:
        self.expression = self.expression.upper()
        return int(self.__calculate_with_bracket().result)

    # 提取轮数和原因
    def __extract_roundnum_and_reason(self) -> "Calculator":

        # 匹配正则
        match_result = re.search(
            r"(([0-9]+)#)?([dDkK0-9\.+\-*/\^\(\)]*)(.*)", self.expression
        )

        # 获取轮数，获取不到默认为1，超过10或等于0报错
        try:
            self.round_num = int(match_result.group(2))
        except:
            self.round_num = 1
        if self.round_num <= 0 or self.round_num > 10:
            raise DiceException("非法轮数")

        # 获取表达式
        self.source = match_result.group(3).strip().upper()

        # 获取掷骰原因，获取不到默认为空
        try:
            self.reason = match_result.group(4).strip()
        except:
            self.reason = None

        return self

    # 计算有括号的表达式
    def __calculate_with_bracket(self) -> "Calculator":
        expression = self.expression
        right_bracket_position = expression.find(")")
        if right_bracket_position >= 0:
            expression_in_left = expression[:right_bracket_position]
            expression_in_right = expression[right_bracket_position + 1 :]
            left_bracket_position = expression_in_left.rfind("(")
            if left_bracket_position >= 0:
                calculator_in_bracket = Calculator().new(
                    expression=expression_in_left[left_bracket_position + 1 :],
                )
                calculator_in_bracket.__calculate_without_bracket()
                expression_in_left = expression_in_left[:left_bracket_position]
                self.expression = (
                    expression_in_left
                    + str(int(calculator_in_bracket.result))
                    + expression_in_right
                )
                self.detail = (
                    expression_in_left
                    + calculator_in_bracket.detail
                    + expression_in_right
                )
                self.__calculate_with_bracket()
            else:
                self.__calculate_without_bracket()
        else:
            self.__calculate_without_bracket()

        return self

    # 计算无括号的表达式
    def __calculate_without_bracket(self) -> "Calculator":

        # 去除无效括号
        expression = self.expression.replace("(", "").replace(")", "")

        if re.search(r"[+\-*/\^]", expression):
            if "+" in expression:
                operator = "+"
                operator_position = expression.find("+")
            elif "-" in expression:
                operator = "-"
                operator_position = expression.find("-")
            elif "*" in expression:
                operator = "*"
                operator_position = expression.find("*")
            elif "/" in expression:
                operator = "/"
                operator_position = expression.find("/")
            elif "^" in expression:
                operator = "^"
                operator_position = expression.find("^")

            calculator_in_left = self.new(expression=expression[:operator_position])
            calculator_in_left.__calculate_without_bracket()
            calculator_in_right = self.new(
                expression=expression[operator_position + 1 :]
            )
            calculator_in_right.__calculate_without_bracket()

            if operator == "+":
                calculator_result = calculator_in_left + calculator_in_right
            elif operator == "-":
                calculator_result = calculator_in_left - calculator_in_right
            elif operator == "*":
                calculator_result = calculator_in_left * calculator_in_right
            elif operator == "/":
                calculator_result = calculator_in_left / calculator_in_right
            elif operator == "^":
                calculator_result = calculator_in_left ** calculator_in_right

            self.expression = calculator_result.expression
            self.detail = calculator_result.detail
            self.result = calculator_result.result
        elif re.search(r"([0-9]*)D([0-9]*)(K([0-9]*))?", expression):
            self.__throw_dice()
        else:
            self.result = float(expression)

        return self

    # 掷骰
    def __throw_dice(self) -> "Calculator":
        expression = self.expression
        default_dice = self.default_dice

        # 匹配正则
        match_result = re.search(r"([0-9]*)D([0-9]*)(K([0-9]*))?(.*)", expression)

        # 获取骰数，获取不到默认为1，超过100或等于0报错
        try:
            dice_num = int(match_result.group(1))
        except:
            dice_num = 1
        if dice_num <= 0 or dice_num > 100:
            raise DiceException("非法骰数")

        # 获取骰面，获取不到默认为100，超过1000或等于0报错
        try:
            dice_face = int(match_result.group(2))
        except:
            dice_face = default_dice
        if dice_face <= 0 or dice_face > 1000:
            raise DiceException("非法骰面")

        # 获取有效骰数，获取不到默认为骰数，超过骰数或等于0报错
        try:
            dice_pick = int(match_result.group(4))
        except:
            dice_pick = dice_num
        if dice_pick <= 0 or dice_pick > dice_num:
            raise DiceException("非法有效骰数")

        try:
            if match_result.group(5) is not None:
                raise DiceException("非法表达式")
        except:
            pass

        # 模拟现实掷骰
        dice_result_list = []
        for i in range(dice_num):
            dice_result = random.randint(1, dice_face)
            dice_result_list.append(dice_result)

        dice_result_list.sort(reverse=True)  # 降序排列，为有效骰作准备

        # 统计骰子以及计算过程
        self.detail = "["
        dice_count = 0.0
        for i in range(dice_num):
            if i:
                self.detail += "+"
            if i < dice_pick:
                self.detail += str(dice_result_list[i])
                dice_count += dice_result_list[i]
            else:
                self.detail += "(" + str(dice_result_list[i]) + ")"
        self.detail += "]"
        self.result = dice_count

        return self


class CocCalculator(Calculator):
    type = "coc"

    def deal_with_result(self, success_rate: int, success_rule: int = 0) -> str:
        if success_rule == 0:
            if self.result == 100:
                result = "{strFumble}"
            elif self.result == 1:
                result = "{strCriticalSuccess}"
            elif self.result <= success_rate / 5:
                result = "{strExtremeSuccess}"
            elif self.result <= success_rate / 2:
                result = "{strHardSuccess}"
            elif self.result <= success_rate:
                result = "{strSuccess}"
            elif self.result < 96 or success_rate >= 50:
                result = "{strFailure}"
            else:
                result = "{strFumble}"
        elif success_rule == 1:
            if self.result == 100:
                result = "{strFumble}"
            elif self.result == 1 or self.result <= 5 and success_rate >= 50:
                result = "{strCriticalSuccess}"
            elif self.result <= success_rate / 5:
                result = "{strExtremeSuccess}"
            elif self.result <= success_rate / 2:
                result = "{strHardSuccess}"
            elif self.result <= success_rate:
                result = "{strSuccess}"
            elif self.result < 96 or success_rate >= 50:
                result = "{strFailure}"
            else:
                result = "{strFumble}"
        elif success_rule == 2:
            if self.result == 100:
                result = "{strFumble}"
            elif self.result <= 5 and self.result <= success_rate:
                result = "{strCriticalSuccess}"
            elif self.result <= success_rate / 5:
                result = "{strExtremeSuccess}"
            elif self.result <= success_rate / 2:
                result = "{strHardSuccess}"
            elif self.result <= success_rate:
                result = "{strSuccess}"
            elif self.result < 96:
                result = "{strFailure}"
            else:
                result = "{strFumble}"
        elif success_rule == 3:
            if self.result >= 96:
                result = "{strFumble}"
            elif self.result <= 5:
                result = "{strCriticalSuccess}"
            elif self.result <= success_rate / 5:
                result = "{strExtremeSuccess}"
            elif self.result <= success_rate / 2:
                result = "{strHardSuccess}"
            elif self.result <= success_rate:
                result = "{strSuccess}"
            else:
                result = "{strFailure}"
        elif success_rule == 4:
            if self.result == 100:
                result = "{strFumble}"
            elif self.result <= 5 and self.result <= success_rate / 10:
                result = "{strCriticalSuccess}"
            elif self.result <= success_rate / 5:
                result = "{strExtremeSuccess}"
            elif self.result <= success_rate / 2:
                result = "{strHardSuccess}"
            elif self.result <= success_rate:
                result = "{strSuccess}"
            elif self.result < 96 + success_rate / 10 or success_rate >= 50:
                result = "{strFailure}"
            else:
                result = "{strFumble}"
        elif success_rule == 5:
            if self.result >= 99:
                result = "{strFumble}"
            elif self.result <= 2 and self.result <= success_rate / 10:
                result = "{strCriticalSuccess}"
            elif self.result <= success_rate / 5:
                result = "{strExtremeSuccess}"
            elif self.result <= success_rate / 2:
                result = "{strHardSuccess}"
            elif self.result <= success_rate:
                result = "{strSuccess}"
            elif self.result < 96 or success_rate >= 50:
                result = "{strFailure}"
            else:
                result = "{strFumble}"
        elif success_rule == 6:
            if self.result > success_rate:
                if self.result == 100 or self.result % 11 == 0:
                    result = "{strFumble}"
                else:
                    result = "{strFailure}"
            else:
                if self.result == 1 or self.result % 11 == 0:
                    result = "{strCriticalSuccess}"
                else:
                    result = "{strSuccess}"
        else:
            return IndexError

        return result

    # 常规检定
    def roll_check(self, attribute: dict, success_rule=0):
        # 匹配正则
        match_result = re.search(
            r"(([0-9]+)#)?([^0-9]*)([0-9]*)(.*)", self.expression
        )

        # 获取轮数，获取不到默认为1，超过10或等于0报错
        try:
            round_num = int(match_result.group(2))
        except:
            round_num = 1
            
        if round_num <= 0 or round_num > 10:
            raise DiceException("非法轮数")

        difficulty = match_result.group(3)
        try:
            self.attribute = match_result.group(4)
        except:
            self.attribute = ""
        try:
            success_rate = int(match_result.group(5))
        except:
            if self.attribute in property.keys():
                success_rate = property[self.attribute]
            else:
                success_rate = 0
        if difficulty == "困难":
            success_rate = int(success_rate / 2)
        elif difficulty == "极难":
            success_rate = int(success_rate / 5)
        else:
            difficulty = ""

        self.attribute = difficulty + self.attribute

        # 返回消息
        message = ""
        for i in range(round_num):
            calculator = self.new("D100", type)
            calculator.__calculate_with_bracket()
            message += "\n" + calculator.source
            message += "=" + str(int(calculator.result))
            message += "/" + str(success_rate)
            message += calculator.deal_with_result(success_rate, success_rule)
        return message

    # 理智检定
    def san_check(self, property: dict, success_rule=0):
        type = self.type

        # 匹配正则
        match_result = re.search(r"([d0-9]*)/([d0-9]*)[\s]*([0-9]*)", self.expression)

        # 成功与失败时的表达式
        calculator_success = CocCalculator(match_result.group(1).strip().lower())
        calculator_fail = CocCalculator(match_result.group(2).strip().lower())

        try:
            success_rate = int(match_result.group(3))
        except:
            if "理智" in property.keys():
                success_rate = property["理智"]
            else:
                success_rate = 0

        # 返回消息
        message = ""
        calculator = self.new("D100", type)
        calculator.__throw_dice()
        message += "\n" + calculator.source
        message += "=" + str(int(calculator.result))
        message += "/" + str(success_rate)
        success_level = calculator.deal_with_result(success_rate, success_rule)
        message += success_level
        if success_level == "{strSuccess}":
            message += calculator_fail.expression[
                calculator_fail.expression.find("d") + 1 :
            ]
        elif success_level == "{strFailure}":
            message += " 失败 理智减少"
            calculator_fail.__throw_dice()
            message += calculator_fail.source
            message += "=" + str(int(calculator_fail.result))
        elif success_level == "{strFumble}":
            message += calculator_fail.expression[
                calculator_fail.expression.find("d") + 1 :
            ]
        return message


class FateCalculator:
    type = "fate"

    # 掷骰
    def __throw_dice(self):
        print("__throw_dice:", self)

        expression = self.expression
        default_dice = self.default_dice

        # 匹配正则
        match_result = re.search(r"([0-9]*)D([0-9]*)(K([0-9]*))?(.*)", expression)

        # 获取骰数，获取不到默认为1，超过100或等于0报错
        try:
            dice_num = int(match_result.group(1))
        except:
            dice_num = 1
        if dice_num <= 0 or dice_num > 100:
            raise DiceException("非法骰数")

        # 获取骰面，获取不到默认为100，超过1000或等于0报错
        try:
            dice_face = int(match_result.group(2))
        except:
            dice_face = default_dice
        if dice_face <= 0 or dice_face > 1000:
            raise DiceException("非法骰面")

        # 获取有效骰数，获取不到默认为骰数，超过骰数或等于0报错
        try:
            dice_pick = int(match_result.group(4))
        except:
            dice_pick = dice_num
        if dice_pick <= 0 or dice_pick > dice_num:
            raise DiceException("非法有效骰数")

        if match_result.group(5) != "":
            raise DiceException("非法表达式")

        # 格式化表达式
        self.source = f"{dice_num}D{dice_face}"
        if dice_pick < dice_num:
            self.source += f"K{dice_pick}"

        # 模拟现实掷骰
        dice_result_list = []
        for i in range(dice_num):
            dice_result = random.randint(1, dice_face)
            dice_result_list.append(dice_result)

        dice_result_list.sort(reverse=True)  # 降序排列，为有效骰作准备

        # 统计骰子以及计算过程
        self.detail = "["
        dice_count = 0
        for i in range(dice_num):
            if i:
                self.detail += "+"
            if i < dice_pick:
                self.detail += str(dice_result_list[i])
                dice_count += dice_result_list[i]
            else:
                self.detail += "(" + str(dice_result_list[i]) + ")"
        self.detail += "]"
        self.result = dice_count


class WodCalculator:
    type = "wod"

    # 掷骰
    def __throw_dice(self):
        print("__throw_dice:", self)

        expression = self.expression
        default_dice = self.default_dice

        # 匹配正则
        match_result = re.search(r"([0-9]*)D([0-9]*)(K([0-9]*))?(.*)", expression)

        # 获取骰数，获取不到默认为1，超过100或等于0报错
        try:
            dice_num = int(match_result.group(1))
        except:
            dice_num = 1
        if dice_num <= 0 or dice_num > 100:
            raise DiceException("非法骰数")

        # 获取骰面，获取不到默认为100，超过1000或等于0报错
        try:
            dice_face = int(match_result.group(2))
        except:
            dice_face = default_dice
        if dice_face <= 0 or dice_face > 1000:
            raise DiceException("非法骰面")

        # 获取有效骰数，获取不到默认为骰数，超过骰数或等于0报错
        try:
            dice_pick = int(match_result.group(4))
        except:
            dice_pick = dice_num
        if dice_pick <= 0 or dice_pick > dice_num:
            raise DiceException("非法有效骰数")

        if match_result.group(5) != "":
            raise DiceException("非法表达式")

        # 格式化表达式
        self.source = f"{dice_num}D{dice_face}"
        if dice_pick < dice_num:
            self.source += f"K{dice_pick}"

        # 模拟现实掷骰
        dice_result_list = []
        for i in range(dice_num):
            dice_result = random.randint(1, dice_face)
            dice_result_list.append(dice_result)

        dice_result_list.sort(reverse=True)  # 降序排列，为有效骰作准备

        # 统计骰子以及计算过程
        self.detail = "["
        dice_count = 0
        for i in range(dice_num):
            if i:
                self.detail += "+"
            if i < dice_pick:
                self.detail += str(dice_result_list[i])
                dice_count += dice_result_list[i]
            else:
                self.detail += "(" + str(dice_result_list[i]) + ")"
        self.detail += "]"
        self.result = dice_count
