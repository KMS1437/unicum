# 1
def update_odd_numbers():
    global numbers_list
    
    numbers_list = input("Введите ваш список чисел: ").split()

    numbers_list = [int(num) for num in numbers_list]

    odd_sum = 0
    total_sum = 0
    for i, num in enumerate(numbers_list):
        total_sum += num
        if num % 2 != 0:
            odd_sum += num
            numbers_list[i] = odd_sum

    numbers_list = [total_sum]

    print("Список после всех манипуляций: ", numbers_list)

update_odd_numbers()



# 2
def length_of_segment(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def perimeter_of_triangle(x1, y1, x2, y2, x3, y3):
    side1 = length_of_segment(x1, y1, x2, y2)
    side2 = length_of_segment(x2, y2, x3, y3)
    side3 = length_of_segment(x3, y3, x1, y1)
    return side1 + side2 + side3

x1 = float(input("Введите x-координату первого конца отрезка: "))
y1 = float(input("Введите y-координату первого конца отрезка: "))
x2 = float(input("Введите x-координату второго конца отрезка: "))
y2 = float(input("Введите y-координату второго конца отрезка: "))

segment_length = length_of_segment(x1, y1, x2, y2)
print("Длина отрезка:", segment_length)

x3 = float(input("Введите x-координату первой вершины треугольника: "))
y3 = float(input("Введите y-координату первой вершины треугольника: "))
x4 = float(input("Введите x-координату второй вершины треугольника: "))
y4 = float(input("Введите y-координату второй вершины треугольника: "))
x5 = float(input("Введите x-координату третьей вершины треугольника: "))
y5 = float(input("Введите y-координату третьей вершины треугольника: "))

triangle_perimeter = perimeter_of_triangle(x3, y3, x4, y4, x5, y5)
print("Периметр треугольника:", triangle_perimeter)



# 3
def is_power_of_two(n):
    if n == 1:
        return True
    elif n % 2 == 0:
        return is_power_of_two(n // 2)
    else:
        return False

N = int(input("Введите натуральное число N: "))

if is_power_of_two(N):
    print("YES")
else:
    print("NO")
