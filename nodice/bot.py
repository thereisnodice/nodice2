import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot
from nonebot.adapters.mirai import Bot as MIRAIBot

nonebot.init()

app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
driver.register_adapter("mirai", MIRAIBot)

nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.run(app="bot:app")
