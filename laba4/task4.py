from modules_process import null_opps, word_count, ost
print("Введите два числа:")
a = int(input())
b = int(input())
print("Разность: ", null_opps.null(a, b))

w = input("Введите текст: ")
print("Количество слов: ", word_count(w))

print("Введите два числа:")
a = int(input())
b = int(input())
print("Деление без остатка: ", ost(a, b))