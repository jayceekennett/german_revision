# engine.py

from german_revision.classes import (Deck, Verb, Spread, Plural, Article, C, 
                                     colour, InputHandler, Sentence)
import german_revision.constructors as c
from german_revision.cli_services import show_help, get_advice, quit_app, advice_dict
import random

# --------------------------- INITIALISE INPUT HANDLER ------------------------

command_map = {
        ":help"  : lambda: show_help(),
        ":rules" : lambda: get_advice(advice_dict, ih),
        ":quit"  : lambda: quit_app()}

ih = InputHandler(command_map)

# --------------------------- PRESENT VERB OPTIONS ----------------------------


def present_verb_choices(verb: Verb):
    inf = verb.infinitive
    print(f"Infinitiv: {inf}")
    i = 0
    while i < len(verb.pronouns):
        print(verb.pronouns[i])
        answer = ih.conditional_type("str")
        if answer == verb.present[i]:
            print(colour("************************ Correct! ***********************\n", C.BOLD, C.GREEN))
            i += 1
        else:
            print(colour(f"The correct answer is: {verb.present[i]}, try again: ", C.RED))
            continue

# --------------------------- PRESENT VOCAB OPTIONS ---------------------------        
# present vocab choices
def present_vocab_choices(spread: Spread, mode: str):
        print(f"German: {spread.prompt} \n")
        while True:
            if mode == "multiple_choice":
                for i, opt in enumerate(spread.options, start=1):
                    print(f"{i}) {opt}")
                raw_answer = ih.conditional_accept([str(1), str(2), str(3), str(4)], spread.options)
                if raw_answer is not None:
                    answer = spread.options[int(raw_answer) - 1]
                else:
                    continue
            else:
                answer = ih.conditional_type("str")
            if answer == spread.correct_answer:
                print(colour("************************ Correct! ***********************\n", C.BOLD, C.GREEN))
                break
            else:
                print(colour(f"********* The correct word is: {spread.correct_answer} *********\n", C.RED))
                print("Try again:")
                continue

# --------------------------- PRESENT PLURAL OPTIONS --------------------------

def present_plurals_choices(plural: Plural):
    while True:
        print(f"Singular: {plural.singular} \n")
        answer = ih.conditional_type("str")
        if answer == plural.plural:
            print(colour("************************ Correct! ***********************\n", C.BOLD, C.GREEN))
            break
        else:
            print(colour(f"********* The correct plural form is: {plural.plural} *********\n", C.RED))
            print("Try again!")
            continue
            
# --------------------------- PRESENT ARTICLE CHOICES -------------------------       
def present_article_choices(article: Article):
    while True:
        print(f"Singular: {article.noun} \n")
        answer = ih.conditional_type("str")
        if answer == article.article:
            print(colour("************************ Correct! ***********************\n", C.BOLD, C.GREEN))
            break
        else:
            print(colour(f"********* The correct plural form is: {article.article} *********\n", C.RED))
            print("Try again!")
            continue

# --------------------------- PRESENT SENTENCE CHOICES ------------------------
       
def present_sentence_choices(sentence: Sentence) -> None:
    print("Unscramble the sentence: ")      
    while True:
        print(f"Scrambled: {sentence.scrambled}")
        answer = ih.conditional_type("str")
        if answer == sentence.correct:
            print(colour("************************ Correct! ***********************\n", C.BOLD, C.GREEN))
            break
        else:
            print(colour(f"Try again! The rule type is {sentence.rule_type}.", C.RED))
            print("Press any key to try again ':A' to see the answer.")
            choice = input("...")
            if choice != ":A":
                continue
            else:
                print(f"The correct answer is: {sentence.correct}")  
                print("Press any key to try again or use :N to go to the next sentence")
                choice = input("...")
                if choice != ":N":
                    continue
                else:
                    break
        

