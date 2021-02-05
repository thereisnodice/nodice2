# utils.py
# 工具模块，负责与 __init__.py 交互

import re

from .calculator import getCalculator
from .message import getGlobalMsg
from .deck import getDeck
from .sqlite import create_db,update_db,insert_db,select_db,delete_db
from .others import get_jrrp,get_rules
from .character import getCharacterCard

def get_coc_character():
    attr={"力量":'3d6*5', "体质":'3d6*5', "体型":'(2d6+6)*5', 
          "敏捷":'3d6*5', "外貌":'3d6*5', "智力":'(2d6+6)*5', 
          "意志":'3d6*5', "教育":'(2d6+6)*5', "幸运":'3d6*5'}
    return getCharacterCard(attr)

def get_dnd_character():
    attr={"力量":'4d6k3', "体质":'4d6k3', "敏捷":'4d6k3', 
          "智力":'4d6k3', "感知":'4d6k3', "魅力":'4d6k3'}
    return getCharacterCard(attr)

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
    default_dice=select_db('group_info',('default_dice',),{'id':group_id})
    if default_dice:
        return default_dice[0]
    else:
        set_defaultdice(group_id,100)
        return 100
def set_nickname(qq_id:int,nickname:str)->bool:
    if(insert_db('qq_info',{'id':qq_id,'nickname':nickname})):
        return True
    else:
        return update_db('qq_info',{'nickname':nickname},{'id':qq_id})
def get_nickname(qq_id:int,username:str)->str:
    nickname=select_db('qq_info',('nickname',),{'id':qq_id})
    if nickname:
        return nickname[0]
    else:
        return username

# 调试用
if __name__=='__main__':
    print(format_string('{pc}掷骰: {res}',{'pc':'jigsaw','res':'1d100=100'}))
        