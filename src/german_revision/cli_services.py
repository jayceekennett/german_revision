# cli_services.py

import shutil
import textwrap

# ------------------------- QUIT APP ------------------------------------------

def quit_app() -> None:
    print("[system message: exiting german-revision.]")
    quit()

# ------------------------- GET ADVICE ----------------------------------------


# ---------- create advice
advice_dict ={
"tmp_advice" : """
In German, extra information in a sentence usually follows this order:
TIME → MANNER → PLACE    
This means:
	•	WHEN something happens (time)
	•	HOW it happens (manner)
	•	WHERE it happens (place)

Example:
Ich gehe heute mit dem Bus zur Arbeit.
TIME   MANNER        PLACE

Breakdown:
	•	heute → when?
	•	mit dem Bus → how?
	•	zur Arbeit → where?
    
IMPORTANT NOTES:
	1.	TMP is the DEFAULT order, not the only possible order.
(German allows flexibility, but TMP is safest.)
	2.	In your exercises, always follow TMP unless told otherwise.
	3.	TMP happens AFTER the verb in normal sentences:
Ich gehe heute mit dem Bus zur Arbeit.
	4.	If TIME is moved to the front:
Heute gehe ich mit dem Bus zur Arbeit.
→ the verb still stays in position 2 (V2 rule).
""",

"v2_advice" : """
V2 WORD ORDER (VERB IN POSITION 2) & INVERSION

In German main clauses, the verb is always in position 2.

IMPORTANT:
Position ≠ second word
Position = second idea (second part of the sentence)

If something other than the subject comes first,
the verb still stays in position 2.

This forces the subject to move AFTER the verb.

RULE:
[ANY ELEMENT] + VERB + SUBJECT + rest

""",

"modal_advice" : """
MODAL VERBS (VERB BRACKET STRUCTURE)

Modal verbs change the meaning of another verb:
	•	können (can)
	•	müssen (must)
	•	wollen (want)
	•	sollen (should)
	•	dürfen (may / be allowed)
 
    
KEY RULE:

In German, modal verbs create a verb bracket:
POSITION 2 → modal verb (conjugated)
END → main verb (infinitive)


BASIC STRUCTURE:
SUBJECT → MODAL VERB → rest → MAIN VERB (at the end)

IMPORTANT:

The main verb is ALWAYS:
	•	in infinitive form
	•	at the END of the sentence

WITH INVERSION:

The same rule applies (V2 still holds): 
    
""",

"subordinate_advice" : """
SUBORDINATE CLAUSES (VERB AT THE END)

A subordinate clause is a clause that depends on another clause.

It usually begins with a conjunction like:
	•	dass (that)
	•	weil (because)
	•	wenn (if / when)
	•	obwohl (although)

    
KEY RULE:
In a subordinate clause, the CONJUGATED verb goes to the END.


BASIC STRUCTURE:
MAIN CLAUSE, + SUBORDINATE CLAUSE

IMPORTANT:

Inside the subordinate clause:
	•	the verb is ALWAYS last
	•	the normal V2 rule does NOT apply


MULTIPLE VERBS:

If there is more than one verb, they ALL go to the end:
    
WORD ORDER INSIDE THE CLAUSE:

Subject usually comes early:
dass ich heute komme

Then time, manner, place (TMP):
dass ich heute mit dem Bus zur Arbeit gehe

""",

"seperable_advice" : """
SEPARABLE VERBS (TRENNBARE VERBEN)

Some German verbs have a prefix that splits off in main clauses.

Common prefixes:
	•	an, auf, ein, aus, mit, vor, zurück, etc.

Example verb:
anrufen (to call)


KEY RULE (MAIN CLAUSE):

The verb SPLITS into two parts:
	•	conjugated verb → position 2
	•	prefix → goes to the END
    
SUBJECT → VERB → rest → PREFIX (at the end)


WITH INVERSION:

The same rule applies.


IMPORTANT:

The prefix is ALWAYS at the END in main clauses.


SUBORDINATE CLAUSES (VERY IMPORTANT):

In subordinate clauses, the verb does NOT split.

The prefix stays attached, and the whole verb goes to the END.

Example:
Ich weiß, dass ich meine Mutter anrufe.


MODAL VERBS:

With modal verbs, the separable verb also stays together at the end:
""",

"negation_advice" : """
NEGATION (NICHT vs KEIN)

German has two main ways to negate:
	•	nicht → negates verbs, adjectives, or whole sentences
	•	kein → negates nouns (like “not a / no”)


KEY RULE:
	•	Use kein for nouns without an article
	•	Use nicht for everything else


KEIN (NEGATING NOUNS)

Use kein when the noun:
	•	has no article
	•	would normally use ein / eine


IMPORTANT:

kein changes form like ein:
	•	kein (masc./neut. nominative)
	•	keinen (masc. accusative)
	•	keine (feminine / plural)
    

NICHT (NEGATING ACTION / SENTENCE)

Use nicht to negate:
	•	verbs
	•	adjectives
	•	the whole sentence
    

PLACEMENT OF NICHT (VERY IMPORTANT)

nicht usually goes as late as possible, but BEFORE what it negates.
"""
}

# ---------- format advice for terminal
def get_terminal_width(default: int = 80) -> int:
    try:
        return shutil.get_terminal_size().columns
    except OSError:
        return default


def wrap_cli_text(text: str, padding: int = 2) -> str:
    width = max(60, get_terminal_width() - padding)

    wrapped_lines = []

    for line in text.splitlines():
        # Preserve empty lines
        if not line.strip():
            wrapped_lines.append("")
            continue

        # Don't wrap separator lines
        if set(line.strip()) in [{"="}, {"-"}]:
            wrapped_lines.append(line[:width])
            continue

        # Preserve indentation
        indent = len(line) - len(line.lstrip())
        wrapped = textwrap.fill(
            line.strip(),
            width=width,
            subsequent_indent=" " * indent,
            initial_indent=" " * indent,
        )

        wrapped_lines.append(wrapped)

    return "\n".join(wrapped_lines)


# ---------- show advice
def show_grammar_advice(advice: str) -> None:
    print(wrap_cli_text(advice))
    
# ---------- show advice options
def get_advice(advice_dict: dict[str, str], ih) -> None:
    advice_map = {
        "V2": "v2_advice",
        "time-manner-place": "tmp_advice",
        "modal": "modal_advice",
        "subordinate": "subordinate_advice",
        "seperable verbs": "seperable_advice",
        "negation": "negation_advice"
    }
    
    print("Choose from rule options: ")
    for k in advice_map.keys():
        print(k)
  
    choice = ih.conditional_accept(accepted = list(advice_map.keys()))
    advice_topic = advice_map.get(choice)
    advice = advice_dict.get(advice_topic)
    show_grammar_advice(advice)
    
def show_help() -> None:
    print(''' 
          --- GERMAN-REVISION HELP ---
          Commands: 
              :quit     = quit app
              :rules    = view grammar rules
              '''
          )
 


    




