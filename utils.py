import random
from copy import deepcopy
from typing import Any
import itertools

baseCard = {}
basePile = {}
basePlayer = {}
baseAction = {}

# might need to check these attribs later if they have been defined previously
def addCardAttrib(key, value):
    baseCard[key] = value

def addPileAttrib(key, value):
    if key == 'cards' or key == 'count':
        raise KeyError(f'Cannot directly modify value of {key}')
    basePile[key] = value

def addPlayerAttrib(key, value):
    if key == 'hand':
        raise KeyError(f'Cannot directly modify value of {key}')
    basePlayer[key] = value

def addActionAttrib(key, value):
    baseAction[key] = value

class Card:
    def __init__(self, obj=None):
        for key, value in baseCard.items():
            self.__dict__[key] = deepcopy(value)
        if obj is not None:
            for key, value in obj.items():
                self.__dict__[key] = deepcopy(value)

    def display(self):
        # think about complex stuff next time
        # i.e. object in card
        for key, value in self.__dict__.items():
            print(f'{key}: {value}')

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in self.__dict__.keys():
            old_value = self.__dict__[__name]
            if old_value is None:
                if __value is not None and type(__value) not in [Card, Pile, Player, Action, Object]:
                    raise TypeError(f'Incompatible type, expected Card, Pile, Player, Action, or Object')
            elif __value is None:
                if type(old_value) not in [Card, Pile, Player, Action, Object]:
                    raise TypeError(f'Incompatible type, expected {type(old_value).__name__}')
            if type(old_value) is not type(__value):
                raise TypeError(f'Incompatible type, expected {type(old_value).__name__}')
        self.__dict__[__name] = __value

class Pile:
    def __init__(self, a=None, b=None, mode=None):
        self.__dict__['cards'] = []
        self.__dict__['count'] = 0
        for key, value in basePile.items():
            self.__dict__[key] = deepcopy(value)

        if a is None:
            return
        try:
            if mode == 'mul':
                if isinstance(a, int):
                    self.set_cards(b)
                    self.mul(a)
                elif isinstance(b, int):
                    self.set_cards(a)
                    self.mul(b)
                else:
                    raise Exception()
            else:
                self.set_cards(a)
                self.add(b)
        except:
            raise TypeError(f'Incompatible types, {type(a).__name__} and {type(b).__name__}')

    def set_cards(self, item):
        if isinstance(item, Card):
            self.__dict__['cards'] = [deepcopy(item)]
            self.__dict__['count'] = 1
        elif isinstance(item, Pile):
            self.__dict__['cards'] = deepcopy(item.__dict__['cards'])
            self.__dict__['count'] = item.count
        else:
            raise TypeError('Incompatible type, expected Card or Pile')
                
    def add(self, o):
        other = Pile(o, 1, 'mul')
        self.__dict__['cards'].extend(deepcopy(other.__dict__['cards']))
        self.__dict__['count'] += other.count

    def mul(self, val):
        cards = []
        for _ in range(val):
            cards.extend(deepcopy(self.__dict__['cards']))
        self.__dict__['cards'] = cards
        self.__dict__['count'] *= val

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'cards' or __name == 'count':
            raise AttributeError(f'Cannot directly modify value of {__name}')
        
        if __name in self.__dict__.keys():
            old_value = self.__dict__[__name]
            if old_value is None:
                if __value is not None and type(__value) not in [Card, Pile, Player, Action, Object]:
                    raise TypeError(f'Incompatible type, expected Card, Pile, Player, Action, or Object')
            elif __value is None:
                if type(old_value) not in [Card, Pile, Player, Action, Object]:
                    raise TypeError(f'Incompatible type, expected {type(old_value).__name__}')
            if type(old_value) is not type(__value):
                raise TypeError(f'Incompatible type, expected {type(old_value).__name__}')
        self.__dict__[__name] = __value

    def __getattribute__(self, __name: str) -> Any:
        if __name == 'cards':
            raise AttributeError('Cannot directly access value of cards')
        return object.__getattribute__(self, __name)

    def __getitem__(self, index):
        if isinstance(index, int):
            if index >= self.count:
                raise IndexError('Index out of bounds')
            return self.__dict__['cards'][index]
        else:
            raise TypeError('Index must be an integer')

    def insert(self, card):
        self.__dict__['cards'] = [card] + self.__dict__['cards']
        self.__dict__['count'] = self.count + 1

    def deal(self, val, players):
        if self.count < val * len(players):
            raise MemoryError('Underflow, not enough cards in pile')
        for _ in range(val):
            for player in players:
                card = self.draw()
                player.hand.insert(card)

    def draw(self, idx=0):
        if self.count == 0:
            raise MemoryError('Underflow, no cards left in pile')
        card = self[idx]
        self.__dict__['cards'] = self.__dict__['cards'][0:idx] + self.__dict__['cards'][idx + 1:]
        self.__dict__['count'] = self.count - 1
        return card

    def move(self, card, other):
        idx = -1
        for i in range(self.count):
            if self.__dict__['cards'][i] == card:
                idx = i
                break
        if idx == -1:
            raise LookupError('Card not found')
        card = self.draw(idx)
        other.insert(card)
           
    def shuffle(self):
        random.shuffle(self.__dict__['cards'])

    def peek(self, val):
        if self.count < val:
            raise MemoryError('Underflow, not enough cards in pile')
        for i in range(val):
            self.__dict__['cards'][i].display()

    def pick(self):
        try:
            idx = int(input())
            if idx >= self.count:
                raise
            return self.__dict__['cards'][idx]
        except:
            return None

