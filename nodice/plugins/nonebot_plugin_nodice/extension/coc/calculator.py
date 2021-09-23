import re
import random

from nonebot_plugin_nodice.core import Calculator, DiceException


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
        match_result = re.search(r"(([0-9]+)#)?([^0-9]*)([0-9]*)(.*)", self.expression)

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
