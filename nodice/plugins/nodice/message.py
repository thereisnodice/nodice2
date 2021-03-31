import os

import hjson

def setGlobalMsg(key: str, value):
    with open("data/nodice/CustomMsg.hjson", "r", encoding="utf-8") as f:
        CustomMsg = hjson.loads(f.read())
    CustomMsg[key] = value
    with open("data/nodice/CustomMsg.hjson", "w", encoding="utf-8") as f:
        f.write(hjson.dumps(CustomMsg))


def getGlobalMsg(key: str):
    try:
        with open("data/nodice/CustomMsg.hjson", "r", encoding="utf-8") as f:
            CustomMsg = hjson.loads(f.read())
            return CustomMsg[key]
    except:
        return False


# 格式化字符串
def format_string(origin_str: str, format_para: dict) -> str:
    while origin_str.find("{") >= 0 and origin_str.find("}") >= 0:
        l = origin_str[: origin_str.index("}")]
        r = origin_str[origin_str.index("}") + 1 :]
        para = l[l.rindex("{") + 1 :]
        l = l[: l.rindex("{")]
        if para in format_para.keys():
            para = format_para[para]
        elif getGlobalMsg(para):
            para = getGlobalMsg(para)
        origin_str = l + para + r
    return origin_str


# 调试用
if __name__ == "__main__":
    print(getGlobalMsg("strRollDice"))
