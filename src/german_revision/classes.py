# classes.py

from dataclasses import dataclass
from typing import Optional, List, Any

@dataclass(slots = True)
class Word:
    english: str
    german: str
    word_type: str
    german_first: bool  # True means German is displayed first
    
    @classmethod
    def start_with_german(cls):
        cls.german_first = True
        return(cls)

@dataclass(frozen = True, slots = True)
class Article_pair:
    word: str
    article: str
    
@dataclass(frozen = True, slots = True)
class Spread:
    options: List[Word]
    incorrect_options: List[Word]
    correct_answer: str
    prompt: str
    
@dataclass(slots = True)
class Deck:
    name: str
    stack: List[Word]

    @classmethod
    def set_german_first(self):
        new_deck = []
        name = self.name
        for word in self.stack:
            word.start_with_german()
            new_deck.append(word)   
        return self(name, new_deck)
        
    
@dataclass(frozen = True, slots = True)
class Verb:
    infinitive: str
    pronouns: List[str]
    present: List[str]
    perfect: Optional[List[str]]
    simple_past: Optional[List[str]]
    conjunctive: Optional[List[str]]
    
@dataclass(slots = True)
class Verb_deck:
    name: str
    stack: List[Verb]
    
@dataclass(slots = True)
class Plural:
    singular: str
    plural: str
    
@dataclass(slots = True)
class Plural_deck:
    name: str
    stack: List[Verb]
    
@dataclass(slots = True)
class Article:
    noun: str
    article: str
    
@dataclass(slots = True)
class Article_deck:
    name: str
    stack: List[Verb]

@dataclass(slots = True)
class Sentence:
    rule_type: str
    scrambled: list[str]
    correct: str
    
@dataclass
class SentenceDeck:
    name: str
    stack: List[Sentence]
    
# --------------------------- COLOURS -----------------------------------------
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"

    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"

    BG_RED    = "\033[41m"
    BG_GREEN  = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE   = "\033[44m"
    
    
    
def colour(text: str, *styles: str) -> str:
    return "".join(styles) + text + C.RESET  
    
# --------------------------- INPUTHANDLER ------------------------------------    
class InputHandler:
    def __init__(self, command_map: dict[str, Any]):
        self.command_map = command_map
        
    def _categorise(self, user_input: str):          # identify if input is a command
        usr_input = user_input.strip()     
        if usr_input.startswith(":"):
            usr_input = usr_input.lower()
            usr_input = usr_input.split()[0]
            cmd = True
            return cmd, usr_input
        else:
            cmd = False
            return cmd, usr_input
    
    def _usr_command(self, usr_input: str):          # get command from command map
        if usr_input not in self.command_map.keys():
            print("[system message: invalid command, try again]")
            return None
        else:
            execute = self.command_map[usr_input]
            return execute
        
    def handle(self, user_input):                    # categorise input and get command
        cmd, usr_input = self._categorise(user_input)
        if cmd is True:
            execute = self._usr_command(usr_input)
            return cmd, execute
        elif cmd is False:
            pass
        else:
            print(f"[system message: cmd determination in _categorise is false: returned {type(cmd)}]")
        return cmd, usr_input
    
    def conditional_accept(self, accepted: list[str], spread_options: list[Word] | None = None):
        while True:
            user_input = str(input("...  "))
            cmd, usr_input = self._categorise(user_input)
            if cmd is True:
                try:
                    execute = self._usr_command(usr_input)()
                    return execute
                    break
                except TypeError:
                    continue
            else:
                if usr_input in accepted: 
                    return usr_input   
                    break
                    
                else:
                    if spread_options is not None:
                        print("Possible options are:")
                        for i, opt in enumerate(spread_options, start=1):
                            print(f"{i}) {opt}")
                        continue
                    else:
                        print("Possible options are:")
                        for acc in accepted:
                            print(f"- {acc}")
                        continue
                
    def conditional_type(self, accepted_type: str):
        
        types_dict = {
            "str": lambda x: str(x),
            "list": lambda x: list(x),
            "tuple": lambda x: tuple(x),
            "set": lambda x: set(x),
            "dict": lambda x: dict(x),
            "int": lambda x: int(x)}

        accepted = types_dict.get(accepted_type)
        if accepted is not None:
            while True:
                
                while True:    
                    user_input = str(input("...  "))
                    
                    cmd, usr_input = self._categorise(user_input)
                    if cmd is True:
                        try:
                            execute = self._usr_command(usr_input)()
                            return execute
                            break
                        except TypeError:
                            continue
                    else:
                        try:
                            user_input = accepted(user_input)
                            return user_input
                            break
                        except ValueError:
                            print("Invalid entry, please try again")
                            continue
                break
            
        else:
            print("[system message: invalid desired type]")
    
    
    