from nonebot.adapters.cqhttp import Event, Bot, PrivateMessageEvent

from ..handle import *
from ..matcher import *


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
        await handle_rules(message=event.get_plaintext().strip(), self_id=event.self_id),
    )


@nodice_jrrp.handle()
async def _(bot: Bot, event: Event):
    print(nodice_jrrp.module)
    await bot.send(
        event,
        await handle_jrrp(
            self_id=event.self_id, user_id=event.user_id, nickname=event.sender.nickname
        ),
    )


@nodice_r.handle()
async def _(bot: Bot, event: Event):
    message = event.get_message().extract_plain_text().strip()
    user_id = event.sender.user_id
    nickname = event.sender.nickname
    group_id = None
    if not isinstance(event, PrivateMessageEvent):
        group_id = event.group_id
    await bot.send(
        event,
        handle_r(
            message=message, user_id=user_id, nickname=nickname, group_id=group_id
        ),
    )


@nodice_coc.handle()
async def _(bot: Bot, event: Event):
    message = event.get_message().extract_plain_text().strip()
    user_id = event.sender.user_id
    nickname = event.sender.nickname
    await bot.send(
        event,
        handle_coc(message=message, user_id=user_id, nickname=nickname),
    )


@nodice_dnd.handle()
async def _(bot: Bot, event: Event):
    message = event.get_message().extract_plain_text().strip()
    user_id = event.sender.user_id
    nickname = event.sender.nickname
    await bot.send(
        event,
        handle_dnd(message=message, user_id=user_id, nickname=nickname),
    )

@nodice_st.handle()
async def _(bot: Bot, event: Event):
    message = event.get_message().extract_plain_text().strip()
    user_id = event.sender.user_id
    group_id = None
    if not isinstance(event, PrivateMessageEvent):
        group_id = event.group_id
    nickname = event.sender.nickname
    await bot.send(
        event,
        handle_st(message=message, user_id=user_id, nickname=nickname, group_id=group_id
        )
    )

@nodice_draw.handle()
async def _(bot: Bot, event: Event):
    message = event.get_message().extract_plain_text().strip()
    user_id = event.sender.user_id
    group_id = None
    if not isinstance(event, PrivateMessageEvent):
        group_id = event.group_id
    nickname = event.sender.nickname
    await bot.send(
        event,
        handle_draw(message=message, user_id=user_id, nickname=nickname, group_id=group_id
        )
    )

@nodice_ti.handle()
async def _(bot: Bot, event: Event):
    message = event.get_message().extract_plain_text().strip()
    user_id = event.sender.user_id
    group_id = None
    if not isinstance(event, PrivateMessageEvent):
        group_id = event.group_id
    nickname = event.sender.nickname
    await bot.send(
        event,
        handle_ti(message=message, user_id=user_id, nickname=nickname, group_id=group_id
        )
    )

@nodice_li.handle()
async def _(bot: Bot, event: Event):
    message = event.get_message().extract_plain_text().strip()
    user_id = event.sender.user_id
    group_id = None
    if not isinstance(event, PrivateMessageEvent):
        group_id = event.group_id
    nickname = event.sender.nickname
    await bot.send(
        event,
        handle_li(message=message, user_id=user_id, nickname=nickname, group_id=group_id
        )
    )

@nodice_name.handle()
async def _(bot: Bot, event: Event):
    message = event.get_message().extract_plain_text().strip()
    user_id = event.sender.user_id
    group_id = None
    if not isinstance(event, PrivateMessageEvent):
        group_id = event.group_id
    nickname = event.sender.nickname
    await bot.send(
        event,
        handle_name(message=message, user_id=user_id, nickname=nickname, group_id=group_id
        )
    )