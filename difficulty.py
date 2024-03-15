import random
from random import randint
import os



operators = ['+', '-', '*']


def easy():
    counter = 0
    scores = 0
    while counter < 5 and scores != 10:
        v1 = randint(1,10)
        v2 = randint(1,10)
        operator = random.choice(operators)
        user_input = int(input(f'{v1} {operator} {v2} = '))
        os.system('clear')
        if operator == operators[0]:
            if user_input == (v1 + v2):
                scores += 1
                print(f'Dobrze! \t Punkty: {scores} \t Błędne odpowiedzi: {counter}')
                continue
            else:
                counter += 1
                print(f'Źle! \t Punkty: {scores} \t Błędne odpowiedzi: {counter}')
                continue
        if operator == operators[1]:
            if user_input == (v1 - v2):
                scores += 1
                print(f'Dobrze! \t Punkty: {scores} \t Błędne odpowiedzi: {counter}')
                continue
            else:
                counter += 1
                print(f'Źle! \t Punkty: {scores} \t Błędne odpowiedzi: {counter}')
                continue
        if operator == operators[2]:
            if user_input == (v1 * v2):
                scores += 1
                print(f'Dobrze! \t Punkty: {scores} \t Błędne odpowiedzi: {counter}')
                continue
            else:
                counter += 1
                print(f'Źle! \t Punkty: {scores} \t Błędne odpowiedzi: {counter}')
                continue
    print(f'\nZdobyłeś/aś {scores} pkt.\n')

def medium():
    counter = 0
    scores = 0
    while counter < 3 and scores != 10:
        v1 = randint(1,20)
        v2 = randint(1,20)
        operator = random.choice(operators)
        user_input = int(input(f'\n{v1} {operator} {v2} = '))
        if operator == operators[0]:
            if user_input == (v1 + v2):
                scores += 1
                print('Dobrze!')
                continue
            else:
                counter += 1
                print('Źle!')
                continue
        if operator == operators[1]:
            if user_input == (v1 - v2):
                scores += 1
                print('Dobrze!')
                continue
            else:
                counter += 1
                print('Źle!')
                continue
        if operator == operators[2]:
            if user_input == (v1 * v2):
                scores += 1
                print('Dobrze!')
                continue
            else:
                counter += 1
                print('Źle!')
                continue
    print(f'\nZdobyłeś/aś {scores} pkt.\n')

def hard():
    counter = 0
    scores = 0
    while counter < 3 and scores != 10:
        v1 = randint(1,10)
        v2 = randint(1,10)
        v3 = randint(1,10)
        operator = random.choice(operators)
        operator2 = random.choice(operators)
        user_input = int(input(f'\n{v1} {operator} {v2} {operator2} {v3} = '))
        if operator == operators[0] and operator2 == operators[0]:
            if user_input == (v1 + v2 + v3):
                scores += 1
                print('Dobrze!')
                continue
            else:
                counter += 1
                print('Źle!')
                continue
        if operator == operators[0] and operator2 == operators[1]:
                if user_input == (v1 + v2 - v3):
                    scores += 1
                    print('Dobrze!')
                    continue
                else:
                    counter += 1
                    print('Źle!')
                    continue
        if operator == operators[0] and operator2 == operators[2]:
            if user_input == (v1 + v2 * v3):
                scores += 1
                print('Dobrze!')
                continue
            else:
                counter += 1
                print('Źle!')
                continue
        if operator == operators[1] and operator2 == operators[0]:
            if user_input == (v1 - v2 + v3):
                scores += 1
                print('Dobrze!')
                continue
            else:
                counter += 1
                print('Źle!')
                continue
        if operator == operators[1] and operator2 == operators[1]:
            if user_input == (v1 - v2 - v3):
                scores += 1
                print('Dobrze!')
                continue
            else:
                counter += 1
                print('Źle!')
                continue
        if operator == operators[1] and operator2 == operators[2]:
            if user_input == (v1 - v2 * v3):
                scores += 1
                print('Dobrze!')
                continue
            else:
                counter += 1
                print('Źle!')
                continue
        if operator == operators[2] and operator2 == operators[0]:
            if user_input == (v1 * v2 + v3):
                scores += 1
                print('Dobrze!')
                continue
            else:
                counter += 1
                print('Źle!')
                continue
        if operator == operators[2] and operator2 == operators[1]:
            if user_input == (v1 * v2 - v3):
                scores += 1
                print('Dobrze!')
                continue
            else:
                counter += 1
                print('Źle!')
                continue
        if operator == operators[2] and operator2 == operators[2]:
            if user_input == (v1 * v2 * v3):
                scores += 1
                print('Dobrze')
                continue
            else:
                counter += 1
                print('Źle!')
                continue
    print(f'\nZdobyłeś/aś {scores} pkt.\n')
