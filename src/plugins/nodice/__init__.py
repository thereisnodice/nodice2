# __init__.py
# 主模块，负责接收所有的命令并向 utils.py 传递

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp.event import Event
from nonebot.adapters import Bot

from .utils import *
from .message import *
from .calculator import BaseCalculator

roll_dice = on_command("r", priority=5)

@roll_dice.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    dice_expression = str(event.get_message()).strip()
    await bot.send(event,format_string(getGlobalMsg('strRollDice'),
                                                    {'pc':event.sender.nickname,
                                                    'res':BaseCalculator(dice_expression).extract_roundnum_and_reason(100)}))
