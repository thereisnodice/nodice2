# __init__.py
# 主模块，负责与 Nonebot 交互

from nonebot import on_command,on_message,on_notice
from nonebot.rule import to_me
from nonebot.adapters import Event,Bot
from nonebot.adapters.cqhttp import PrivateMessageEvent,GroupMessageEvent

from .utils import *

nodice_r = on_command("r", priority=5)
@nodice_r.handle()
async def _(bot: Bot, event: Event):
    dice_expression = str(event.get_message()).strip()
    if isinstance(event,PrivateMessageEvent):
        data={'pc':get_nickname(event.sender.user_id,event.sender.nickname),
              'res':getCalculator(dice_expression).extract_roundnum_and_reason(100)}
    elif isinstance(event,GroupMessageEvent):
        data={'pc':get_nickname(event.sender.user_id,event.sender.nickname),
              'res':getCalculator(dice_expression).extract_roundnum_and_reason(get_defaultdice(event.group_id))}
    await bot.send(event,format_string(getGlobalMsg('strRollDice'),data))
set_default_dice= on_command("set", priority=5)
@set_default_dice.handle()
async def _(bot:Bot,event:Event):
    default_dice = int(str(event.get_message()).strip())
    await bot.send(event,str(set_defaultdice(event.group_id,default_dice)))
roll_fate_dice = on_command("rf", priority=4)
@roll_fate_dice.handle()
async def _(bot: Bot, event: Event):
    dice_expression = str(event.get_message()).strip()
    await bot.send(event,format_string(getGlobalMsg('strRollDice'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getCalculator(dice_expression,2).extract_roundnum_and_reason()}))
roll_wod_dice = on_command("w", priority=4)
@roll_wod_dice.handle()
async def _(bot: Bot, event: Event):
    dice_expression = str(event.get_message()).strip()
    await bot.send(event,format_string(getGlobalMsg('strRollDice'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getCalculator(dice_expression,3).extract_roundnum_and_reason()}))
'''
roll_hide = on_command("rh", priority=4)
@roll_hide.handle()
async def _(bot: Bot, event: Event, state: T_State):
    dice_expression = str(event.get_message()).strip()
    await bot.send(event,format_string(getGlobalMsg('strRollHidden'),
                                                    {'pc':event.sender.nickname,
                                                    'res':getCalculator(dice_expression).extract_roundnum_and_reason(100)}))
'''
draw_deck=on_command("draw", priority=5)
@draw_deck.handle()
async def _(bot: Bot, event: Event):
    deck_name = str(event.get_message()).strip()
    await bot.send(event,format_string(getGlobalMsg('strDrawCard'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getDeck().get_value(deck_name)}))
name=on_command("name",priority=5)
@name.handle()
async def _(bot: Bot, event: Event):
    await bot.send(event,format_string(getGlobalMsg('strNameGenerator'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getDeck().get_value('_name_')}))
template_insane=on_command("ti",priority=5)
@template_insane.handle()
async def _(bot: Bot, event: Event):
    await bot.send(event,format_string(getGlobalMsg('strDrawCard'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getDeck().get_value('_即时症状')}))
template_insane=on_command("li",priority=5)
@template_insane.handle()
async def _(bot: Bot, event: Event):
    await bot.send(event,format_string(getGlobalMsg('strDrawCard'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getDeck().get_value('_总结症状')}))
jrrp=on_command("jrrp", priority=5)
@jrrp.handle()
async def _(bot: Bot, event: Event):
    await bot.send(event,format_string(getGlobalMsg('strJrrp'),
                                                    {'nick':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':get_jrrp(event.self_id,event.sender.user_id)}))
rules=on_command("rules", priority=4)
@rules.handle()
async def _(bot: Bot, event: Event):
    rule_name = str(event.get_message()).strip()
    await bot.send(event,get_rules(event.self_id,rule_name))

nodice_coc=on_command("coc",priority=5)
@nodice_coc.handle()
async def _(bot:Bot,event:Event):
    await bot.send(event,get_coc_character())
nodice_dnd=on_command("dnd",priority=5)
@nodice_dnd.handle()
async def _(bot:Bot,event:Event):
    await bot.send(event,get_dnd_character())
    

nodice_nn=on_command("nn",priority=2)
@nodice_nn.handle()
async def _(bot:Bot,event:Event):
    nickname = str(event.get_message()).strip()
    set_nickname(event.sender.user_id,nickname)
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