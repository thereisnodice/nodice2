import re

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
    print(format_string('{pc}掷骰: {res}',{'pc':'jigsaw','res':'1d100=100'}))
        