# 求一数的阶乘

number = 5

def factorial(number):
    if number == 1:
        return 1
    else:
        return factorial(number-1) * number

print(factorial(number))