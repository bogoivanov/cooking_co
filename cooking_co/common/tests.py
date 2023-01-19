import re
import enchant


def spell_check(s):
    # Create a dictionary for Bulgarian words
    dictionary = enchant.Dict("bg_BG")

    # Split the string into words
    words = s.split()

    # Check the spelling of each word
    for i, word in enumerate(words):
        if not dictionary.check(word):
            # Get a list of suggested corrections for the misspelled word
            suggestions = dictionary.suggest(word)
            # If there are suggestions, use the first one
            if suggestions:
                words[i] = suggestions[0]

    # Join the words back into a single string
    s = ' '.join(words)
    return s


# Test the function
test_string = "Това е теккст"
print(spell_check(test_string))  # Output: "Това е тест"
