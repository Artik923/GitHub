# Импортируем функцию urlparse из модуля urllib.parse
from urllib.parse import urlparse

# Задаем URL-адрес
url = 'https://www.foxbusiness.com/lifestyle/chemical-found-in-cheerios-quaker-oats-other-oat-based-foods-linked-potential-health-issues-study'

# Применяем функцию urlparse к URL-адресу
result = urlparse(url)

# Выводим результат
print(result)
