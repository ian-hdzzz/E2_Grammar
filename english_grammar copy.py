import nltk
from nltk import CFG, ChartParser
import sys
import re

# Definition of the superhero grammar with the updated structure
grammar_text = """
# Syntactic rules
    S -> NP_SG V_SG S_PRIME   
    S -> NP_PL V_PL S_PRIME   
    S_PRIME -> CONJ S | 

    # Rules for singular noun phrases
    NP_SG -> DET N | DET ADJ N | N

    # Rules for plural noun phrases
    NP_PL -> NP_SG CONJ NP_SG   

    # Rules for verb phrases 
    V_SG -> V_S V_OPT | ADV V_S V_OPT        
    V_OPT -> NP_SG PP | NP_SG | PP | ADV | 

    # Rules for verb phrases 
    V_PL -> V_P V_OPT | ADV V_P V_OPT         

    # Rule for prepositional phrases
    PP -> PREP NP_SG | PREP NP_PL

    # Lexical categories
    # Superheroes and villains (N)
    N -> 'iron man' | 'spider-man' | 'thor' | 'hulk' | 'black widow' | 'captain america' | 'doctor strange' | 'black panther'
    N -> 'thanos' | 'loki' | 'ultron' | 'green goblin'

    # Objects (N)
    N -> 'shield' | 'hammer' | 'suit' | 'web' | 'portal' | 'stone' | 'city' | 'universe'

    # Singular Verbs (V_S) - verbs with 's'
    V_S -> 'fights' | 'saves' | 'protects' | 'defeats' | 'flies' | 'shoots' | 'throws' | 'builds' | 'creates' | 'uses'

    # Plural Verbs (V_P) - base form verbs
    V_P -> 'fight' | 'save' | 'protect' | 'defeat' | 'fly' | 'shoot' | 'throw' | 'build' | 'create' | 'use'

    # Determiners (DET)
    DET -> 'the' | 'a' | 'an' | 'this' | 'that'

    # Connectors (CONJ)
    CONJ -> 'and' | 'or' | 'but' | 'because'

    # Prepositions (PREP)
    PREP -> 'in' | 'on' | 'with' | 'from' | 'to' | 'against'

    # Adverbs (ADV)
    ADV -> 'quickly' | 'bravely' | 'secretly' | 'suddenly'

    # Adjectives (ADJ)
    ADJ -> 'powerful' | 'amazing' | 'strong' | 'intelligent' | 'brave' | 'magical' | 'dangerous' | 'evil'
"""

# Load the grammar
grammar = CFG.fromstring(grammar_text)
parser = ChartParser(grammar)

def tokenize(sentence):
    """
    Tokenizes the sentence properly handling compound names
    """
    # List of compound tokens that should be preserved
    compound_tokens = [
        "iron man", "spider-man", "black widow", "captain america", 
        "doctor strange", "black panther", "green goblin"
    ]
    
    # Convert to lowercase
    sentence = sentence.lower()
    
    # Handle compound tokens
    for token in compound_tokens:
        if token in sentence:
            # Replace spaces with a temporary marker
            sentence = sentence.replace(token, token.replace(" ", "_SPACE_"))
    
    # Now split and restore spaces
    tokens = []
    for word in sentence.split():
        if "_SPACE_" in word:
            tokens.append(word.replace("_SPACE_", " "))
        else:
            tokens.append(word)
    
    return tokens

def print_descent_tree(tree, level=0):
    """
    Prints a descent tree representation of the parse tree
    """
    if isinstance(tree, nltk.Tree):
        # Print the node label indented by level
        print("  " * level + tree.label())
        # Process each child with increased indentation
        for child in tree:
            print_descent_tree(child, level + 1)
    else:
        # Print terminal node (token)
        print("  " * level + tree)

def parse_sentence(sentence):
    """
    Analyzes a sentence and returns True if it's valid, False if it's not
    Displays a descent tree for valid sentences
    """
    # Tokenize the sentence
    tokens = tokenize(sentence)
    
    try:
        # Get all possible trees
        trees = list(parser.parse(tokens))
        
        # If there's at least one tree, the sentence is valid
        if trees:
            print(f"\n✅ The sentence '{sentence}' is valid according to the grammar.")
            print("\nParse Tree:")
            
            print("\nSyntax Tree (NLTK format):")
            trees[0].pretty_print()
            return True
        else:
            print(f"\n❌ The sentence '{sentence}' is NOT valid according to the grammar.")
            print(f"Tokens processed: {tokens}")
            return False
    except Exception as e:
        print(f"\n❌ The sentence '{sentence}' is NOT valid according to the grammar.")
        print(f"Error: {e}")
        print(f"Tokens processed: {tokens}")
        return False

def run_test_cases():
    """
    Runs various predefined test cases
    """
    print("\n==== PREDEFINED TEST CASES ====\n")
    
    # Valid sentences
    valid_sentences = [
        "Iron Man defeats Thanos",
        "The powerful Thor throws the hammer",
        "Spider-Man quickly saves the city",
        "Doctor Strange creates a portal with the stone",
        "Captain America fights with the shield",
        "Thor protects the universe and Iron Man defeats Thanos"
    ]
    
    # Invalid sentences
    invalid_sentences = [
        "Fights Iron Man Thanos",
        "The Thor hammer throws",
        "Iron Man quickly",
        "The save universe",
        "Powerful the Thor",
        "Spider-Man and defeat Thanos",
        "Captain America in shield"
    ]
    
    print("--- VALID SENTENCES ---")
    for sentence in valid_sentences:
        parse_sentence(sentence)
        print("-" * 50)
    
    print("\n--- INVALID SENTENCES ---")
    for sentence in invalid_sentences:
        parse_sentence(sentence)
        print("-" * 50)

def interactive_mode():
    """
    Interactive mode for the user to enter sentences
    """
    print("\n==== INTERACTIVE MODE ====")
    print("Enter sentences to verify if they are valid according to the grammar.")
    print("Type 'exit' to end.")
    
    while True:
        sentence = input("\nEnter a sentence: ")
        if sentence.lower() == 'exit':
            break
        
        parse_sentence(sentence)

def main():
    """
    Main function
    """
    print("\n=== SUPERHERO GRAMMAR ANALYZER ===")
    print("\nThis program analyzes sentences according to the defined superhero grammar.")
    
    while True:
        print("\nSelect an option:")
        print("1. Run predefined test cases")
        print("2. Enter sentences manually")
        print("3. Exit")
        
        choice = input("\nOption: ")
        
        if choice == '1':
            run_test_cases()
        elif choice == '2':
            interactive_mode()
        elif choice == '3':
            print("\nGoodbye!")
            sys.exit(0)
        else:
            print("\nInvalid option. Try again.")

if __name__ == "__main__":
    # Check if NLTK is installed
    try:
        import nltk
    except ImportError:
        print("NLTK is not installed. Install it with 'pip install nltk'")
        sys.exit(1)
    
    main()