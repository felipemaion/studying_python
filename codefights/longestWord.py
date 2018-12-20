# https://codefights.com/arcade/intro/level-12/s9qvXv4yTaWg8g4ma
# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

# Example

# For text = "Ready, steady, go!", the output should be
# longestWord(text) = "steady".
import string
def longestWord(text):
    all_chars = string.ascii_letters + string.whitespace + string.punctuation
    text = text.replace("[", " ") # Disgusting... just keep moving...
    new_text = ''.join(filter(all_chars.__contains__, text))
    new_text = new_text.split()
    return max(new_text, key=lambda x: len(x))

print(longestWord("Ready, steady, go!"))


# import string
# def longestWord(text):
#     all_chars = string.ascii_letters + string.whitespace
#     return max(''.join(filter(all_chars.__contains__, text)).split(), key=lambda x: len(x))
