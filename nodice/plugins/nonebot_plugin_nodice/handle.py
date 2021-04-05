from .calculator import Calculator
from .data import *
from .message import getGlobalMsg, format_string
from .help import getHelpDoc
from .others import get_rules, get_jrrp

# 函数一律命名为 handle_command


def handle_r(**kargs) -> str:
    if not "group_id" in kargs.keys():
        cal = Calculator(kargs["message"])
        data = {
            "pc": get_nickname(kargs["user_id"], kargs["nickname"]),
            "res": cal.run(),
            "reason": cal.reason,
        }
    else:
        cal = Calculator(kargs["message"], get_defaultdice(kargs["group_id"]))
        data = {
            "pc": get_nickname(kargs["user_id"], kargs["nickname"]),
            "res": cal.run(),
            "reason": cal.reason,
        }

    if cal.reason:
        return format_string(getGlobalMsg("strRollDiceReason"), data)
    else:
        return format_string(getGlobalMsg("strRollDice"), data)


def handle_help(**kargs) -> str:
    result = getHelpDoc(kargs["message"])
    if not result:
        result = getGlobalMsg("strHlpMsg")
    return result


def handle_dismiss(**kargs) -> str:
    result = getGlobalMsg("strDismiss")
    return result


def handle_rules(**kargs) -> str:
    result = get_rules(kargs["self_id"], kargs["message"])
    return result


def handle_jrrp(**kargs) -> str:
    data = {
        "nick": get_nickname(kargs["user_id"], kargs["nickname"]),
        "res": get_jrrp(kargs["self_id"], kargs["user_id"]),
    }
    return format_string(getGlobalMsg("strJrrp"), data)
