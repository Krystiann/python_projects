from random import randint

def dice_roll(amount: int ) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = randint(1, 6)
        rolls.append(random_roll)

    return rolls

def main():
    while True:
        try:
            user_input: str = input(f'How many times you want to roll the dice (exit): ')

            if user_input.lower() == 'exit':
                print('Thanks for playing')
                break

            print(*dice_roll(int(user_input)), sep=' ')
        except ValueError:
            print(f'Please enter a valid number! ')


if __name__ == '__main__':
    main()
