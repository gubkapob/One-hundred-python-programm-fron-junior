# This programm is simple generator of password. Max value lenght=75.
import random

def password_gen(lenght):

    chars = 'abcdefghijklmnopqrstuvwxyz'
    chars += chars.upper()
    nums = str(1234567890)
    chars += nums
    spec_chars = '@#$%^&*()_+-/'
    chars += spec_chars
    rezult = ''.join(random.sample(chars, lenght))

    print(rezult)

if __name__ == '__main__':
    try:
        password_gen(lenght = int(input('Vvedite dlinnu parolya -- ')))
    except:
        print('ValueError: invalid literal for int() or sample larger than population or is negative')
