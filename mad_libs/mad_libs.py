def get_input(word_type: str):
    user_input: str = input(f'Enter a {word_type} : ')
    return user_input

noun1 = get_input('noun1') #rzeczownik
noun2 = get_input('noun2') #rzeczownik
verb1 = get_input('verb1')         #czasownik
verb2 = get_input('verb2')         #czasownik
adjective1 = get_input('adjective1')                              #przymiotnik


story = f"""Był sobie pewien {noun1}, który był znany z tego, że potrafił {verb1} na komendę.
Pewnego dnia, gdy próbował {verb2}, zauważył, że jego {noun2} zachowuje się dziwnie.
- O rany! Co się dzieje z moim {noun2}? - zawołał.
Wtedy zobaczył małego kodera w postaci robota, który próbował naprawić jego {noun2}.
- Hej! Co ty tu robisz? - zapytał zaskoczony.
- Przepraszam, ale twój {noun2} potrzebował małej poprawki w kodzie! - odpowiedział robot.
- Ależ ja nie prosiłem o programistę-robota! - krzyknął {noun1}.
Wtedy robot zaczął {verb1} wokół {noun1} z radością.
- Ależ to jest niesamowite! - wykrzyknął.
Następnie wspólnie postanowili {verb2} przy użyciu Pythona.
- Wow, nie wiedziałem, że moje życie na {noun1} będzie takie ekscytujące! - powiedział z uśmiechem.
A od tego czasu, ich przygody w kodowaniu były jeszcze bardziej {adjective1}.
"""
print(story)