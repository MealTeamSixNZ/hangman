import random
import tkinter as tk

with open('dict.txt', 'r') as file: 
    wordList = file.read().splitlines()

root = tk.Tk()
root.title("Hangman Game")
difficultyVar = tk.StringVar(value="easy")

# initialize game
print('Hangman')
missedLetters = ''
correctLetters = ''
isGameEnd = False

def getRandomWord(wordList, difficulty):
    if difficulty == "easy":
        filteredWords = [word for word in wordList if len(word) == 3]
    elif difficulty == "medium":
        filteredWords = [word for word in wordList if 4 <= len(word) <= 5]
    else: # hard
        filteredWords = [word for word in wordList if len(word) >= 6]
    return random.choice(filteredWords)

difficulty = difficultyVar.get()
secretWord = getRandomWord(wordList, difficulty).lower()

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

def updateDisplay():
    hangmanLabel.config(image=hangmanImages[len(missedLetters)])
    blanks = ['_' if letter not in correctLetters else letter for letter in secretWord]
    wordDisplay.config(text=' '.join(blanks))
    missedLabel.config(text='Missed: ' + missedLetters)

def handleGuess(guess):
    global missedLetters, correctLetters, isGameEnd, secretWord
    if guess in secretWord:
        correctLetters += guess
        # check if the player has won
        foundAllLetters = all(letter in correctLetters for letter in secretWord)
        if foundAllLetters:
            resultLabel.config(text="Congratulations, you've won!")
            isGameEnd = True
    else:
        missedLetters += guess
        if len(missedLetters) == 6:
            resultLabel.config(text=f"Sorry, you've lost. The word was: {secretWord}")
            isGameEnd = True
    updateDisplay()

    if isGameEnd:
        for btn in letterButtons:
            btn.config(state=tk.DISABLED)

def resetGame():
    global missedLetters, correctLetters, isGameEnd, secretWord
    missedLetters = ''
    correctLetters = ''
    difficulty = difficultyVar.get()
    isGameEnd = False
    if not customWordVar.get():
        secretWord = getRandomWord(wordList, difficulty).lower()
    for btn in letterButtons:
        btn.config(state=tk.NORMAL)
    resultLabel.config(text='')
    customWordVar.set('')
    updateDisplay()

def handleDifficultyChange():
    currentDifficulty = difficultyVar.get()
    difficultyLabel.config(text=f"The difficulty is: {currentDifficulty}")
    resetGame()


wordDisplay = tk.Label(root, font=('Helvetica', 18))
wordDisplay.pack()

missedLabel = tk.Label(root, font=('Helvetica', 18))
missedLabel.pack()

resultLabel = tk.Label(root, font=('Helvetica', 18))
resultLabel.pack()

resetButton = tk.Button(root, text='Play again', command=resetGame)
resetButton.pack()

letterFrame = tk.Frame(root)
letterFrame.pack()

hangmanImages = [tk.PhotoImage(file=f"./hangmanimages/hangman{step}.png") for step in range(7)]

hangmanLabel = tk.Label(root)
hangmanLabel.pack()

difficultyLabel = tk.Label(root, text=f"The difficulty is: {difficultyVar.get()}", font=('helvetica', 18))
difficultyLabel.pack()


customWordFrame = tk.Frame(root)
customWordFrame.pack()

customWordLabel = tk.Label(customWordFrame, text='Please enter custom word: ')
customWordLabel.pack(side=tk.LEFT)

customWordEntry = tk.Entry(customWordFrame)
customWordEntry.pack(side=tk.LEFT)

customWordVar = tk.StringVar()

def startCustomGame():
    global secretWord
    enteredWord = customWordEntry.get().lower()
    if 2 < len(enteredWord) <= 8:
        secretWord = enteredWord
        customWordVar.set(enteredWord)
        resetGame()
    else:
        resultLabel.config(text="Invalid word. Enter a custom word 3 to 7 letters in length.")

startCustomGameBtn = tk.Button(customWordFrame, text='Start Custom Game', command=startCustomGame)
startCustomGameBtn.pack(side=tk.RIGHT)


tk.Label(root, text="Select Difficulty:").pack()
difficulties = [("Easy","easy"), ("Medium", "medium"), ("Hard", "hard")]
for text, value in difficulties:
    tk.Radiobutton(root, text=text, variable=difficultyVar, value=value, command=handleDifficultyChange).pack()


letterButtons = []
for char in 'abcdefghijklmnopqrstuvwxyz':
    btn = tk.Button(letterFrame, text=char.upper(), command=lambda c=char:handleGuess(c), width=4, height=2)
    btn.pack(side=tk.LEFT)
    letterButtons.append(btn)    

updateDisplay()

# Start the GUI even loop
root.mainloop()

# functions to run the game
# wordList = "hang man new old hangman".split()

# # array of hangman stages
# HANGMAN_PICS = ['''
#   +---+
#       |
#       |
#       |
#      ===''', '''
#   +---+
#   O   |
#       |
#       |
#      ===''', '''
#   +---+
#   O   |
#   |   |
#       |
#      ===''', '''
#   +---+
#   O   |
#  /|   |
#       |
#      ===''', '''
#   +---+
#   O   |
#  /|\  |
#       |
#      ===''', '''
#   +---+
#   O   |
#  /|\  |
#  /    |
#      ===''', '''
#   +---+
#   O   |
#  /|\  |
#  / \  |
#      ===''']

# def displayBoard(missedLetters, correctLetters, secretWord):
#     print(HANGMAN_PICS[len(missedLetters)])
#     print('Missed letters:', end=' ')
#     for letter in missedLetters:
#         print(letter, end=' ')
#     print()
#     blanks = '_' * len(secretWord)  

#     for i in range(len(secretWord)): # Replace blanks with correctly guessed letters.
#         if secretWord[i] in correctLetters:
#             blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

#     for letter in blanks: # Show the secret word with spaces in between each letter.
#         print(letter, end=' ')
#     print()

''' This is for the CLI functionality
# runs through the game by calling functions in loops
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
'''