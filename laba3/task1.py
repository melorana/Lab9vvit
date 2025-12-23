def get_file_lines_readlines(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line)
def read_file_content(filename):
    try:
        with open("example.txt", "r") as file:
            content = file.read()
        return(content)
    except FileNotFoundError:
        print('Ошибка: Файл не найден.')
print("Выберите способ чтения файла: 1 - прочитать файл целиком, 2 - прочитать файл построчно")
n = input("Введите число:")
if n=="1":
    file_content = read_file_content("example.txt")
    print(file_content)
elif n=="2":
    file_content = get_file_lines_readlines("example.txt")
    print(file_content)
else:
    print("Неверно указанный тип чтения.")
