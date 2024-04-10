import string
import secrets


#Check upper and symbols in generate passwors
def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
        else:
            return False


def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
        else:
            return False


#Generate passwords
def generate_password(lenght: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_lenght: int = len(combination)
    new_password: str = ''

    for _ in range(lenght):
        new_password += combination[secrets.randbelow(combination_lenght)]


    return new_password

#Menu of generate passwords

print(f'Hello, in password generator !')
print('-'*35)
while True:
    number_of_passwords = input(f'How many passwords you want to generate >> ')
    lenght = input(f'Input lenght of password >> ')
    symbols = input(f'Do you want symbols in password (Y/N) >> ')
    uppercase = input(f'Do you want capital letters in password (Y/N) >> ')


    for i in range(0, int(number_of_passwords)):

        if symbols.lower() == 'y' and uppercase.lower() == 'y':
            new_password = generate_password(int(lenght), True, True)
            print(f'{i+1}.   {new_password}')

        elif symbols.lower() == 'y' and uppercase.lower() == 'n':
            new_password = generate_password(int(lenght), True, False)
            print(f'{i+1}.   {new_password}')

        elif symbols.lower() == 'n' and uppercase.lower() == 'y':
            new_password = generate_password(int(lenght), False, True)
            print(f'{i+1}.   {new_password}')

        else:
            new_password = generate_password(lenght, False, False)
            print(f'{i+1}.   {new_password}')

    stop_program = input(f'Do you want exit (Y/N) >>')
    if stop_program.lower() == 'y':
        break
