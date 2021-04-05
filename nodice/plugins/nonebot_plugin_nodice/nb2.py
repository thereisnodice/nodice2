from nonebot import on_command, on_request

from .constant import load_const

load_const()

accept_request = on_request()
nodice_help = on_command("help", priority=5)
nodice_dismiss = on_command("dismiss", priority=5)
nodice_r = on_command("r", priority=5)
nodice_rh = on_command("rh", priority=4)
nodice_rules = on_command("rules", priority=4)
nodice_jrrp = on_command("jrrp", priority=5)