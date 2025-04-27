# Evidence: 2 Generating and Cleaning a Restricted Context-Free Grammar
Ian Hernández Hernández - A01276755

## Description

## Language structure
## Models
### Nouns (N)
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

### Verbs (V)
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

### Preposiciones (PREP)
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

### Eliminate Ambiguity
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
### Eliminate Left Recursion
```python
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
## Implementation + Testing
### Correct sentences
### Incorrect sentences
### Running the program
## Complexity
## Analysis
## References


