#tests1.py


import german_revision.constructors as c
from german_revision.classes import Word, Deck, Verb, Spread, Verb_deck, Plural, Plural_deck
from german_revision.csv_loader import get_csvs, get_verbs
from dataclasses import dataclass
from typing import Optional, List
import random


def test_loading():
    filenames = ["data/adjectives.csv", "data/adverbs.csv", "data/articles.csv",
                 "data/nouns.csv", "data/plural_nouns.csv", "data/verbs.csv",
                 "data/conjugations.csv"]

    data = get_csvs(filenames)

    assert len(data["adjectives"]) == 649
    assert len(data["adjectives"][0]) == 2
    
    assert len(data["adverbs"]) == 254
    assert len(data["adverbs"][0]) == 2
    
    assert len(data["articles"]) == 1782
    assert len(data["articles"][0]) == 2
    
    assert len(data["nouns"]) == 1782
    assert len(data["nouns"][0]) == 2
    
    assert len(data["plural_nouns"]) == 1780
    assert len(data["plural_nouns"][0]) == 2
    
    assert len(data["verbs"]) == 1055
    assert len(data["verbs"][0]) == 2
    
    assert len(data["conjugations"]) == 2898
    assert len(data["conjugations"][0]) == 18
    

def test_constructors():
    filenames = ["data/adjectives.csv", "data/adverbs.csv",
                 "data/nouns.csv","data/verbs.csv"]

    to_load = ["adjectives", "nouns", "adverbs", "verbs"]
    master = {}
    for l in to_load:
        d = c.load_cards_from_csv(filenames, l)
        deck = Deck(name = l, stack = d)
        master[l] = deck
        
    test_deck = master["adjectives"]
    assert isinstance(test_deck, Deck)
    
    german_first = True
    test_spread = c.get_spread(test_deck,(random.randrange(len(test_deck.stack))), german_first)
    assert isinstance(test_spread, Spread)

    test_spread1 = c.get_spread(test_deck,(random.randrange(len(test_deck.stack))), german_first)
    assert test_spread.prompt != test_spread1.prompt
    
    test_deck = master["adverbs"]
    assert isinstance(test_deck, Deck)
    
    test_deck = master["nouns"]
    assert isinstance(test_deck, Deck)
    
    test_deck = master["verbs"]
    assert isinstance(test_deck, Deck)
    
    verb_deck = c.load_verb_deck("data/conjugations.csv")
    assert isinstance(verb_deck, Verb_deck)
    
    n_verbs = 5
    freq = 5
    
    verb_spread = c.get_verb_spread(verb_deck, n_verbs, freq)
    assert isinstance(verb_spread, list)
    assert len(verb_spread) == n_verbs
    
    plural_deck = c.load_plural_deck(["data/plural_nouns.csv"])
    assert isinstance(plural_deck, Plural_deck)
    
    n_plurals = 5
    plural_spread = c.get_plurals_spread(plural_deck, n_plurals)
    assert isinstance(plural_spread, list)
    assert len(plural_spread) == n_plurals
    
    plural_spread1 = c.get_plurals_spread(plural_deck, n_plurals)
    assert plural_spread != plural_spread1
    

def test_spreads():
    filenames = ["data/adjectives.csv", "data/adverbs.csv",
                 "data/nouns.csv","data/verbs.csv"]

    to_load = ["adjectives", "nouns", "adverbs", "verbs"]
    master = {}
    for l in to_load:
        d = c.load_cards_from_csv(filenames, l)
        deck = Deck(name = l, stack = d)
        master[l] = deck
        

    
    
    
    
    
    
    
    
    
    
    
    
        