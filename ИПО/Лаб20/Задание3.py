# Импортируем необходимые функции из модуля urllib.parse
from urllib.parse import urlparse, urlunparse

# Задаем URL-адрес, который нужно разобрать и затем собрать обратно
url = 'https://www.foxbusiness.com/lifestyle/chemical-found-in-cheerios-quaker-oats-other-oat-based-foods-linked-potential-health-issues-study'

# Разбираем URL-адрес на составляющие
result = urlparse(url)

# Выводим разобранный URL-адрес
print(result)

# Собираем URL-адрес обратно из элементов кортежа
reconstructed_url = urlunparse(result)

# Выводим полученный URL-адрес на печать
print(reconstructed_url)
