import pandas as pd

# Данные о мобильных телефонах
mobile_data = {
    "Производитель": ["Apple", "Samsung", "Google", "OnePlus", "Xiaomi", "Sony", "Huawei", "Nokia", "Motorola", "LG"],
    "Модель": ["iPhone 13", "Galaxy S21", "Pixel 6", "OnePlus 9", "Mi 11", "Xperia 5", "P50 Pro", "8.3 5G", "Moto G100", "Wing 5G"],
    "Диагональ экрана": [6.1, 6.2, 6.4, 6.55, 6.81, 6.1, 6.6, 6.81, 6.7, 6.8]
}

# Создание DataFrame
df = pd.DataFrame(mobile_data)

# Сохранение DataFrame в CSV файл с указанием кодировки UTF-8-SIG
csv_file_path = "mobile_phones.csv"
df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

# Чтение данных из CSV файла с указанием кодировки UTF-8-SIG
df = pd.read_csv(csv_file_path, encoding='utf-8-sig')

# Установка индекса
df.set_index("Модель", inplace=True)

# Вывод данных в виде таблицы
print(df)
