def kfc():
    print("Добро пожаловать в KFC!")
    print("Меню:")
    print("1. Шефбургер - 150₴")
    print("2. Двойной Латте на Кокосовом - 100₴")
    print("3. Шефбургер Джуниор - 50₴")
    print("4. Чизбургер - 45₴")
    print("5. Влажная Салфетка - 2₴")

    menu = {
        "1": ("Шефбургер", 150),
        "2": ("Двойной Латте на Кокосовом", 100),
        "3": ("Шефбургер Джуниор", 50),
        "4": ("Чизбургер", 45),
        "5": ("Влажная Салфетка", 2)
    }

    order = {}

    while True:
        item = input("Введите номер американ блюда, которое вы хотите заказать (или 'Оплатить' для оплаты, 'Удалить' для удаления одного пункта): ")

        if item == "Оплатить":
            payment_method = input("Введите способ оплаты (1 - наличными, 2 - картой): ")
            if payment_method == "1":
                card_number = input("Оплатите при получении по адресу г. Полтава, ул. Котляревского, 13/28")
            if payment_method == "2":
                card_number = input("Введите номер карты: ")

            total = 0
            for item, count in order.items():
                name, price = menu[item]
                print(f"{name} - {count} шт. за {price * count}₴")
                total += price * count
            print(f"Итого, вы набрали американ продуктов на: {total}₴")
            print("Если возникли вопросы, обращайтесь по номеру +380 (67) 672-47-42")
            break
        elif item == "Удалить":
            item_to_remove = input("Введите номер американ блюда, которое передумали брать во славу Руси: ")
            if item_to_remove in order:
                order[item_to_remove] -= 1
                if order[item_to_remove] == 0:
                    del order[item_to_remove]
        elif item in menu:
            if item in order:
                order[item] += 1
            else:
                order[item] = 1
        else:
            print("Неверный номер блюда. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    kfc()
