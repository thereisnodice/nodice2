import os

import hjson

from .calculator import ExpressionError

def setGlobalMsg(key:str,value):
    with open(os.path.join(os.path.dirname(__file__),'data','CustomMsg.hjson'),
              'r',encoding='utf-8') as f:
        CustomMsg=hjson.loads(f.read())
    CustomMsg[key]=value
    with open(os.path.join(os.path.dirname(__file__),'data','CustomMsg.hjson'),
              'w',encoding='utf-8') as f:
        f.write(hjson.dumps(CustomMsg))
    
def getGlobalMsg(key:str):
    with open(os.path.join(os.path.dirname(__file__),'data','CustomMsg.hjson'),
              'r',encoding='utf-8') as f:
        CustomMsg=hjson.loads(f.read())
        return CustomMsg[key]

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

# 调试用
if __name__=='__main__':
    print(getGlobalMsg('strRollDice'))