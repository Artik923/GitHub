from file import File

files = [
    File(
        input('Введите имя файла: '),
        int(input('Введите размер файла: ')),
        input('Введите дату создания файла: ')
    )
    for _ in range(10)
]

for file in files:
    file.num_of_accesses = random.randint(0, 100)

access_threshold = int(input('Введите пороговое значение числа обращений: '))

files_with_high_access = [file for file in files if file.num_of_accesses > access_threshold]

for file in files_with_high_access:
    file.print_info()