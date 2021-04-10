from nonebot.adapters.mirai import Event, Bot, FriendMessage, GroupMessage

from .nb2 import *
from .handle import *

@accept_request.handle()
async def _(bot: Bot, event: Event):
    await event.approve(bot)


@nodice_help.handle()
async def _(bot: Bot, event: Event):
    message = event.get_message().extract_plain_text().strip()
    await bot.send(event, handle_help(message=message))


@nodice_dismiss.handle()
async def _(bot: Bot, event: Event):
    # await bot.send(event,command_dismiss())
    await bot.set_group_leave(group_id=event.group_id)


@nodice_rules.handle()
async def _(bot: Bot, event: Event):
    await bot.send(
        event,
        handle_rules(message=event.get_plaintext().strip(), self_id=event.self_id),
    )


@nodice_jrrp.handle()
async def _(bot: Bot, event: Event):
    await bot.send(
        event,
        handle_jrrp(
            self_id=event.self_id, user_id=event.id, nickname=event.sender.nickname
        ),
    )


@nodice_r.handle()
async def _(bot: Bot, event: GroupMessage):
    message = event.get_message().extract_plain_text().strip()
    user_id = event.sender.id
    nickname = event.sender.name
    group_id = None
    if not isinstance(event, FriendMessage):
        group_id = event.sender.group.id
    await bot.send(
        event,
        handle_r(
            message=message, user_id=user_id, nickname=nickname, group_id=group_id
        ),
    )
