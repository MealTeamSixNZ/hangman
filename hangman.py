import random
dict={1:"hang", 2:"man", 3:"new", 4:"old", 5:"hangman"}
random_num = random.randint(1,5)
print(dict[random_num])

# array with lines and what makes the hangman
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
# function to display board
wordList = "hang man new old hangman".split()

def getRandomWords(wordList)
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secretWord)  

    for i in range(len(secretWord)): # Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


# CLI or GUI

# user input with for loop
'''
guess = input("Take a guess! ")
add guess letter to array of guessed?
start guess counter at 0, add 1 each guess
'''

# implement error handling
'''
if guess = any of guessed db/array
    print "That letter has already been guessed"

allow only one character to be guessed

allow only alphabet to be guessed
'''

# success and loss exit loop

# guess counter & loss/win condition
''' 
def guess counter 
if guess counter = 0  
        print "Hanged Man!"
    if guess counter =! 0 and complete guess = random word
        print "Man was not hanged, well done!"
'''
# stats/record keeping

