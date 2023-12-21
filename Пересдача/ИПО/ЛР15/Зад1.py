import time
from functools import wraps

def timeit(method):
    @wraps(method)
    def timed(*args, **kw):
        # Записывает текущее время
        ts = time.monotonic()
        # Выполняет функцию и сохраняет результат
        result = method(*args, **kw)
        # Записывает время после выполнения функции
        te = time.monotonic()
        # Вычисляет разницу между начальным и конечным временем в миллисекундах
        ms = (te - ts) * 1000
        # Формирует строку с аргументами функции
        all_args = ', '.join(tuple(f'{a!r}' for a in args)
                             + tuple(f'{k}={v!r}' for k, v in kw.items()))
        # Выводит имя функции, её аргументы и время выполнения
        print(f'{method.__name__}({all_args}): {ms:2.2f} ms')
        # Возвращает результат функции
        return result
    return timed

# использование:

@timeit
def slow_func(x, y, sleep):
    # Приостанавливает выполнение на заданное количество секунд
    time.sleep(sleep)
    # Возвращает сумму двух чисел
    return x + y

# Вызывает функцию slow_func с аргументами 10, 20 и sleep=2
# Время выполнения функции будет выведено на экран
slow_func(10, 20, sleep=2)
