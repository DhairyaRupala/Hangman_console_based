from Words import word_list
from time import sleep
import random
import os


def clear():
    if os.name == 'nt':
        _ = os.system('cls')


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Welcome to Hangman')
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:

        guess = input('Please guess a word or letter').upper()

        if len(guess) == 1 and guess.isalpha():

            if guess in guessed_letters:
                print('You already guessed the letter', guess)
            elif guess not in word:
                print(guess, 'is not in word')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Great ', guess, ' is in the word')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True


        elif len(guess) == len(word) and guess.isalpha():

            if guess in guessed_words:
                print('You alredy guessed the word')
            elif guess != word:
                print(guess, ' is not in the word')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print('Not a valid guess')

        print(display_hangman(tries))
        print(word_completion)
        print()

    if guessed:
        print('Bravo you win')
    else:
        print('Sorry you ran out of the tries the word is ' + word + ' may be next time')


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)

    while input('Play again? (Y/N)').upper() == "Y":
        sleep(2)
        clear()
        word = get_word()
        play(word)

    print("Thanks for playing GLITCH'S game")


if __name__ == "__main__":
    main()
