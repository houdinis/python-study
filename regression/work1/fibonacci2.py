# 求斐波那契数列第101项


number = 101

def fib(number):
    n0 = 0
    n1 = 1
    flag = 1
    while flag <= number:
        n2 = n1 + n0
        n0 = n1
        n1 = n2
        flag += 1
    print(n2)


fib(number)

