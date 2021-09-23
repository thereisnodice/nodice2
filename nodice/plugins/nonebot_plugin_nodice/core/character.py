from typing import Union, Dict

from .calculator import Calculator
from .data import get_attribute, set_attribute


class Character:
    def __init__(self, template: Union[Dict[str, str], str]):
        if isinstance(template, dict):
            self.__template = template
        else:
            self.__template = eval(template)

    def __str__(self):
        return (
            " ".join(f"{key}:{self.__attribute[key]}" for key in self.__attribute)
            + f" 共计: {self.__summary}"
        )

    def generate(self) -> "Character":
        self.__attribute = {}
        self.__summary = 0
        for key in self.__template:
            self.__attribute[key] = Calculator(self.__template[key]).calculate()
            self.summary += self.__attribute[key]
        return self


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
    return str(Character(attr).generate())


def get_dnd_character():
    attr = {
        "力量": "4d6k3",
        "体质": "4d6k3",
        "敏捷": "4d6k3",
        "智力": "4d6k3",
        "感知": "4d6k3",
        "魅力": "4d6k3",
    }
    return str(Character(attr).generate())
