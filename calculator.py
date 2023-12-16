class Calculator:
    def __init__(self):
        pass

    def square_area(self, side):
        return side ** 2

    def rectangle_area(self, length, width):
        return length * width

    def triangle_area(self, base, height):
        return (base * height) / 2

    def circle_area(self, radius):
        return 3.14159 * (radius ** 2)

    def castration(self):
        animal = input("Введите животное для кастрации: ")
        if animal == "Собака":
            return "Ну всё.."
        elif animal == "Поварич":
            return "ОМАГАД."
        elif animal == "Кошка":
            return "А кота то зачем?)"
        else:
            return "Не нашли такого животного."

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            return "Ошибка! Деление на ноль"
        return num1 / num2


calc = Calculator()
print("Выберите операцию:")
print("1. Площадь квадрата")
print("2. Площадь прямоугольника")
print("3. Площадь треугольника")
print("4. Площадь окружности")
print("5. Кастрация")
print("6. Сложение")
print("7. Вычитание")
print("8. Умножение")
print("9. Деление")

choice = int(input("Введите номер операции: "))

if choice == 1:
    side = int(input("Введите длину стороны квадрата: "))
    print("Площадь квадрата:", calc.square_area(side))
elif choice == 2:
    length = int(input("Введите длину прямоугольника: "))
    width = int(input("Введите ширину прямоугольника: "))
    print("Площадь прямоугольника:", calc.rectangle_area(length, width))
elif choice == 3:
    base = int(input("Введите длину основания треугольника: "))
    height = int(input("Введите высоту треугольника: "))
    print("Площадь треугольника:", calc.triangle_area(base, height))
elif choice == 4:
    radius = int(input("Введите радиус окружности: "))
    print("Площадь окружности:", calc.circle_area(radius))
elif choice == 5:
    print(calc.castration())
elif choice == 6:
    num1 = int(input("Введите первое число для сложения: "))
    num2 = int(input("Введите второе число для сложения: "))
    print("Результат сложения:", calc.addition(num1, num2))
elif choice == 7:
    num1 = int(input("Введите первое число для вычитания: "))
    num2 = int(input("Введите второе число для вычитания: "))
    print("Результат вычитания:", calc.subtraction(num1, num2))
elif choice == 8:
    num1 = int(input("Введите первое число для умножения: "))
    num2 = int(input("Введите второе число для умножения: "))
    print("Результат умножения:", calc.multiplication(num1, num2))
elif choice == 9:
    num1 = int(input("Введите число для деления: "))
    num2 = int(input("Введите делитель: "))
    result = calc.division(num1, num2)
    if isinstance(result, str):
        print(result)
    else:
        print("Результат деления:", result)
else:
    print("Некорректный выбор операции")
