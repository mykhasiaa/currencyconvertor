import easygui

while True:
    hrn = easygui.enterbox("Введіть суму у гривнях: ",
                           "Конвертер валют")
    if hrn is None:
        break

    else:
        try:
            hrn = float(hrn)
        except ValueError:
            easygui.msgbox("Напишіть число",
                           "Помилка",
                           "OK")

        currency = easygui.choicebox("Оберіть валюту",
                                      "Конвертер валют",
                                      ("Євро (EUR)", "Долар США (USD)"))
        if currency == None:
            break

        elif currency == "Євро (EUR)":
            result = hrn / 42.96
            message = f"{hrn} гривень = {result} євро"

        else:
            result = hrn / 41.47
            message = f"{hrn} гривень = {result} доларів"
        easygui.msgbox(message, "Результат")


        choice = easygui.buttonbox("Продовжити чи вийти?",
                                   "Конвертер валют",
                                   ("Продовжити", "Вийти"))
        if choice == "Вийти":
            easygui.msgbox("До побачення!",
                           "Конвертер валют")
            break