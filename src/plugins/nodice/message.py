import os

import hjson

def getGlobalMsg(str):
    with open(os.path.join(os.path.dirname(__file__),'data','CustomMsg.hjson'),
              'r',encoding='utf-8') as f:
        CustomMsg=hjson.loads(f.read())
        return CustomMsg[str]
        
# 调试用
if __name__=='__main__':
    print(getGlobalMsg('strRollDice'))