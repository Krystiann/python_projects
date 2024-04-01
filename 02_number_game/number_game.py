from random import randint

random_number: int = randint(0, 20)

while True:
    try:
        user_input: int = int(input('Enter a number from 0 to 20 : '))
    except ValueError:
        print('Invalid number')
        continue

    if user_input > random_number:
        print('Too big a number !')

    elif user_input < random_number:
        print('Too small a number !')

    else:
        print('You won !')
        break


