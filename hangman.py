import random

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

def getRandomWord(wordList):
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

print('Hangman')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(wordList)
isGameEnd = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters+correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        isGameComplete = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                isGameComplete = False
                break
        if isGameComplete:
            print('Fin.')
            isGameEnd = True
    else: 
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You lose.')
            isGameEnd = True
    
    if isGameEnd:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(wordList)
            isGameEnd = False    
        else:
            print('Thanks for playing.')
            break

