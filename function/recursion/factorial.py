#递归实现阶乘
def recursion(n):
    if n == 1:
        return n
    return recursion(n-1)*n



print(recursion(5))