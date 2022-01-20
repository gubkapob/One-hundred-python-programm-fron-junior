"""
In this game you need to guess what number is hidden 
"""

import random
import time

print('Необходимо угадать загаданное число от 1 до 100')
time.sleep(5)
start_time = time.time()

def game():

    ansver = random.randint(1, 100)

    while True:
        try:
            user_guess = int(input('Введите число ___'))

            if user_guess < 1 or user_guess > 100:
                print('Внимание! Значение должно быть в интервале от 1 до 100')

            elif user_guess == ansver:
                print(f'Верно! Правильный ответ {user_guess}')
                break

            elif user_guess < ansver:
                print(f'Число {user_guess} меньще загаданного!')

            else:
                print(f'Число {user_guess} больше загаданного!')

        except ValueError:
            print('Невалидное значение')
    print('')
    print("--- На поиск ответа вы потратили %s seconds ---" % round(time.time() - start_time))
game()