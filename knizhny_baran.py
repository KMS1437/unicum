class Baran:
    def __init__(self):
        self.menu = {
            "1": ('"Манифест Коммунистической Партии" Карл Маркс', 350),
            "2": ('"Двойной Латте на Кокосовом Ван Лав" Владимир Чижиков', 250),
            "3": ('"Mainkampf" Релтиг Флода', 1200),
            "4": ('"Учебник По алгебре" Министерство Образования', 1000),
            "5": ('"Пособие по ютубу" Гений Маркетинга', 70),
            "6": ('"Кастрация по Черному (Электрошокеру)" Александр Тайлаков', 20000),
            "7": ('"Подписывайтесь все на Александр Блог" Александр Антюфеев', 150),
            "8": ('"Моя жизнь" Лев Троцкий', 550),
            "9": ('"Вино из одуванчиков" Рэй Бредбери', 900),
            "10": ('"Дмиртий от АДА я" Дмитрий Никишин', 4000),
            "11": ('"Монах, который продал свою феррари" Робин Шарма', 400),
            "12": ('"Часодеи" Наталья Щерба', 600),
            "13": ('"Маленькие мужчины" Луиза Мэй Олкотт', 300),
            "14": ('"Чума" Альбер Камю', 300),
            "15": ('"Тошнота" Жан Поль Сартр', 300),
            "16": ('"Большие надежды" Чарлз Диккенс', 300),
            "17": ('"О Дивный Новый Мир" Олдос Хаксли', 300),
            "18": ('"Ведьмак" Анджей Сабковский', 300),
            "19": ('"Как Управлять Рабами" Марк Фалкс', 2200),
            "20": ('"Как играть в Доту" Тимофей', 666),
            "21": ('Пакет', 6)
        }
        self.order = {}

    def print_menu(self):
        print("Добро пожаловать в КнижныйБаран!")
        print("Ассортимент:")
        for item, (book, price) in self.menu.items():
            print(f"{item}. {book} - {price}₽")

    def take_order(self, item):
        if item in self.menu:
            if item in self.order:
                self.order[item] += 1
            else:
                self.order[item] = 1
        else:
            print("Неверный номер товара. Пожалуйста, попробуйте еще раз.")

    def remove_order(self, item_to_remove):
        if item_to_remove in self.order:
            self.order[item_to_remove] -= 1
            if self.order[item_to_remove] == 0:
                del self.order[item_to_remove]

    def checkout(self):
        payment_method = input("Введите способ оплаты (1 - наличными, 2 - картой): ")
        if payment_method == "1":
            card_number = input("Оплатите при получении по адресу г. Кемерово, ул. Московский, 39")
        elif payment_method == "2":
            while True:
                card_number = input("Введите номер карты: ")
                if len(card_number) == 16 and card_number.isdigit():
                    break
                else:
                    print("Неправильный номер карты. Пожалуйста, введите 16 цифр.")

            while True:
                card_date = input("Введите XX/XX: ")
                if len(card_date) == 4 and card_date.isdigit():
                    break
                else:
                    print("Ошибка. Пожалуйста, введите 4 цифры.")

            while True:
                card_three_number = input("Введите 3 циферки на задней части карты ***: ")
                if len(card_three_number) == 3 and card_three_number.isdigit():
                    break
                else:
                    print("Неправильный формат кода. Пожалуйста, введите 3 цифры.")
        else:
            print("Введите 1 или 2")

        total = 0
        for item, count in self.order.items():
            name, price = self.menu[item]
            print(f"{name} - {count} шт. за {price * count}₽")
            total += price * count
        print(f"Итого, вы набрали товаров на: {total}₽")
        print("Если возникли вопросы, обращайтесь по номеру 8 (800) 600-07-84")

    def run(self):
        self.print_menu()

        while True:
            item = input("Введите номер Книги, которую вы хотите купить (или 'Оплатить' для оплаты, 'Удалить' для удаления одного пункта): ")

            if item == "Оплатить":
                self.checkout()
                break
            elif item == "Удалить":
                item_to_remove = input("Введите номер книги, которую передумали брать: ")
                self.remove_order(item_to_remove)
            else:
                self.take_order(item)

baran = Baran()
baran.run()
