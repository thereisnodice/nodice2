import os
import json
import random

import yaml

def getDeck():
    return Deck()

from .utils import getCalculator

deck_path=os.path.join(os.path.dirname(__file__),'data','decks')

class Deck:
    def get_deck_list(self):
        deck_list_json=load_decks()
        message='读取到以下牌堆：'
        for i in deck_list_json.keys():
            if i[0]=='_':continue
            message+='\n'+i
        return message

    def load_decks(self):
        deck_list_data={}
        deck_list = os.listdir(deck_path)
        for i in deck_list:
            f=open(os.path.join(deck_path,i),'r',encoding='utf-8')
            if i[len(i)-1]=='n':deck_list_data.update(json.loads(f.read()))
            else:deck_list_data.update(yaml.load(f.read()))
            f.close()
        return deck_list_data

    def get_value(self,key,num=1,mode=False):
        value_list=self.load_decks()[key]
        message=''
        for i in range(num):
            if mode:
                value=value_list.pop(random.randint(0,len(value_list)-1))
            else:
                value=value_list[random.randint(0,len(value_list)-1)]
            while '{' in value:
                value=self.get_sub_key(value)
            while '[' in value:
                value=self.get_calculator(value)
            if i:message+='\n'
            message+=value
        return message

    def get_sub_key(self,value):
        mode=False
        l=value[:value.index('}')]
        r=value[value.index('}')+1:]
        key_sub=l[l.rindex('{')+1:]
        l=l[:l.rindex('{')]
        if key_sub[0]=='%':
            mode=True
            key_sub=key_sub[1:]

        return l+self.get_value(key_sub,1,mode)+r

    def separate_deckname_and_num(self,args,mode=False):
        args=args.split()
        deckname=args[0]
        try:num=int(args[1])
        except:num=1
        return '抽到了：\n'+self.get_value(deckname,num,mode)

'''
    def get_calculator(self,value):
        l=value[:value.index(']')]
        r=value[value.index(']')+1:]
        key_sub=l[l.rindex('[')+1:]
        l=l[:l.rindex('[')]
        cal=getCalculator(key_sub)
        cal.calculate_with_bracket()
        return l+str(int(cal.result))+r
''' 

# 调试用
if __name__=='__main__':
    deck=Deck()
    print(deck.separate_deckname_and_num(input()))