class Player:
    def __init__(self) -> None:
        self.__dict__['hand'] = Pile()
        for key, value in basePlayer.items():
            self.__dict__[key] = deepcopy(value)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in self.__dict__.keys():
            old_value = self.__dict__[__name]
            if old_value is None:
                if __value is not None and type(__value) not in [Card, Pile, Player, Action, Object]:
                    raise TypeError(f'Incompatible type, expected Card, Pile, Player, Action, or Object')
            elif __value is None:
                if type(old_value) not in [Card, Pile, Player, Action, Object]:
                    raise TypeError(f'Incompatible type, expected {type(old_value).__name__}')
            elif type(old_value) is not type(__value):
                raise TypeError(f'Incompatible type, expected {type(old_value).__name__}')
        self.__dict__[__name] = __value

    def play(self, card, pile):
        self.hand.move(card, pile)

class Action:
    def __init__(self, obj) -> None:
        for key, value in baseAction.items():
            self.__dict__[key] = deepcopy(value)
        if obj is not None:
            for key, value in obj:
                self.__dict__[key] = deepcopy(value)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in self.__dict__.keys():
            old_value = self.__dict__[__name]
            if old_value is None:
                if __value is not None and type(__value) not in [Card, Pile, Player, Action, Object]:
                    raise TypeError(f'Incompatible type, expected Card, Pile, Player, Action, or Object')
            elif __value is None:
                if type(old_value) not in [Card, Pile, Player, Action, Object]:
                    raise TypeError(f'Incompatible type, expected {type(old_value).__name__}')
            if type(old_value) is not type(__value):
                raise TypeError(f'Incompatible type, expected {type(old_value).__name__}')
        self.__dict__[__name] = __value

ActionStack = []
def push(action):
    if not isinstance(action, Action):
        raise TypeError('Incompatible type, expected Action')
    ActionStack.append(action)

def pop():
    if len(ActionStack) == 0:
        raise MemoryError('Underflow, ActionStack is empty')
    action = ActionStack.pop()
    return action
    
def GetInt():
    try:
        return int(input())
    except:
        raise ValueError('Incompatible type, expected int input')

def GetString():
    return input()

class Enum:
    def __init__(self, obj) -> None:
        for key, value in obj.items():
            self.__dict__[key] = deepcopy(value)
    
    def toList(self):
        arr = []
        for _, value in self.__dict__.items():
            arr.append(value)
        return arr

class Object:
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in self.__dict__.keys():
            old_value = self.__dict__[__name]
            if old_value is None:
                if __value is not None and type(__value) not in [Card, Pile, Player, Action, Object]:
                    raise TypeError(f'Incompatible type, expected Card, Pile, Player, Action, or Object')
            elif __value is None:
                if type(old_value) not in [Card, Pile, Player, Action, Object]:
                    raise TypeError(f'Incompatible type, expected {type(old_value).__name__}')
            if type(old_value) is not type(__value):
                raise TypeError(f'Incompatible type, expected {type(old_value).__name__}')
        self.__dict__[__name] = __value

    def has(self, __name: str):
        return __name in self.__dict__.keys()
    
    def combination(self):
        names = []
        vals = []

        for key, value in self.__dict__.items():
            names.append(key)
            if isinstance(value, list):
                vals.append(value)
            elif isinstance(value, Enum):
                vals.append(value.toList())
            else:
                raise TypeError('Incompatible type, expected array or enum')
        
        product = itertools.product(*vals)
        pile = Pile()
        for item in product:
            obj = {}
            for i in range(len(names)):
                obj[names[i]] = item[i]
            pile.add(Card(obj))
        return pile