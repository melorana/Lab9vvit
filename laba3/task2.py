def write_user_input():
    text = input("Ввести: ")
    with open("user_input.txt", "w") as file:
        file.write(text)
        print("Файл создан")
def append_text(filename, content):
    with open(filename, "a") as file:
        file.write("n/"+ content)
    return("Текст добавлен")
    
print("1 - создать текстовый файл, 2 - добавить текст в существующий файл")
s = input('Введите число:')
if s == "1":
    write_user_input()
elif s == "2":
    content = input("Введите текст: ")
    append_text("user_input.txt", content)
else:
    print("Ошибка!")