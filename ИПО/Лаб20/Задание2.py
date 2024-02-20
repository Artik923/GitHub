# Импортируем функцию urlparse из модуля urllib.parse
from urllib.parse import urlparse

# Задаем URL-адрес, который нужно разобрать
url = 'https://www.foxbusiness.com/lifestyle/chemical-found-in-cheerios-quaker-oats-other-oat-based-foods-linked-potential-health-issues-study'

# Разбираем URL-адрес на составляющие
result = urlparse(url)

# Извлекаем протокол из разобранного URL-адреса
protocol = result.scheme

# Выводим протокол на печать
print(f"Протокол: {protocol}")
