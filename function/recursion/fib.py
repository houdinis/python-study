
#递归实现斐波那数列

def fib(n):
    #return 1 if n < 2 else fib(n-1) + fib(n-2)
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(5):
    print(fib(i),end=' ')