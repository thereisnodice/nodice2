from nonebot import __version__

if int(__version__[0]) == 2:
    from .nb2 import *
else:
    from .nb import *
