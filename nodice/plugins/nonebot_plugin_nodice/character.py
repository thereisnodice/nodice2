from .calculator import Calculator
#from .data import 

class Character:
    def __init__(self, template: dict):
        self.template = template

    def __str__(self):
        return " ".join(f"{key}:{self.attribute[key]}" for key in self.attribute) + f" 共计: {self.summary}"

    def generate(self):
        self.attribute = {}
        self.summary = 0
        for key in self.template:
            self.attribute[key] = Calculator(self.template[key].upper()).calculate_with_bracket()
            self.summary += self.attribute[key]

def get_coc_character():
    attr = {
        "力量": "3d6*5",
        "体质": "3d6*5",
        "体型": "(2d6+6)*5",
        "敏捷": "3d6*5",
        "外貌": "3d6*5",
        "智力": "(2d6+6)*5",
        "意志": "3d6*5",
        "教育": "(2d6+6)*5",
        "幸运": "3d6*5",
    }
    char = Character(attr)
    char.generate()
    return str(char)

def get_dnd_character():
    attr = {
        "力量": "4d6k3",
        "体质": "4d6k3",
        "敏捷": "4d6k3",
        "智力": "4d6k3",
        "感知": "4d6k3",
        "魅力": "4d6k3",
    }
    char = Character(attr)
    char.generate()
    return str(char)

if __name__ == "__main__":
    print(str(get_dnd_character()))