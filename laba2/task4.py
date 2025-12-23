def describe_person(name, age=30):
    # return("Имя: ", name , ", возраст: " , age)
    return(f"Имя {name} возраст {age}")
name = input()
age = input()
if age:
    print(describe_person(name, age))
else:
    print(describe_person(name))
