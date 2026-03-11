i = input("введите ваш возраст: ")

if i.lstrip("-").isdigit():
    age = int(i)
    if age < 0:
        print("возраст не может быть отрицательным!!!!")
    else:
        if age >= 18:
            print("вы совершеннолетний...")
        else:
            print("вы несовершеннолетний!!!")
else:
    print("введено не число!")
