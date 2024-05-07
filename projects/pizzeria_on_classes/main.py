import json
from abc import ABC, abstractmethod
from typing import List

class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

class CustomPizza(Pizza):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        return self.name

    def get_cost(self):
        return self.price

class Basket:
    def __init__(self):
        self.pizzas: List[Pizza] = []

    def add_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)

    def get_total_cost(self):
        return sum(pizza.get_cost() for pizza in self.pizzas)

    def show_cart(self):
        for pizza in self.pizzas:
            print(f"{pizza.get_description()} - {pizza.get_cost()}$")
        print(f"К оплате: {self.get_total_cost()}$")

class Order:
    def __init__(self, cart: Basket):
        self.cart = cart

    def place_order(self):
        print("Оплачено!")
        self.cart.show_cart()

    def pay(self, payment_method: str):
        if payment_method == "1":
            print("Оплатите при получении по адресу г. Полтава, ул. Котляревского, 13/28")
        elif payment_method == "2":
            card_number = input("Введите номер карты: ")
            input("Введите срок действия карты (ММ/ГГ): ")
            input("Введите CVV-код карты (XXX): ")
            print(f"Оплачено картой с номером {card_number}")
        else:
            print("Неверный способ оплаты.")

class Pizzeria:
    def __init__(self):
        self.cart = Basket()
        self.load_pizzas_from_json()

    def load_pizzas_from_json(self):
        with open('pizzas.json', 'r', encoding='utf-8') as file:
            pizzas_data = json.load(file)
            self.pizzas = [CustomPizza(**pizza) for pizza in pizzas_data]

    def add_to_cart(self, pizza: Pizza):
        self.cart.add_pizza(pizza)

    def show_cart(self):
        self.cart.show_cart()

    def place_order(self):
        order = Order(self.cart)
        order.place_order()
        return order

class UserInterface:
    def __init__(self):
        self.store = Pizzeria()

    def start(self):
        user = input("Введите ваше имя: ")
        print(f"Добрый день, {user}!")
        while True:
            print("\n1. Выбрать пиццу")
            print("2. Показать корзину")
            print("3. Оплатить")
            print("4. Выход")
            choice = input("Введите номер выбранного варианта: ")

            if choice == "1":
                self.add_pizza_to_cart()
            elif choice == "2":
                self.show_cart()
            elif choice == "3":
                self.place_order()
            elif choice == "4":
                break
            else:
                print("Неверный номер выбранного варианта.")

    def add_pizza_to_cart(self):
        for i, pizza in enumerate(self.store.pizzas, start=1):
            print(f"{i}. {pizza.get_description()} - {pizza.get_cost()}$")
        choice = input("Введите номер пиццы: ")
        try:
            pizza = self.store.pizzas[int(choice) - 1]
            self.store.add_to_cart(pizza)
        except (ValueError, IndexError):
            print("Неверный номер пиццы.")

    def show_cart(self):
        self.store.show_cart()

    def place_order(self):
        order = self.store.place_order()
        payment_method = input("Введите способ оплаты (1 - наличными, 2 - картой): ")
        order.pay(payment_method)

if __name__ == "__main__":
    ui = UserInterface()
    ui.start()
