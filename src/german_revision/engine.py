# engine.py

from german_revision.classes import Deck, Verb, Spread, Plural, Article
import german_revision.constructors as c
import random

# --------------------------- HELPER FUNCTIONS --------------------------------

# present verb choices
def present_verb_choices(verb: Verb):
    inf = verb.infinitive
    print(f"Infinitiv: {inf}")
    i = 0
    while i < len(verb.pronouns):
        print(verb.pronouns[i])
        answer = input("Type here: ")
        if answer == verb.present[i]:
            print("************************ Correct! ***********************\n")
            i += 1
        else:
            print(f"The correct answer is {verb.present[i]}, try again: ")
            continue
        
# present vocab choices
def present_vocab_choices(spread: Spread, mode: str):
        print(f"German: {spread.prompt} \n")
        if mode == "multiple_choice":
            for i, opt in enumerate(spread.options, start=1):
                print(f"{i}) {opt}")
            raw_answer = int(input("Choose 1–4: "))
            answer = spread.options[raw_answer - 1]
        else:
            answer = input("Type here: ")
        if answer == spread.correct_answer:
            print("************************ Correct! ***********************\n")
        else:
            print(f"********* The correct article is: {spread.correct_answer} *********\n")

# present plural choices
def present_plurals_choices(plural: Plural):
    print(f"Singular: {plural.singular} \n")
    answer = input("Plural: ")
    if answer == plural.plural:
        print("************************ Correct! ***********************\n")
    else:
        print(f"********* The correct plural form is: {plural.plural} *********\n")

# present article_choices        
def present_article_choices(article: Article):
    print(f"Singular: {article.noun} \n")
    answer = input("Article: ")
    if answer == article.article:
        print("************************ Correct! ***********************\n")
    else:
        print(f"********* The correct plural form is: {article.article} *********\n")
        
            

# ---------------------------  LOAD DECKS FROM CSV ----------------------------
# vocab decks
filenames = ["data/adjectives.csv", "data/adverbs.csv", "data/articles.csv",
             "data/nouns.csv", "data/plural_nouns.csv", "data/verbs.csv"]

to_load = ["adjectives", "nouns", "adverbs", "verbs", "plural_nouns", "articles"]
master = {}
for l in to_load:
    d = c.load_cards_from_csv(filenames, l)
    deck = Deck(name = l, stack = d)
    master[l] = deck
    
# verb deck
verb_deck = c.load_verb_deck("data/conjugations.csv")

# plural deck
plural_deck = c.load_plural_deck(["data/plural_nouns.csv"])

# article deck
article_deck = c.load_article_deck(["data/articles.csv"])

# --------------------------- VOCAB LOGIC -------------------------------------

def run_game(deck_choice, german_first):
    vocab_decks = ["adjectives", "adverbs", "nouns", "verbs"]
    
    if deck_choice in vocab_decks:
        chosen_deck = master[deck_choice]
        n_words = int(input("How many words would you like to practice? "))
        
        # select mode
        select_mode = input("Would you like multiple choice (1) or free text (2)? ")
        if select_mode == "1":
            mode = "multiple_choice"
        else:
            mode = "free_text"
            
        for i in range(n_words):
            selected_spread = c.get_spread(chosen_deck, 
                                          (random.randrange(len(chosen_deck.stack))), 
                                          german_first)
            present_vocab_choices(selected_spread, mode)

    
# --------------------------- VERBS LOGIC -------------------------------------

    elif deck_choice == "conjugations":
        n_verbs = int(input("How many verbs would you like to practice? \n"))
        print("How common the verbs should these be (e.g. 20 = chosen from 20 most common German verbs)")
        freq = int(input("Please enter a number: "))
        verb_spread = c.get_verb_spread(verb_deck, n_verbs, freq)
        for v in verb_spread:
            present_verb_choices(v)
            
# --------------------------- PLURALS LOGIC -----------------------------------    
    
    elif deck_choice == "plural nouns":
        n_plurals = int(input("How many plurals would you like to practice? \n"))
        plural_spread = c.get_plurals_spread(plural_deck, n_plurals)
        for pl in plural_spread:
            present_plurals_choices(pl)
            
# --------------------------- PLURALS LOGIC -----------------------------------    
    
    elif deck_choice == "articles":
        n_articles = int(input("How many articles would you like to practice? \n"))
        article_spread = c.get_article_spread(article_deck, n_articles)
        for ar in article_spread:
            present_article_choices(ar)
            
            
        
        







