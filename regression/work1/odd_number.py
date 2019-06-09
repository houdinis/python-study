# 求100内所有奇数的和(2500)

number = 100

def odd(number):
    for num in range(1, number):
        if num % 2:
            print(num)

odd(number)
