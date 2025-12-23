num = int(input("Введите первое число: "))
s = int(input("Введите второе число: "))
if num > s:
    print("Большее число:", num)
elif s > num:
    print("Большее число:", s )
elif num==s:
    print("Числа одинаковы")