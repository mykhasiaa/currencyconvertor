print("Вітаємо!")

while True:
    while True:
        try:
            hrn = float(input("Введіть суму у гривнях:\n"))
            print("\n")
            break
        except ValueError:
            print("Напишіть число.\n")

    print("Валюти для конвертації:")
    print("1. Євро (EUR)")
    print("2. Долар США (USD)")

    while True:
        choice = input("Оберіть валюту для конвертації (1/2): ")
        print("\n")

        if choice == '1':
            result = hrn / 42.96
            print(f"{hrn} гривень = {result} євро\n")
            break


        elif choice == '2':
            result = hrn / 41.47
            print(f"{hrn} гривень = {result} доларів\n")
            break


        else:
            continue

    print("Ви хочете продовжити чи вийти?")
    print("1. Продовжити")
    print("2. Вийти")

    while True:
        exitchoice = input("Оберіть варіант (1/2): ")

        if exitchoice == '1':
            print("\n")
            break

        elif exitchoice == '2':
            print("До побачення!")
            break

        else:
            print("Введіть 1 або 2\n")
    if exitchoice == '2':
        break