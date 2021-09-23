import json
import random
from pathlib import Path

from .calculator import Calculator

_DECK_PATH = Path() / "data" / "nodice" / "deck"

class Deck:
    deck_list = {}
    result = ""

    def __init__(self):
        self.__load()

    def __load(self) -> "Deck":
        for deck in _DECK_PATH.iterdir():
            self.deck_list.update(json.load(deck.open("r", encoding="utf-8")))
        return self

    def get_value(self, deck: str) -> "Deck":
        
        if deck in self.deck_list:
            self.result = random.choice(self.deck_list[deck])
        else:
            raise Exception
        while "{" in self.result:
            self.get_sub_key()
        while "[" in self.result:
            self.get_calculator()
        return self

    def get_sub_key(self) -> "Deck":
        value = self.result

        l = value[: value.index("}")]
        r = value[value.index("}") + 1 :]
        sub_key = l[l.rindex("{") + 1 :]
        l = l[: l.rindex("{")]
        
        if sub_key[0] == "%":
            sub_key = sub_key[1:]

        self.result = l + Deck().get_value(sub_key).result + r

        return self

    def get_calculator(self) -> "Deck":
        value = self.result

        l = value[: value.index("]")]
        r = value[value.index("]") + 1 :]
        sub_key = l[l.rindex("[") + 1 :]
        l = l[: l.rindex("[")]

        self.result = l + str(Calculator(sub_key).calculate()) + r

        return self
