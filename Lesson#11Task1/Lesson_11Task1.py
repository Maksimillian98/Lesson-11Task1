﻿def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
A = int(input('Введите натуральное число: '))
print(factorial(A))