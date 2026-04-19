# main.py

from .engine import run_game, load_decks

def main():
    print("Welcome to German Revision\n")
    master = load_decks()
    
    while True:
        print(
            "Choose: adjectives (1), adverbs (2), articles (3), "
            "nouns (4), plural nouns (5), verbs (6), conjugations (7), word order (8), or word order (hard) (9)"
        )
    
        deck_map = {
            1: "adjectives",
            2: "adverbs",
            3: "articles",
            4: "nouns",
            5: "plural nouns",
            6: "verbs",
            7: "conjugations",
            8: "word_order",
            9: "complex_word_order"
        }
    
        while True:
            try:
                deck_choice_int = int(input("Your choice: "))
                deck_choice = deck_map.get(deck_choice_int)
                if deck_choice is not None:
                    break
            except ValueError:
                pass
            print("Please enter a number between 1 and 7.\n")
    
        if deck_choice_int in (3, 5, 7, 8, 9):
            german_first = True
        else:
            while True:
                try:
                    lang_choice = int(input("Choose English to German (1) or German to English (2): "))
                    if lang_choice in (1, 2):
                        break
                except ValueError:
                    pass
                print("Please type 1 or 2.\n")
    
            german_first = (lang_choice == 2)
        
        run_game(master, deck_choice, german_first)
    
        choice = input("Would you like to play again? Y/N: ").strip().lower()
        if choice != "y":
            break


if __name__ == "__main__":
    main()





