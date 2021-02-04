# utils.py
# 工具模块，负责与 __init__.py 交互

import re

from .calculator import getCalculator
from .message import getGlobalMsg
from .deck import getDeck
from .sqlite import create_db,update_db,insert_db,select_db,delete_db
from .others import get_jrrp,get_rules

# 格式化字符串
def format_string(origin_str:str,format_para:dict)->str:
    while(origin_str.find('{')>=0):
        l=origin_str[:origin_str.index('}')]
        r=origin_str[origin_str.index('}')+1:]
        para=l[l.rindex('{')+1:]
        l=l[:l.rindex('{')]
        para=format_para[para]
        origin_str=l+para+r
    return origin_str

# 默认骰
def set_defaultdice(group_id:int,default_dice:int)->bool:
    if(insert_db('group_info',{'id':group_id,'default_dice':default_dice})):
        return True
    else:
        return update_db('group_info',{'default_dice':default_dice},{'id':group_id})
def get_defaultdice(group_id:int)->int:
    default_dice=select_db('group_info',('default_dice',),{'id':group_id})[0]
    if default_dice:
        return default_dice
    else:
        set_defaultdice(group_id,100)
        return 100

# 调试用
if __name__=='__main__':
    print(format_string('{pc}掷骰: {res}',{'pc':'jigsaw','res':'1d100=100'}))
        