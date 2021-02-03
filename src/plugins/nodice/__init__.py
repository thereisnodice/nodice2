# __init__.py
# 主模块，负责与 Nonebot 交互

from nonebot import on_command,on_message,on_notice
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Event,Bot

from .utils import *

roll_dice = on_command("r", priority=5)

@roll_dice.handle()
async def _(bot: Bot, event: Event, state: T_State):
    dice_expression = str(event.get_message()).strip()
    await bot.send(event,format_string(getGlobalMsg('strRollDice'),
                                                    {'pc':event.sender.nickname,
                                                    'res':getCalculator(dice_expression).extract_roundnum_and_reason(100)}))

draw_deck=on_command("draw", priority=5)

@draw_deck.handle()
async def _(bot: Bot, event: Event, state: T_State):
    deck_name = str(event.get_message()).strip()
    await bot.send(event,format_string(getGlobalMsg('strDrawCard'),
                                                    {'pc':event.sender.nickname,
                                                    'res':getDeck().get_value(deck_name)}))


'''
group_update=on_message(priority=1)

@group_update.handle()
async def group_update():
    pass

group_invite=on_notice()

@group_invite.handle()
async def group_invite():
    pass
'''