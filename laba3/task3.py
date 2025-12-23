print("Выберите способ чтения файла: 1 - прочитать файл целиком, 2 - прочитать файл построчно")
n = input("Введите число:")
try:
    f = open('example2.txt')
except FileNotFoundError:
    print('Ошибка: Файл не найден.')
else:
    if n=="1":
        with open("example2.txt", "r") as file:
            content = file.read()
            print("Содержимое файла целиком:")
            print(content)
    elif n=="2":
        with open("example2.txt", "r") as file:
            print("Содержимое файла построчно:")
            for line in file:
                print(line)
    else:
        print("Неверно указанный тип чтения.")
