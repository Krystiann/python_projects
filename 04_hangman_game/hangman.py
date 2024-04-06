
from random import choice

def game():
    word = choice(['test', 'oko'])

    username = input(f'Hello, whats your name : ')
    print(f'Hi, {username} in Hangman Game !')
    print('*' *40)

    guessed = ''
    tries = 3

    while tries > 0:
        blanks = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('-', end='')
                blanks += 1

        print('\n')

        if blanks == 0:
            print('*' *40 )
            print(f'Congratulatons {username} !')
            print(f'The hidden word is {word.upper()}')
            break


        while True:

            guess = input(f'Enter a letter : ')
            if len(guess) > 1:
                print(f'You must input one letter !')
            else:
                break


        if guess in guessed:
            print(f'You already used: {guess}. Try another letter !')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry, this letter is wrong, tries {tries}. Try again ! ')

        if tries == 0:
            print(f'No more tries, you lose !')
            break



if __name__ == '__main__':
    game()
