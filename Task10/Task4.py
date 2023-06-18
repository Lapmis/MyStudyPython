# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

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

@pytest.mark.usefixtures('start_finish')
class TestWithFixture:

    def test1(self):
        assert all_division(9, 3) == 3


    def test2(self, lead_time):
        assert all_division(5, 5) == 1

