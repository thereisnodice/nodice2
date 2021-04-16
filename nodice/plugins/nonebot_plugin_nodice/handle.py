from .deck import Deck
from .character import get_coc_character, get_dnd_character
from .calculator import Calculator
from .character import Character
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
        cal = Calculator(kargs["message"], get_default_dice(kargs["group_id"]))
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


async def handle_rules(**kargs) -> str:
    result = await get_rules(kargs["self_id"], kargs["message"])
    return result


async def handle_jrrp(**kargs) -> str:
    data = {
        "nick": get_nickname(kargs["user_id"], kargs["nickname"]),
        "res": await get_jrrp(kargs["self_id"], kargs["user_id"]),
    }
    return format_string(getGlobalMsg("strJrrp"), data)


def handle_coc(**kargs) -> str:
    data = {
        "pc": get_nickname(kargs["user_id"], kargs["nickname"]),
        "res": get_coc_character(),
    }
    return format_string(getGlobalMsg("strCOCBuild"), data)


def handle_dnd(**kargs) -> str:
    data = {
        "pc": get_nickname(kargs["user_id"], kargs["nickname"]),
        "res": get_dnd_character(),
    }
    return format_string(getGlobalMsg("strDNDBuild"), data)


def handle_set(**kargs) -> str:
    try:
        set_default_dice(kargs["group_id"],default_dice = int(kargs["message"]))
        return ""
    except ValueError:
        return getGlobalMsg("strSetInvalid")

def handle_st(**kargs) -> str:
    attr = {}
    for each in kargs["message"].split(" "):
        each = each.replace("：", ":").split(":")
        attr[each[0]] = each[1]
    set_attribute(kargs["user_id"], get_current_character(kargs["user_id"],kargs["group_id"]), attr)
    return getGlobalMsg("strSetPropSuccess")

def handle_draw(**kargs) -> str:
    data = {
        "pc": get_nickname(kargs["user_id"], kargs["nickname"]),
        "res": Deck().get_value(kargs["message"]).result,
    }
    return format_string(getGlobalMsg("strDrawCard"), data)

def handle_li(**kargs) -> str:
    result = Deck().get_value("_总结症状").result
    return result

def handle_ti(**kargs) -> str:
    result = Deck().get_value("_即时症状").result
    return result

def handle_name(**kargs) -> str:
    data = {
        "pc": get_nickname(kargs["user_id"], kargs["nickname"]),
        "res": Deck().get_value("_name " + kargs["message"]).result,
    }
    return format_string(getGlobalMsg("strNameGenerator"), data)