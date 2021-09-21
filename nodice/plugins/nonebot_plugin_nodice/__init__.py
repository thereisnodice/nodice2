from nonebot import get_driver

from .init import init

init()

driver = get_driver()

if "cqhttp" in driver._adapters:
    from .adapters.cqhttp import *
