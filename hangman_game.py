import random # for random genertion

words = ["java", "python", "script", "kotlin", "code", "javascript", "program"] # total word list
attempts = 6 # number of incorrect guessess allowed
guessed = [] # all user guessed numbers
progress = [] # tracks user progress through word

solved = False # checks if word is solved

    # selecting random word
num = random.randint(0, (len(words) - 1))
word = words[num]

for letter in word: #provides correct number of blank spaces for word length
    progress.append("_")

print(*progress) # prints progress to show total number of letters in word

guess = input("Guess a letter:\n") # taking user input


while attempts > 0 and solved == False: # main game loop

    if guess not in guessed: # checking if guessed letter has already been guessed

        if guess in word:
            for index, letter in enumerate(word): #replaces progress blank spaces with letter position
                if guess == letter:
                    progress[index] = guess
                else:
                    pass

        else:
            print("Not in the word!")
            attempts -= 1

        guessed.append(guess) # adds guessed number to list of previosuly guessed numbers

    else:
        print("Already guessed")

    if "_" not in progress: #prevents the loop from restarting if all blank spaces are filled
        solved = True

    if solved == False: # only shows if game is not solved
        print(*progress)
        guess = input("Guess a letter:\n")


if attempts == 0: # ending game because of too many failed choices
    print("Sorry you ran out of guesses! Feel free to play again!")

if solved == True: # ending the game because the word was solved
    print(f"You got it! The word was {word}!")
