# handle.py
# 与 nonebot 完全松耦合的命令实现

from .calculator import Calculator
from .data import *
from .message import getGlobalMsg,format_string
from .help import getHelpDoc

# 函数一律命名为 handle_command

def handle_r(message: str, **kargs) -> str:
    if not "group_id" in kargs.keys():
        cal = Calculator(message)
        data = {
            "pc": get_nickname(kargs["user_id"], kargs["nickname"]),
            "res": cal.run(),
            "reason": cal.reason,
        }
    else:
        cal = Calculator(message, get_defaultdice(kargs["group_id"]))
        data = {
            "pc": get_nickname(kargs["user_id"], kargs["nickname"]),
            "res": cal.run(),
            "reason": cal.reason,
        }

    if cal.reason:
        return format_string(getGlobalMsg("strRollDiceReason"), data)
    else:
        return format_string(getGlobalMsg("strRollDice"), data)


def handle_help(message: str) -> str:
    result = getHelpDoc(message)
    if not result :
        result = getGlobalMsg("strHlpMsg")
    return result


def handle_dismiss() -> str:
    result = getGlobalMsg("strDismiss")
    return result
