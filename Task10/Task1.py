# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
def generate_random_name():
    """
    Функция-генератор случайных 2 латинских слов длиной от 1 до 15 символов
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    name = ''
    while True:
        for i in range(2):
            word = [random.choice(alphabet) for i in range(random.randint(1, 15))]
            name += ''.join(word) + ' '
        yield name.rstrip()
        name = ''

gen = generate_random_name()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
