# nonebot.py
# 负责与 Nonebot 交互

from nonebot import on_command
from nonebot.adapters import Event,Bot
from nonebot.adapters.cqhttp import PrivateMessageEvent

from .utils import *    

load_const()

# 命令一律命名为 nodice_command

# 掷骰模块
nodice_r = on_command("r", priority=5)
@nodice_r.handle()
async def _(bot: Bot, event: Event):
    dice_expression = event.get_message().extract_plain_text().strip()
    if isinstance(event,PrivateMessageEvent):
        cal=getCalculator(dice_expression)
        data={'pc':get_nickname(event.sender.user_id,event.sender.nickname),
              'res':cal.extract_roundnum_and_reason(),
              'reason':cal.roll_reason}
    else:
        cal=getCalculator(dice_expression,0,get_defaultdice(event.group_id))
        data={'pc':get_nickname(event.sender.user_id,event.sender.nickname),
              'res':cal.extract_roundnum_and_reason(),
              'reason':cal.roll_reason}

    if cal.roll_reason:
        await bot.send(event,format_string(getGlobalMsg('strRollDiceReason'),data))
    else:
        await bot.send(event,format_string(getGlobalMsg('strRollDice'),data))

nodice_rh = on_command("rh", priority=4)
@nodice_rh.handle()
async def _(bot: Bot, event: Event):
    dice_expression = event.get_message().extract_plain_text().strip()
    if isinstance(event,PrivateMessageEvent):
        cal=getCalculator(dice_expression)
        data={'pc':get_nickname(event.sender.user_id,event.sender.nickname),
              'res':cal.extract_roundnum_and_reason(),
              'reason':cal.roll_reason}
        if cal.roll_reason:
            await bot.send(event,format_string(getGlobalMsg('strRollDiceReason'),data))
        else:
            await bot.send(event,format_string(getGlobalMsg('strRollDice'),data))
    else:
        cal=getCalculator(dice_expression,0,get_defaultdice(event.group_id))
        data={'pc':get_nickname(event.sender.user_id,event.sender.nickname),
              'res':cal.extract_roundnum_and_reason(),
              'reason':cal.roll_reason}
        await bot.send(event,format_string(getGlobalMsg('strRollHidden'),data))
        if cal.roll_reason:
            await bot.call_api('send_private_msg',user_id=event.sender.user_id,message=format_string(getGlobalMsg('strRollDiceReason'),data))
        else:
            await bot.call_api('send_private_msg',user_id=event.sender.user_id,message=format_string(getGlobalMsg('strRollDice'),data))

nodice_set= on_command("set", priority=5)
@nodice_set.handle()    
async def _(bot:Bot,event:Event):
    default_dice = int(event.get_message().extract_plain_text().strip())
    await bot.send(event,str(set_defaultdice(event.group_id,default_dice)))

nodice_rf = on_command("rf", priority=4)
@nodice_rf.handle()
async def _(bot: Bot, event: Event):
    dice_expression = event.get_message().extract_plain_text().strip()
    await bot.send(event,format_string(getGlobalMsg('strRollDice'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getCalculator(dice_expression,2).extract_roundnum_and_reason()}))

nodice_w = on_command("w", priority=4)
@nodice_w.handle()
async def _(bot: Bot, event: Event):
    dice_expression = event.get_message().extract_plain_text().strip()
    await bot.send(event,format_string(getGlobalMsg('strRollDice'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getCalculator(dice_expression,3).extract_roundnum_and_reason()}))

nodice_rarc=on_command(('ra','rc'),priority=4)
@nodice_rarc.handle()
async def _(bot:Bot,event:Event):
    dice_expression = event.get_message().extract_plain_text().strip()
    cal=getCalculator(dice_expression,1)
    await bot.send(event,format_string(getGlobalMsg('strRollCheck'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':cal.roll_check(get_property(event.sender.user_id,'default')),
                                                    'attr':cal.attribute}))

nodice_sc=on_command('sc',priority=4)
@nodice_sc.handle()
async def _(bot:Bot,event:Event):
    dice_expression = event.get_message().extract_plain_text().strip()
    cal=getCalculator(dice_expression,1)
    await bot.send(event,format_string(getGlobalMsg('strRollCheck'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':cal.san_check(get_property(event.sender.user_id,'default')),
                                                    'attr':'理智'}))


# 牌堆模块
nodice_draw=on_command("draw", priority=5)
@nodice_draw.handle()
async def _(bot: Bot, event: Event):
    deck_name = event.get_message().extract_plain_text().strip()
    await bot.send(event,format_string(getGlobalMsg('strDrawCard'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getDeck().get_value(deck_name)}))

nodice_name=on_command("name",priority=5)
@nodice_name.handle()
async def _(bot: Bot, event: Event):
    await bot.send(event,format_string(getGlobalMsg('strNameGenerator'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getDeck().get_value('_name_')}))

nodice_ti=on_command("ti",priority=5)
@nodice_ti.handle()
async def _(bot: Bot, event: Event):
    await bot.send(event,format_string(getGlobalMsg('strDrawCard'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getDeck().get_value('_即时症状')}))

nodice_li=on_command("li",priority=5)
@nodice_li.handle()
async def _(bot: Bot, event: Event):
    await bot.send(event,format_string(getGlobalMsg('strDrawCard'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getDeck().get_value('_总结症状')}))


# 其他模块
nodice_jrrp=on_command("jrrp", priority=5)
@nodice_jrrp.handle()
async def _(bot: Bot, event: Event):
    await bot.send(event,format_string(getGlobalMsg('strJrrp'),
                                                    {'nick':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':get_jrrp(event.self_id,event.sender.user_id)}))

nodice_rules=on_command("rules", priority=4)
@nodice_rules.handle()
async def _(bot: Bot, event: Event):
    rule_name = event.get_message().extract_plain_text().strip()
    await bot.send(event,get_rules(event.self_id,rule_name))


# 人物作成
nodice_coc=on_command("coc",priority=5)
@nodice_coc.handle()
async def _(bot:Bot,event:Event):
    await bot.send(event,get_coc_character())

nodice_dnd=on_command("dnd",priority=5)
@nodice_dnd.handle()
async def _(bot:Bot,event:Event):
    await bot.send(event,get_dnd_character())
    

# 待定
nodice_nn=on_command("nn",priority=2)
@nodice_nn.handle()
async def _(bot:Bot,event:Event):
    nickname = event.get_message().extract_plain_text().strip()
    set_nickname(event.sender.user_id,nickname)

nodice_setstr=on_command("setstr",priority=3)
@nodice_setstr.handle()
async def _(bot:Bot,event:Event):
    value = event.get_message().extract_plain_text().split()
    setGlobalMsg(value[0],value[1])

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