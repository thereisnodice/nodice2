# rule.py
# 自造 rule 用于全局开关以及黑白名单
# 不是 .rules 命令，那玩意儿在 other.py 里。

from nonebot.rule import Rule

def isBan(service: Optional[str] = None, level: Optional[int] = None) -> Rule:
    global warning
    if service and not service in available:
        if ' ' in service and not warning:
            logger.warning('At least 1 space found in the service name')
            warning = True
        available.append(service)

    async def _isInService(bot: Bot, event: Event, state: T_State) -> bool:
        if isinstance(event, MessageEvent):
            if isinstance(event, GroupMessageEvent):
                if service and auth.policy == 0:
                    return auth.check(event.group_id, service)
                elif level and auth.policy == 1:
                    return bool(auth.check(event.group_id) >= level)
            else:
                return True
        elif isinstance(event, NoticeEvent):
            if isinstance(event, FriendAddNoticeEvent) or isinstance(event, FriendRecallNoticeEvent):
                return True
            elif service and auth.policy == 0:
                return auth.check(event.group_id, service)
            elif level and auth.policy == 1:
                return bool(auth.check(event.group_id) >= level)
        elif isinstance(event, RequestEvent):
            if isinstance(event, FriendRequestEvent):
                return True
            elif service and auth.policy == 0:
                return auth.check(event.group_id, service)
            elif level and auth.policy == 1:
                return bool(auth.check(event.group_id) >= level)
        elif isinstance(event, MetaEvent):
            return True
        else:
            logger.warning('Not supported: nonebot_plugin_rauthman')
            return True
    return Rule(_isInService)