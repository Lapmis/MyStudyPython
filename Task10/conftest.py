import time
import pytest
import datetime

@pytest.fixture(scope='class')
def start_finish(request):
    """
    Выводит на печать время начала и окончания теста
    """
    start = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'\nНачало выполнения в {start}\n')
    yield
    finish = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'\nЗавершение работы в {finish}\n')


@pytest.fixture()
def lead_time(request):
    """
    Выводит на печать продолжительность выполнения теста
    """
    start = datetime.datetime.now()
    yield
    time.sleep(2)
    finish = datetime.datetime.now()
    print(f'\nТекущий тест прошел за {(finish - start)}')

