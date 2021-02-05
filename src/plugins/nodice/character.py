from .utils import getCalculator

def getCharacterCard(attr:dict)->str:
    result=''
    for i,key in enumerate(attr.keys()):
        if i:result+=','
        cal=getCalculator(attr[key])
        cal.calculate_with_bracket()
        result+=key+': '+str(int(cal.result))
    return result