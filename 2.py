i = input("Введите число: ")

if i.isdigit():
    number = int(i)
    if number % 2 == 0:
        print(f"число {number} - четное")
    else:
        print(f"число {number} - нечетное..")
else:
    print("ошибка: это не число...")
