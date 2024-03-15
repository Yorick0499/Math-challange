from difficulty import *
from game_mode import *

while True:
    print('1. Rozpocznij')
    print('2. Zakończ')

    user_start_input = int(input(': '))
    os.system('clear')

    if user_start_input == 1:
        print('Wybierz poziom trudności:')
        print('1. Łatwy')
        print('2. Średni')
        print('3. Trudny')
        user_difficilty_input = int(input(': '))
        os.system('clear')
        if user_difficilty_input == 1:
            easy()
        elif user_difficilty_input == 2:
            medium()
        elif user_difficilty_input == 3:
            hard()
                
    elif user_start_input == 2:
        break
