def max_of_two(x,y):
    if x>y:
        return x
    elif x<y:
        return y
    elif x==y:
        print("Числа одинаковы")
x = int(input())
y = int(input())
number = max_of_two(x,y)
print(number)