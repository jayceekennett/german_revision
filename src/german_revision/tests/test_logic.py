# test_logic.py

from german_revision.engine import run_game
from unittest.mock import patch

# this mocks input to make the game run to test logic

def test_noun_logic():
    fake_inputs = [
        1, # practice 1 word
        1, # mode - multiple choice
        1] # answer
        
    with patch("builtins.input", side_effect=fake_inputs):
            result = run_game("nouns", german_first = True)
    assert result is None
    
    with patch("builtins.input", side_effect=fake_inputs):
            result = run_game("nouns", german_first = False)
    assert result is None
# the game should run and exit the loop gracefully

    
def test_adjective_logic():
    fake_inputs = [
        1, # practice 1 word
        1, # mode - multiple choice
        1] # answer
        
    with patch("builtins.input", side_effect=fake_inputs):
            result = run_game("adjectives", german_first = True)
    assert result is None
    
    with patch("builtins.input", side_effect=fake_inputs):
            result = run_game("adjectives", german_first = False)
    assert result is None
    
    
def test_adverb_logic():
    fake_inputs = [
        1, # practice 1 word
        1, # mode - multiple choice
        1] # answer
        
    with patch("builtins.input", side_effect=fake_inputs):
            result = run_game("adverbs", german_first = True)
    assert result is None
    
    with patch("builtins.input", side_effect=fake_inputs):
            result = run_game("adverbs", german_first = False)
    assert result is None
    
def test_verb_logic():
    fake_inputs = [
        1, # practice 1 word
        1, # mode - multiple choice
        1] # answer
        
    with patch("builtins.input", side_effect=fake_inputs):
            result = run_game("verbs", german_first = True)
    assert result is None
    
    with patch("builtins.input", side_effect=fake_inputs):
            result = run_game("verbs", german_first = False)
    assert result is None

def test_conjugation_logic():
    fake_inputs = [
        1, # practice 1 word
        1, # frequency 1
        "bin", "bist", "ist", "sind", "seid", "sind"] # answers
        
    with patch("builtins.input", side_effect=fake_inputs):
            result = run_game("conjugations", german_first = True)
    assert result is None
    

def test_game_output(capsys):
    with patch("builtins.input", side_effect=[1, 1, "wrong", "bin", "bist", 
                                              "ist","sind", "seid", "sind"]):
        run_game("conjugations", german_first = True)

    captured = capsys.readouterr()
    assert "The correct answer is bin, try again:" in captured.out
    assert "************************ Correct! ***********************" in captured.out


    