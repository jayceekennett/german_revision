# classes.py

from dataclasses import dataclass
from typing import Optional, List

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

    
    
    
    
    
    
    
    