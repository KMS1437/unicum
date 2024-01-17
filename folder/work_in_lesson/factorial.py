from math import *
import time
def fact_math(n):
    return sqrt(2*pi*n) * (n / e)**n * (1 + 1 / sqrt(52*e*n))
num = int(input("Введите число: "))
print(f"Факториал Стирлинга: "
      f"{fact_math(num)}"
      f"\nФакториал: {factorial(num)}")
print(f'loss: {100 - (fact_math(num) * 100 / factorial(num))}')
start_time = time.time()
fact_math(num)
end_time = time.time()
total_time = end_time - start_time
print(f"Время формулы Стирлинга: {total_time} секунд")
start_time = time.time()
factorial(num)
end_time = time.time()
total_time = end_time - start_time
print(f"Время математического факториала: {total_time} секунд")
difference = fact_math(num) - factorial(num)
loss = abs(difference) * 100 / factorial(num)
print(f"Погрешность: {loss}%")
