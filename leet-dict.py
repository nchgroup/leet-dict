import itertools
import sys

leet_dict = {
    "a": ["a", "A", "4", "@"],
    "b": ["b", "B", "8"],
    "c": ["c", "C", "("],
    "d": ["d", "D"],
    "e": ["e", "E", "3"],
    "f": ["f", "F"],
    "g": ["g", "G", "6", "9"],
    "h": ["h", "H"],
    "i": ["i", "I", "1"],
    "k": ["k", "K"],
    "l": ["l", "L", "1"],
    "m": ["m", "M"],
    "n": ["n", "N"],
    "o": ["o", "O", "0"],
    "p": ["p", "P"],
    "q": ["q", "Q", "9"],
    "r": ["r", "R"],
    "s": ["s", "S", "5", "$"],
    "t": ["t", "T", "7"],
    "u": ["u", "U"],
    "v": ["v", "V"],
    "w": ["w", "W"],
    "x": ["x", "X"],
    "y": ["y", "Y"],
    "z": ["z", "Z", "2"],
}

# Check if a word was passed as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <word>")
    sys.exit(1)

word = sys.argv[1].lower()

options_per_character = []
for character in word:
    options = set()
    options.add(character)
    if character.isalpha():
        options.add(character.lower())
        options.add(character.upper())
    character_lower = character.lower()
    if character_lower in leet_dict:
        options.update(leet_dict[character_lower])
    options_per_character.append(list(options))

combinations = itertools.product(*options_per_character)

leet_words = {"".join(combination) for combination in combinations}

for leet_word in leet_words:
    print(leet_word)
