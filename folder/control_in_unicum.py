# 1 задача

import random

list_length = int(input("Введите длину списков:"))

list1 = [random.randint(1, 10) for i in range(list_length)]
list2 = [random.randint(1, 10) for i in range(list_length)]

print("Список 1:", list1)
print("Список 2:", list2)

sorted_list = sorted(list1 + list2)

print("Отсортированный список:", sorted_list)

unique_elements = set(list1).intersection(set(list2))

print("Уникальные числа:", list(unique_elements))

max_value = max(list1 + list2)
min_value = min(list1 + list2)

print("Минимальное значение числа:", min_value)
print("Максимальное значение числа:", max_value)


# 2 задача

sales1 = float(input("Введите уровень продаж для Первого Мена:"))
sales2 = float(input("Введите уровень продаж для Второго Мена:"))
sales3 = float(input("Введите уровень продаж для Третьего Мена:"))

num_1 = 200 + min(sales1, 500) * 0.03 + max(min(sales1, 1000) - 500, 0) * 0.05 + max(sales1 - 1000, 0) * 0.08
num_2 = 200 + min(sales2, 500) * 0.03 + max(min(sales2, 1000) - 500, 0) * 0.05 + max(sales2 - 1000, 0) * 0.08
num_3 = 200 + min(sales3, 500) * 0.03 + max(min(sales3, 1000) - 500, 0) * 0.05 + max(sales3 - 1000, 0) * 0.08

thebetter_manager = max(num_1, num_2, num_3)

if thebetter_manager == num_1:
    print("Зарплата Первого:", num_1 + 200, " (премиалист)")
else:
    print("Зарплата Первого:", num_1)
if thebetter_manager == num_2:
    print("Зарплата Второго:", num_2 + 200, " (премиалист)")
else:
    print("Зарплата Второго:", num_2)
if thebetter_manager == num_3:
    print("Зарплата Третьего:", num_3 + 200, " (премиалист)")
else:
    print("Зарплата Третьего:", num_3)


# 3 задача

phone_brands = ('Orange', 'Siaoni', 'Sinsumg', 'Hiavei')

def print_menu():
    print("1. Добавить новый бренд")
    print("2. Удалить бренд")
    print("3. Показать список брендов")
    print("4. Выход из программы")

def add_brand(brand, brands):
    if brand in brands:
        print("Бренд уже существует!")
    else:
        brands += (brand,)
        print("Теперь ваш новый бренд существует!")
    return brands

def remove_brand(brand, brands):
    if brand not in brands:
        print("Бренд не найден! Попробуй ещё раз")
    else:
        brands = tuple(x for x in brands if x != brand)
        print("Бренд удален! Можно отпразновать!")
    return brands

print("Список брендов:", phone_brands)

while True:
    print_menu()
    choice = input("Выберите действие (введите цифру действия):")

    if choice == '1':
        brand = input("Введите название бренда: ")
        phone_brands = add_brand(brand, phone_brands)
        print("Список брендов:", phone_brands)
    elif choice == '2':
        brand = input("Введите название бренда: ")
        phone_brands = remove_brand(brand, phone_brands)
        print("Список брендов:", phone_brands)
    elif choice == '3':
        print("Список брендов:", phone_brands)
    elif choice == '4':
        break
    else:
        print("Неправильно! Попробуй, ещё раз!")


# 4 задание

countries = set(['Россия', 'США', 'Беларусь', 'Египет', 'Таджикистан'])

while True:

    print('1. Посмотреть список стран')
    print('2. Добавить свою страну')
    print('3. Удалить страну')
    print('4. Найти страну')

    choice = input('Введите номер действия: ')

    if choice == '1':
        print(countries)

    elif choice == '2':
        your_country = input('Введите свою страну: ')
        countries.add(your_country)
        print(f'Страна {your_country} добавлена в множество.')

    elif choice == '3':
        del_country = input('Введите название страны, которую нужно удалить: ')
        if del_country in countries:
            countries.remove(del_country)
            print(f'Страна {del_country} удалена')
        else:
            print(f'Страны {del_country} нет в программе')

    elif choice == '4':
        find_country = input('Введите название страны для поиска: ')
        if find_country in countries:
            print(f'Страна {find_country} найдена')
        else:
            print(f'Страна {find_country} не найдена')

    else:
        print('Неправильно ввёл. Переделывай')


# 5 задание

dictionary = {'Муджахед': 1871, 'Игорёк Бобылев': 2010, 'Мишань Камозин': 2009}

while True:
    print('Что вы хотите сделать?')
    print('1 - Добавить новый элемент в словарь')
    print('2 - Удалить элемент из словаря')
    print('3 - Изменить элемент в словаре')
    print('4 - Вывести текущий словарь')
    print('5 - Выйти из программы')

    choice = input()

    if choice == '1':
        name = input('Введите свой имя: ')
        year_of_birth = input('Введите свой год рождения: ')

        try:
            year_of_birth = int(year_of_birth)
            dictionary[name] = year_of_birth
            print('Элемент добавлен в словарь.')
        except ValueError:
            print('Ошибка! Год рождения должен быть числом.')

    elif choice == '2':
        name = input('Введите имя: ')

        if name in dictionary:
            del dictionary[name]
            print('Элемент удалён из словаря.')
        else:
            print('Ошибка! Элемент с таким именем не найден.')

    elif choice == '3':
        name = input('Введите имя: ')

        if name in dictionary:
            year_of_birth = input("Введите новый год рождения:")

            try:
                year_of_birth = int(year_of_birth)
                dictionary[name] = year_of_birth
                print("Элемент изменён в словаре.")
            except ValueError:
                print("Ошибка! Год рождения должен быть числом.")
        else:
            print("Ошибка! Элемент с таким именем не найден.")

    elif choice == '4':
        print(dictionary)

    elif choice == '5':
        break

    else:
        print("Неправильно! Попробуй ещё раз!")


# 6 задача

import random

lst = list(range(int(input("Enter the range: "))))
for i in range(len(lst)):
    lst.insert(random.randint(0, 9), lst.pop(i))

print(lst)
