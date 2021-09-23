import re
import random

# from .exception import DiceException


class Calculator:
    def __init__(self, expression: str, default_dice: int = 100):
        if expression == "":
            expression = f"1D{default_dice}"
        self.expression = expression
        self.source = expression
        self.detail = expression
        self.default_dice = default_dice

    def __add__(self, other: "Calculator") -> "Calculator":
        result = self.new(self.expression + "+" + other.expression)
        result.detail = self.detail + "+" + other.detail
        result.result = self.result + other.result
        return result

    def __sub__(self, other: "Calculator") -> "Calculator":
        result = self.new(self.expression + "-" + other.expression)
        result.detail = self.detail + "-" + other.detail
        result.result = self.result - other.result
        return result

    def __mul__(self, other: "Calculator") -> "Calculator":
        result = self.new(self.expression + "*" + other.expression)
        result.detail = self.detail + "*" + other.detail
        result.result = self.result * other.result
        return result

    def __truediv__(self, other: "Calculator") -> "Calculator":
        result = self.new(self.expression + "/" + other.expression)
        result.detail = self.detail + "/" + other.detail
        result.result = self.result / other.result
        return result

    def __pow__(self, other: "Calculator") -> "Calculator":
        result = self.new(self.expression + "^" + other.expression)
        result.detail = self.detail + "^" + other.detail
        result.result = self.result ** other.result
        return result

    def __str__(self):
        return f"{self.source}{' = ' + self.detail if self.show_detail else ''} = {int(self.result)}"

    @classmethod
    def new(cls, expression: str, default_dice: int = 100) -> "Calculator":
        return Calculator(expression, default_dice)

    def run(self, show_detail: bool = True) -> str:
        self.show_detail = show_detail
        result = ""
        self.__extract_roundnum_and_reason()
        for i in range(self.round_num):
            self.expression = self.source
            self.__calculate_with_bracket()
            result += "\n" + str(self)
        return result

    def calculate(self) -> int:
        self.expression = self.expression.upper()
        return int(self.__calculate_with_bracket().result)

    # 提取轮数和原因
    def __extract_roundnum_and_reason(self) -> "Calculator":

        # 匹配正则
        match_result = re.search(r"((\d*)#)?([dDkK\d.+\-*\/^()]*)(.*)", self.expression)

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

    # 计算有括号的表达式
    def __calculate_with_bracket(self):
        expression = self.expression
        right_bracket_position = expression.find(")")
        if right_bracket_position >= 0:
            expression_in_left = expression[:right_bracket_position]
            expression_in_right = expression[right_bracket_position + 1 :]
            left_bracket_position = expression_in_left.rfind("(")
            if left_bracket_position >= 0:
                calculator_in_bracket = self.new(
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

    # 计算无括号的表达式
    def __calculate_without_bracket(self) -> "Calculator":

        # 去除无效括号
        expression = self.expression.replace("(", "").replace(")", "")

        if re.search(r"[+\-*\/^]", expression):
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
        elif re.search(r"(\d*)D(\d*)(K(\d*))?", expression):
            self.__throw_dice()
        else:
            self.result = float(expression)

    # 掷骰
    def __throw_dice(self) -> "Calculator":
        expression = self.expression
        default_dice = self.default_dice

        # 匹配正则
        match_result = re.search(r"(\d*)D(\d*)(K(\d*))?", expression)

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
        dice_result_list = dice_result_list[:dice_pick]

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


if __name__ == "__main__":
    while True:
        print(Calculator(input()).run())
