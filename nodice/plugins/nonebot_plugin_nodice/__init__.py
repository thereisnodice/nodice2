import nonebot

if int(nonebot.__version__[0]) == 2:
    try:
        from .cqhttp import *
    except:
        nonebot.logger.warning("Could not found CQHTTP Adapter !")

    try:
        from .mirai import *
    except:
        nonebot.logger.warning("Could not found MIRAI Adapter !")
else:
    from .nb import *