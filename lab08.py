# lab08.py
# Sydney Wuu
# 4 May 2020

'''My game, entitled Hangman Hacker Edition, fuses together computer science with language. 
After inputting their name, the user will have 15 tries to guess the complete word randomly 
selected from the word bank. I plan to implement for/while loops and if/else statements.
'''

import random
# First, let's make some introductions.
user = input("What's your username?")
print("Hey, " + user, "Let's play Computer Science hangman.")

# Define a list of computer science terms to include within the word bank.
wordBank = ['debugging', 'software', 'program', 'hacker', 'internet', 'engineer', 
'code', 'hardware', 'bus', 'network', 'binary', 'data', 'file', 'Java', 'Python', 
'compiler', 'execute', 'keyword', 'syntax', 'function']

# The 'word' function will randomly select one item from the above list of computer science terminology.
word = random.choice(wordBank)

print('Time to guess!')

guesses = ''
tries = 15