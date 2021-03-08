from .exchange import getCalculator

def getCharacterCard(attr:dict)->str:
    result=''
    for i,key in enumerate(attr.keys()):
        if i:result+=' '
        cal=getCalculator(attr[key])
        cal.calculate_with_bracket()
        result+=key+': '+str(int(cal.result))
    return result

class CharacterCard:
    def __init__(self,property:dict):
        self.property=property
    def __str__(self):
        return str(self.property)
    def generate(self):
        result=''
        for key in self.property.keys():
            cal=getCalculator(self.property[key])
            cal.calculate_with_bracket()
            result+=key+':'+str(int(cal.result))+' '
        return result
    def count(self):
        return result

def get_coc_character():
    attr={"力量":'3d6*5', "体质":'3d6*5', "体型":'(2d6+6)*5', 
          "敏捷":'3d6*5', "外貌":'3d6*5', "智力":'(2d6+6)*5', 
          "意志":'3d6*5', "教育":'(2d6+6)*5', "幸运":'3d6*5'}
    return BaseCharacterCard(attr).generate()

def get_dnd_character():
    attr={"力量":'4d6k3', "体质":'4d6k3', "敏捷":'4d6k3', 
          "智力":'4d6k3', "感知":'4d6k3', "魅力":'4d6k3'}
    return BaseCharacterCard(attr).generate()