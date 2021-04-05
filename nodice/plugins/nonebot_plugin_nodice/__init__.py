from nonebot import __version__

if int(__version__[0]) == 2:
    from .cqhttp import *
    from .mirai import *
else:
    from .nb import *