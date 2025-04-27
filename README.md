# Evidence: 2 Generating and Cleaning a Restricted Context-Free Grammar
Ian Hernández Hernández - A01276755

## Description
The language we're working with is a simplified subset of English, specifically focused on creating sentences about Marvel superheroes to make it more interesting. The grammar is designed to handle basic sentence structures with subjects, verbs, and objects, along with modifiers and conjunctions to form more complex statements.
## Language structure
Our grammar focuses on several key elements of English:

* Simple declarative sentences (Subject-Verb-Object structure)
* Noun phrases with optional determiners and adjectives
* Verb phrases with optional objects and modifiers
* Prepositional phrases as modifiers
* Compound sentences using conjunctions

Our grammar emphasizes syntactic structure and the relationship between different sentence components.

## Model
Before generating the grammar, here are the words that we'll be using:
### Nouns (NP)
#### Superheroes
* Iron Man
* Spider-Man
* Thor
* Hulk
* Black Widow
* Captain America
* Doctor Strange
* Black Panther

#### Villians:
* Thanos
* Loki
* Ultron
* Green Goblin

##### Objetcs:
* shield
* hammer
* suit
* web
* portal
* stone
* city
* universe

### Verbs (VP)
* fight
* save
* protect
* defeat
* fly
* shoot
* throw
* build
* create
* use

### Determinantes (DET)* 
* the
* a
* an
* this
* that

### Conectores (CONJ)
* and
* or
* but
* because

### Preposiciones (P)
* in
* on
* with
* from
* to
* against

### Adverbios (ADV)
* quickly
* bravely
* secretly
* suddenly

### Adjetivos (ADJ)
* powerful
* amazing
* strong
* intelligent
* brave
* magical
* dangerous
* evil

## Grammar
### Initial grammar
```python
# Rule for a sentence
S -> NP VP
S -> S CONJ S

# Rules for noun phrases
NP -> DET N
NP -> DET ADJ N
NP -> N

# Rules for verb phrases
VP -> V
VP -> V NP
VP -> V PP
VP -> V NP PP

# Rule for prepositional phrases
PP -> PREP NP

# Rule for adverbial modifier
VP -> VP ADV
```
This initial grammar has two key issues:

1. Ambiguity: The rule S -> S CONJ S allows multiple parse trees for sentences with multiple conjunctions, creating ambiguity.
2. Left Recursion: The rules S -> S CONJ S and VP -> VP ADV both contain left recursion, which makes the grammar unsuitable for LL(1) parsing.

### Eliminate Ambiguity
To remove ambiguity, we introduce an intermediate non-terminal S' that handles conjunctions:
```python
# Rule for a sentence
S -> NP VP S'
S' -> CONJ S | ε

# Rules for noun phrases
NP -> DET N
NP -> DET ADJ N
NP -> N

# Rules for verb phrases
VP -> V
VP -> V NP
VP -> V PP
VP -> V NP PP

# Rule for prepositional phrases
PP -> PREP NP

# Rule for adverbial modifier
VP -> VP ADV
```
This modification ensures that for a sentence with conjunctions like "Thor fights and Hulk smashes," there is only one possible parse tree, eliminating ambiguity.

### Eliminate Left Recursion
Left recursion occurs when a non-terminal symbol derives a string that begins with itself. In our original grammar, we had two instances of left recursion:

Left recursion creates significant problems for top-down parsers like LL(1) because:

1. Infinite Loops: When a parser attempts to expand a non-terminal with left recursion, it will repeatedly substitute the non-terminal with itself first, creating an infinite loop.
2. Stack Overflow: In implementation, this causes the parser's stack to grow indefinitely until it crashes.

After addressing ambiguity, we need to eliminate left recursion for LL(1) compatibility. We do this by introducing VP':

``` python
# Rule for a sentence
S -> NP VP S'
S' -> CONJ S | ε

# Rules for noun phrases
NP -> DET N
NP -> DET ADJ N
NP -> N

# Rules for verb phrases
VP -> V VP'
VP' -> NP VP' | PP VP' | NP PP VP' | ADV VP' | ε

# Rule for prepositional phrases
PP -> PREP NP
```

## Grammar that recognizes the language
'''
S -> NP VP S'
S' -> CONJ S | ε

NP -> DET N
NP -> DET ADJ N
NP -> N

VP -> V VP'
VP' -> NP VP' | PP VP' | NP PP VP' | ADV VP' | ε

PP -> PREP NP

N -> "Iron Man" | "Spider-Man" | "Thor" | "Hulk" | "Black Widow" | "Captain America" | "Doctor Strange" | "Black Panther"

N -> "Thanos" | "Loki" | "Ultron" | "Green Goblin"

N -> "shield" | "hammer" | "suit" | "web" | "portal" | "stone" | "city" | "universe"

V -> "fight" | "save" | "protect" | "defeat" | "fly" | "shoot" | "throw" | "build" | "create" | "use"

DET -> "the" | "a" | "an" | "this" | "that"

CONJ -> "and" | "or" | "but" | "because"

PREP -> "in" | "on" | "with" | "from" | "to" | "against"

ADV -> "quickly" | "bravely" | "secretly" | "suddenly"

ADJ -> "powerful" | "amazing" | "strong" | "intelligent" | "brave" | "magical" | "dangerous" | "evil"
'''
## Implementation + Testing
Now that we have our gammar complete let's test it. We'll be working with Google Collabs, so it'll be easier and faster to test the grammar. 
You can just click in here,and it'll take you to the grammar test:
https://colab.research.google.com/drive/1jt0X6AN-sp-hcW53P4pgKN7fI8Luc1pu?usp=sharing 

Another way to do it would be using: Natural Language Toolkit (NLTK). For that follow the next steps: install python (if you don't have it yet) from python.org, clone the repository, navigate to the directory that contains the .py file. Install NLTK by running "pip install nltk" or "brew install python-nltk" (if you're on mac), in your console. Then run the program using the command: python english_grammar.py.

### Correct sentences
Valid sentences in our grammar include:

* Thor fights. (simple subject-verb)
* Spider-Man saves the city. (subject-verb-object)
* The powerful Thor throws the hammer. (subject with adjective, verb, object)
* Iron Man defeats Thanos with a suit. (includes prepositional phrase)
* Thor fights and Hulk smashes. (compound sentence with conjunction)

### Incorrect sentences
* Fights Iron Man Thanos
* The Thor hammer throws
* Iron Man quickly
* The save universe
* Powerful the Thor
* Quickly Thor hammer throws

### Running the program
## Complexity
## Analysis
Chomsky Hierarchy Classification
This grammar is a Context-Free Grammar (Type 2) because:

All left sides of productions are single non-terminals
Right sides contain both terminals and non-terminals
It cannot be classified as a Regular Grammar (Type 3) because it has productions with multiple non-terminals on the right side
It is not a Context-Sensitive Grammar (Type 1) because all productions have a single non-terminal on the left side
## References


