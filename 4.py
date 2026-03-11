while True:
    i = input("Введите число: → ")

    if i == "exit":
        print("Выход из программы...")
        break

    if i.lstrip("-").isdigit():
        digits_part = i.lstrip("-")
        length = len(digits_part)
        print(f"кстати в этом числе {length} цифр.")
    else:
        print("данные не являются числом.")
