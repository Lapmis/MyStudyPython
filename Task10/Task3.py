# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

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


@pytest.mark.parametrize('a, b, result', [
    pytest.param(9, 3, 3, marks=pytest.mark.smoke),
    pytest.param(1, 0, None, marks=pytest.mark.skip('Грусть')),
    (-10, -1, 10),
    (1, 0.1, 10.0),
    (5, -5, -1)
    ])

def test_division(a, b, result):

    assert all_division(a, b) == result


