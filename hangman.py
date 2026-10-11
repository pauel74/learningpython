from string import ascii_uppercase
import os # unter das os
import random

RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

clear = lambda: os.system('clear')

def game(targetword):
    hearts = 10
    alphabet = ascii_uppercase
    guessedLetters = []
    rightLetters = []
    lettersInTargetWord = list(targetword)

    while True:

        # print word for debugging and hearts left
        if hearts < 7:
            print(YELLOW, end="")
            if hearts < 4:
                print(RED, end="")
        print("Hearts left: " + str(hearts))
        print(RESET, end="")
        # print(targetword) # debugging

        # print alphabet (with colors)
        for x in range(len(alphabet)):
            if x % 9 == 0:
                print() #multiple lines of keyboard
            if alphabet[x] in guessedLetters:
                if alphabet[x] in lettersInTargetWord:
                    print(f"{GREEN + alphabet[x]} " ,end="" + RESET)
                else:
                    print(f"{RED + alphabet[x]} " ,end="" + RESET)
            else:
                print(f"{alphabet[x]} " ,end="")


        # prints the final word like this: __X_Y_
        print("\n")
        for x in range(len(targetword)):
            if lettersInTargetWord[x] in guessedLetters:
                print(lettersInTargetWord[x] + " ", end="")
            else:
                print("_ ", end="")

        # guessing
        guessedLetters.append(input("\n\nYour guess: ").upper())

        clear()

        # checking input
        # win and lose screen
        if guessedLetters[len(guessedLetters)-1] in lettersInTargetWord:
            rightLetters.append(guessedLetters[len(guessedLetters)-1])
            if len(rightLetters) == len(targetword):
                clear()
                print(GREEN + "YOU WON\n" + RESET)
                print("The word was:")
                print(YELLOW + targetword + "\n")
                if input(RESET + "play again? [y/n] ") == "y":
                    booting()
                break
        else:
            hearts = hearts -1
            if hearts == 0:
                clear()
                print(RED + "YOU LOST\n" + RESET)
                print("The word was:")
                print(YELLOW + targetword + "\n")
                if input(RESET + "play again? [y/n] ") == "y":
                    booting()
                break

        # debugging
        # print()
        # print(guessedLetters)
        # print(rightLetters)
        # print(lettersInTargetWord)

# checks if there is a list with words and starts the game if so
def booting():
    clear()
    try:
        with open("hangman.txt", "r", encoding="utf-8") as file:
            fileContent = file.read()

        wordsHangman = fileContent.split() # create array
        targetword = random.choice(wordsHangman) ## choose random array word

        if not wordsHangman: # if not array == true == array is empty
            print("the hangman.txt file cant be empty and needs to contain at least one word")
            if input("try again? [y/n] ") == "y":
                booting()
        else:
            game(targetword.upper())
    except FileNotFoundError:
        print("how to play?")
        print("1. create a file called hangman.txt in the directory where hangman.py is located")
        print("2. write your words with spaces in between into the hangman.txt file")
        print("3. start the program again")
        if input("\nautomatically create a file filled with random words? [y/n] ") == "y":
            open("hangman.txt", "w", encoding="utf-8").write(("computer keyboard monitor printer speaker network browser website program software hardware internet desktop laptop tablet camera router server socket backup update driver binary editor folder python docker script mobile battery charger display storage memory processor graphics wireless bluetooth download upload password account database firewall antivirus algorithm variable function compiler terminal").upper()) #list created with ai
            booting()
            return
        else: return

booting()
