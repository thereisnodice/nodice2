from .init import init

from nonebot import get_driver

init()


driver = get_driver()

if "cqhttp" in driver._adapters:
    from .adapters.cqhttp import *

if "mirai" in driver._adapters:
    from .adapters.mirai import *
