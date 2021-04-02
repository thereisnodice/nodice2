# nb2.py
# 负责与 nonebot2 交互

from nonebot import on_command, on_request
from nonebot.adapters.cqhttp import Event, Bot, PrivateMessageEvent

from .handle import *
from .constant import load_const

load_const()

accept_request = on_request()
nodice_help = on_command("help", priority=5)
nodice_dismiss = on_command("dismiss", priority=5)
nodice_r = on_command("r", priority=5)
nodice_rh = on_command("rh", priority=4)

@accept_request.handle()
async def _(bot: Bot, event: Event):
    await event.approve(bot)

@nodice_help.handle()
async def _(bot: Bot, event: Event):
    message = event.get_message().extract_plain_text().strip()
    await bot.send(event, handle_help(message))

@nodice_dismiss.handle()
async def _(bot: Bot, event: Event):
    # await bot.send(event,command_dismiss())
    await bot.set_group_leave(group_id=event.group_id)

@nodice_r.handle()
async def _(bot: Bot, event: Event):
    message = event.get_message().extract_plain_text().strip()
    user_id = event.sender.user_id
    nickname = event.sender.nickname
    group_id = None
    if not isinstance(event, PrivateMessageEvent):
        group_id = event.group_id
    await bot.send(
        event, handle_r(message, user_id=user_id, nickname=nickname, group_id=group_id)
    )