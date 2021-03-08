# command.py
# 与 nonebot 完全松耦合的命令实现

from .exchange import *

# 命令函数一律命名为 nodice_command

def r(message:str,**kargs)->str:
    if not 'group_id' in kargs.keys():
        cal=getCalculator(message)
        data={'pc':get_nickname(kargs['user_id'],kargs['nickname']),
              'res':cal.extract_roundnum_and_reason(),
              'reason':cal.roll_reason}
    else:
        cal=getCalculator(message,0,get_defaultdice(kargs['group_id']))
        data={'pc':get_nickname(kargs['user_id'],kargs['nickname']),
              'res':cal.extract_roundnum_and_reason(),
              'reason':cal.roll_reason}

    if cal.roll_reason:
        return format_string(getGlobalMsg('strRollDiceReason'),data)
    else:
        return format_string(getGlobalMsg('strRollDice'),data)

def help(message:str)->str:
    result=getHelpDoc(message)
    if getHelpDoc(message):
        return result
    else:
        return getGlobalMsg('strHlpMsg')

def dismiss()->str:
    result=getGlobalMsg('strDismiss')
    return result
'''
def nodice_rh(message:str,**kargs)->str:
    if not 'group_id' in kargs.keys():
        cal=getCalculator(message)
        data={'pc':get_nickname(kargs['user_id'],kargs['nickname']),
              'res':cal.extract_roundnum_and_reason(),
              'reason':cal.roll_reason}

        if cal.roll_reason:
            return format_string(getGlobalMsg('strRollDiceReason'),data)
        else:
            return format_string(getGlobalMsg('strRollDice'),data)
    else:
        cal=getCalculator(message,0,get_defaultdice(kargs['group_id']))
        data={'pc':get_nickname(kargs['user_id'],kargs['nickname']),
              'res':cal.extract_roundnum_and_reason(),
              'reason':cal.roll_reason}
        group_result=format_string(getGlobalMsg('strRollHidden'),data)
        if cal.roll_reason:
            private_result=format_string(getGlobalMsg('strRollDiceReason'),data)
        else:
             private_result=message=format_string(getGlobalMsg('strRollDice'),data)
        return group_result,private_result

def nodice_set(bot:Bot,event:Event):
    default_dice = int(event.get_message().extract_plain_text().strip())
    await bot.send(event,str(set_defaultdice(event.group_id,default_dice)))

def nodice_rf(bot: Bot, event: Event):
    dice_expression = event.get_message().extract_plain_text().strip()
    await bot.send(event,format_string(getGlobalMsg('strRollDice'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getCalculator(dice_expression,2).extract_roundnum_and_reason()}))

def nodice_w(bot: Bot, event: Event):
    dice_expression = event.get_message().extract_plain_text().strip()
    await bot.send(event,format_string(getGlobalMsg('strRollDice'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getCalculator(dice_expression,3).extract_roundnum_and_reason()}))

def _(bot:Bot,event:Event):
    dice_expression = event.get_message().extract_plain_text().strip()
    cal=getCalculator(dice_expression,1)
    await bot.send(event,format_string(getGlobalMsg('strRollCheck'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':cal.roll_check(get_property(event.sender.user_id,'default')),
                                                    'attr':cal.attribute}))

def _(bot:Bot,event:Event):
    dice_expression = event.get_message().extract_plain_text().strip()
    cal=getCalculator(dice_expression,1)
    await bot.send(event,format_string(getGlobalMsg('strRollCheck'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':cal.san_check(get_property(event.sender.user_id,'default')),
                                                    'attr':'理智'}))


# 牌堆模块


def _(bot: Bot, event: Event):
    deck_name = event.get_message().extract_plain_text().strip()
    await bot.send(event,format_string(getGlobalMsg('strDrawCard'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getDeck().get_value(deck_name)}))



def _(bot: Bot, event: Event):
    await bot.send(event,format_string(getGlobalMsg('strNameGenerator'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getDeck().get_value('_name_')}))



def _(bot: Bot, event: Event):
    await bot.send(event,format_string(getGlobalMsg('strDrawCard'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getDeck().get_value('_即时症状')}))



def _(bot: Bot, event: Event):
    await bot.send(event,format_string(getGlobalMsg('strDrawCard'),
                                                    {'pc':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':getDeck().get_value('_总结症状')}))


# 其他模块


def _(bot: Bot, event: Event):
    await bot.send(event,format_string(getGlobalMsg('strJrrp'),
                                                    {'nick':get_nickname(event.sender.user_id,event.sender.nickname),
                                                    'res':get_jrrp(event.self_id,event.sender.user_id)}))



def _(bot: Bot, event: Event):
    rule_name = event.get_message().extract_plain_text().strip()
    await bot.send(event,get_rules(event.self_id,rule_name))


# 人物作成


def _(bot:Bot,event:Event):
    await bot.send(event,get_coc_character())



def _(bot:Bot,event:Event):
    await bot.send(event,get_dnd_character())
    

# 待定


def _(bot:Bot,event:Event):
    nickname = event.get_message().extract_plain_text().strip()
    set_nickname(event.sender.user_id,nickname)



def _(bot:Bot,event:Event):
    value = event.get_message().extract_plain_text().split()
    setGlobalMsg(value[0],value[1])'''