# ---------------------------  LOAD DECKS FROM CSV ----------------------------
# vocab decks
def load_decks():
    filenames = ["data/adjectives.csv", "data/adverbs.csv", "data/articles.csv",
                 "data/nouns.csv", "data/verbs.csv"]
    
    to_load = ["adjectives", "nouns", "adverbs", "articles", "verbs"]
    master = {}
    for l in to_load:
        d = c.load_cards_from_csv(filenames, l)
        deck = Deck(name = l, stack = d)
        master[l] = deck
    plural_deck = c.load_plural_deck(["data/plural_nouns.csv"])
    master["plural_nouns"] = plural_deck
    
    conjugations_deck = c.load_verb_deck("data/conjugations.csv")
    master["conjugations"] = conjugations_deck
    
    article_deck = c.load_article_deck(["data/articles.csv"])
    master["articles"] = article_deck
    
    sentence_deck = c.load_sentence_deck("data/sentence_bank.json")
    master[sentence_deck.name] = sentence_deck
    
    sentence_deck = c.load_sentence_deck("data/hard_sentence_bank.json")
    master["complex sentences"] = sentence_deck
    
    return master

# --------------------------- RUN GAME  ---------------------------------------

def run_game(master: dict[str, Deck], deck_choice: str, 
             german_first: bool | None = False) -> None:
    
    vocab_decks = ["adjectives", "adverbs", "nouns", "verbs"]
    
    if deck_choice in vocab_decks:
        chosen_deck = master[deck_choice]
        print("How many words would you like to practice? ")
        n_words = ih.conditional_type("int")
       
        
        # select mode
        print("Would you like multiple choice (1) or free text (2)? ")
        select_mode = ih.conditional_accept([str(1), str(2)])
        if select_mode == "1":
            mode = "multiple_choice"
        else:
            mode = "free_text"
            
        for i in range(n_words):
            selected_spread = c.get_spread(chosen_deck,
                                          (random.randrange(len(chosen_deck.stack))), 
                                          german_first)
            
            present_vocab_choices(selected_spread, mode)    
    
# --------------------------- VERBS LOGIC 
    elif deck_choice == "conjugations":
        verb_deck = master["conjugations"]
        n_verbs = int(input("How many verbs would you like to practice? \n"))
        print("How common the verbs should these be (e.g. 20 = chosen from 20 most common German verbs)")
        freq = int(input("Please enter a number: "))
        verb_spread = c.get_verb_spread(verb_deck, n_verbs, freq)
        for v in verb_spread:
            present_verb_choices(v)
            
# --------------------------- PLURALS LOGIC    
    elif deck_choice == "plural nouns":
        plural_deck = master["plural_nouns"]
        n_plurals = int(input("How many plurals would you like to practice? \n"))
        plural_spread = c.get_plurals_spread(plural_deck, n_plurals)
        for pl in plural_spread:
            present_plurals_choices(pl)
            
# --------------------------- ARTICLES LOGIC     
    
    elif deck_choice == "articles":
        article_deck = master["articles"]
        n_articles = int(input("How many articles would you like to practice? \n"))
        article_spread = c.get_article_spread(article_deck, n_articles)
        for ar in article_spread:
            present_article_choices(ar)
    
# --------------------------- SENTENCES LOGIC 
    elif deck_choice == "word_order":
        sentence_deck = master["sentences"]
        print("How many sentences would you like to practice?")
        n_sentences = ih.conditional_type("int")
        print("What grammar rule would you like to practice?")
        options = ['basic V2', 'time-manner-place', 'subject-inversion', 'modal verbs', 'perfect tense', 'subordinate clauses']
        print("Options are: ")
        for opt in options:
            print(f"-{opt}")
        choice = ih.conditional_accept(options)  
        sentence_list = sentence_deck.stack[choice]
        
        for i in range(int(n_sentences)):           
            sentence_spread = c.get_sentence_spread(sentence_list,
                                                    (random.randrange(len(sentence_list))))
            
            present_sentence_choices(sentence_spread)
            
    elif deck_choice == "complex_word_order":
        sentence_deck = master["complex sentences"]
        print("How many sentences would you like to practice?")
        n_sentences = ih.conditional_type("int")
        print("What grammar rule would you like to practice?")
        options = ['basic V2', 'time-manner-place', 'subject-inversion', 'modal verbs', 'perfect tense', 'subordinate clauses']
        print("Options are: ")
        for opt in options:
            print(f"-{opt}")
        choice = ih.conditional_accept(options)  
        sentence_list = sentence_deck.stack[choice]
        
        for i in range(int(n_sentences)):           
            sentence_spread = c.get_sentence_spread(sentence_list,
                                                    (random.randrange(len(sentence_list))))
            
            present_sentence_choices(sentence_spread)


    return None