# constructors.py

from german_revision.classes import (Word, Spread, Verb, Verb_deck, 
    Plural, Plural_deck, Article, Article_deck, Sentence, SentenceDeck)
from german_revision.loader import get_csvs, get_verbs, get_json
import random
from typing import List
from pathlib import Path
import json


# ------------------------------ CONSTRUCT WORD -------------------------------

def get_word(pair: tuple, word_type: str) -> Word:
    de, eng = pair
    w = Word(eng, de, word_type, 
             german_first = False) # default is False
    return w

# ------------------------------ CONSTRUCT PLURAL -----------------------------

def get_plural(pair: tuple) -> Plural:
    plural, singular = pair
    p = Plural(singular, plural)         
    return p

# ------------------------------ CONSTRUCT ARTICLE ----------------------------

def get_article(pair: tuple) -> Article:
    article, noun = pair
    a = Article(noun, article)
    return a
    
 # ------------------------------ CONSTRUCT VERB ------------------------------
   
def get_verb(verb_list: list) -> Verb:
    verb_list = list(verb_list)
    infinitive = verb_list[1]
    present = list(verb_list[2:8])
    simple_past = verb_list[8]
    perfect = verb_list[9]
    conjunctive = verb_list[10]
    v = Verb(infinitive = infinitive, 
             pronouns = ["ich", "du", "er/sie/es", "wir", "ihr", "Sie"],
             present = present, 
             simple_past = simple_past,
             perfect = perfect, 
             conjunctive = conjunctive)
    return v

# ------------------------------ CONSTRUCT PLURAL DECK ------------------------

def load_plural_deck(filenames: list) -> Plural_deck:
    data = get_csvs(filenames)
    plural_list = data["plural_nouns"]
    plural_list.pop(0)
    plurals = []
    for p in plural_list:
        tup = tuple(p)
        plurals.append(tup)
    plural_deck = []
    for p in plurals:
        p_to_append = get_plural(p)
        plural_deck.append(p_to_append)
    deck = Plural_deck(name = "plurals", stack = plural_deck)
    return deck

# ------------------------------ CONSTRUCT ARTICLE DECK -----------------------

def load_article_deck(filenames: list) -> Article_deck:
    data = get_csvs(filenames)
    article_list = data["articles"]
    article_list.pop(0)
    articles = []
    for a in article_list:
        tup = tuple(a)
        articles.append(tup)
    article_deck = []
    for a in articles:
        a_to_append = get_article(a)
        article_deck.append(a_to_append)
    deck = Article_deck(name = "plurals", stack = article_deck)
    return deck


# ------------------------------ CONSTRUCT VOCAB DECK -------------------------
     
def load_cards_from_csv(filenames: list, word_type: str) -> List[Word]:
    data = get_csvs(filenames)
    word_type = str(word_type)
    word_list = data[word_type]
    word_list.pop(0)
    words = []
    for w in word_list:
        tup = tuple(w)
        words.append(tup)
    word_deck = []
    for w in words:
        w_to_append = get_word(w, word_type)
        word_deck.append(w_to_append)
    return word_deck


# ------------------------------ CONSTRUCT VERB DECK --------------------------


def load_verb_deck(filename: str) -> Verb_deck:
    df = get_verbs(filename)
    df_transposed = df.T
    verb_deck_list = []
    length = len(df)
    for i in range(length):
        col = list(df_transposed[i])
        v = get_verb(col)
        verb_deck_list.append(v)
    verb_deck = Verb_deck(name = "verbs", stack = verb_deck_list)
    return(verb_deck)

# ------------------------------ CONSTRUCT SENTENCE_DECK ----------------------
def scramble(sentence: str) -> str:
    tokens = sentence.replace(".", "").split()
    random.shuffle(tokens)
    sentence = ", ".join(tokens)
    return sentence


def load_sentence_deck(filepath: str) -> SentenceDeck:
    sentence_bank = get_json(filepath)
    sentence_dict = {}
    for k, v in sentence_bank.items():
        sentence_list = []
        for sentence in v:
            scrambled = scramble(sentence)
            single_sentence = Sentence(k,
                                       scrambled,
                                       sentence)
            sentence_list.append(single_sentence)
        sentence_dict[k] = sentence_list
    
    sentence_deck = SentenceDeck(name = "sentences",
                                 stack = sentence_dict)
    return sentence_deck


def get_sentence_spread(sentence_list: list[Sentence], index: int) -> Sentence:
    sentence =sentence_list[index]
    return sentence 
    

# -------------------------GET VOCAB SPREAD -----------------------------------

def get_spread(deck, index, german_first) -> Spread:
    options = []
    word = deck.stack[index]
    if german_first == True:
        prompt = word.german
        correct = word.english
    else:
        prompt = word.english
        correct = word.german
    options.append(correct)
    pool = [w for w in range(len(deck.stack)) if w != index]
    incorrect_indexes = random.sample(pool, 3)
    incorrect_words = []
    
    for i in incorrect_indexes:
        word  = deck.stack[i]
        if german_first == True:
            incorrect_words.append(word.english)
        else:
            incorrect_words.append(word.german)
    options.extend(incorrect_words)
    random.shuffle(options)
    constructed = Spread(options = options,
                         incorrect_options = incorrect_words, 
                         correct_answer = correct,
                         prompt = prompt)
    return constructed

# ------------------------------ GET VERB SPREAD ------------------------------

def get_verb_spread(deck: Verb_deck, n_verbs: int, freq: int) -> List[Verb]:
    indexes = []
    full_stack = deck.stack
    abb_deck = full_stack[0:freq] 
    abb_deck_length = len(abb_deck)
    for i in range(n_verbs): 
      idx = random.randint(1, abb_deck_length)
      idx = idx - 1
      indexes.append(idx)
    spread = []
    for i in indexes:
        j = abb_deck[i]
        spread.append(j)
    return spread

# ------------------------------ GET PLURAL SPREAD ----------------------------

def get_plurals_spread(deck: Plural_deck, n_plurals: int) -> List[Plural]:
    indexes = []
    full_stack = deck.stack
    length = len(full_stack)
    for i in range(n_plurals):
        idx = random.randint(1, length)
        idx = idx - 1
        indexes.append(idx)
    spread = []
    for i in indexes:
        j = full_stack[i]
        spread.append(j)
    return spread

# ------------------------------ GET ARTICLE SPREAD ---------------------------

def get_article_spread(deck: Article_deck, n_articles: int) -> List[Article]:
    indexes = []
    full_stack = deck.stack
    length = len(full_stack)
    for i in range(n_articles):
        idx = random.randint(1, length)
        idx = idx - 1
        indexes.append(idx)
    spread = []
    for i in indexes:
        j = full_stack[i]
        spread.append(j)
    return spread
  