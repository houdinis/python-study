# 求100之内的斐波那契数列


number = 100


def fib(number):
    n0 = 0
    n1 = 1
    print(1)
    while True:
        n2 = n1 + n0
        n0 = n1
        n1 = n2
        if n2 > number: break
        print(n2)



fib(number)
