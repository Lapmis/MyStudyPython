# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    """
    Функция производит деление 2 числе
    :param arg1: неограниченное число аргументов
    :return: результат деления
    """
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test1():
    assert all_division(9, 3) == 3

def test2():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)

def test3():
    assert all_division(1, 0.1) == 10

def test4_mask():
    assert all_division(-10, -1) == 10

def test5_mask():
    assert all_division(5, -5) == -1
