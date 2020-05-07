# lab08.py
# Sydney Wuu
# 4 May 2020

'''My game, entitled Hangman Hacker Edition, fuses together computer science with language. 
After inputting their name, the user will have 15 tries to guess the complete word randomly 
selected from the word bank. I plan to implement for/while loops and if/else statements.
'''

import random
# First, let's make some introductions.
user = input("What's your username? ")
print("Hey, " + user, "Let's play Computer Science hangman.")

# Define a list of computer science terms to include within the word bank.
wordBank = ['debugging', 'software', 'program', 'hacker', 'internet', 'engineer', 
'code', 'hardware', 'bus', 'network', 'binary', 'data', 'file', 'Java', 'Python', 
'compiler', 'execute', 'keyword', 'syntax', 'function']

# The 'word' function will randomly select one item from the above list of computer science terminology.
word = random.choice(wordBank)

print('Time to guess!')

# Set the initial number of tries equal to zero.
guesses = ''
tries = 15

# Let's create a while loop.
while tries > 0:
    # When the user does not exceed 15 failed tries, wrong = 0.
    wrong = 0

    # We are going to tackle each character guess, one at a time.
    for char in word:
        if char in guesses:
            print(char)

        # If the user's guess matches a letter(s) in the word, print the letter in its relative position.
        # There will be a dash for every space the user has yet to guess.
        # For every wrong guess, 1 is added to the tally.
        else:
            print('_')
            wrong += 1
    
    # If the user does not run out of tries and have guessed the word completely, they win!
    if wrong == 0:
        print('Congrats! You win!')
        print('You guessed the correct word: ', word)
    
    # Obtain user input/guess.
    userCharacter = input("What is your character?")

    # Each input will be stored in 'guesses.'
    guesses += userCharacter
    
    # Verify if the user input matches the character in the word. If they don't match, subtract one try from the initial 15.
    if userCharacter not in word:
        tries -= 1
        print("Sorry, you are incorrect.")
        print('You have', + tries, 'more guesses available.')
    
    # If the user runs out of tries, they lose.
    if tries == 0:
        print ('Sorry, you lose. Try again!')