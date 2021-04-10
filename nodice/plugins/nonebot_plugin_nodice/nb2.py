from nonebot import on_command, on_request

from .constant import load_const

load_const()

# 待删除
accept_request = on_request()

nodice_coc = on_command("coc", priority=5)
nodice_dnd = on_command("dnd", priority=5)
nodice_dismiss = on_command("dismiss", priority=5)
nodice_draw = on_command("draw", priority=5)
nodice_en = on_command("en", priority=5)
nodice_help = on_command("help", priority=5)
nodice_jrrp = on_command("jrrp", priority=5)
nodice_name = on_command("name", priority=5)
nodice_nn = on_command("nn", priority=5)
nodice_ob = on_command("ob", priority=5)
nodice_pc = on_command("pc", priority=5)
nodice_r = on_command("r", priority=5)
nodice_rh = on_command("rh", priority=4)
nodice_rc = on_command("rc", priority=4)
nodice_ri = on_command("ri", priority=4)
nodice_rules = on_command("rules", priority=4)
nodice_sc = on_command("sc", priority=5)
nodice_set = on_command("set", priority=5)
nodice_setcoc = on_command("setcoc", priority=4)
nodice_st = on_command("st", priority=5)
nodice_w = on_command("w", priority=5)
nodice_welcome = on_command("welcome", priority=4)
