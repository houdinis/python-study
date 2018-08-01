#编写一个函数,能够接受至少2个参数，返回最小值和最大值

def size(*args):
    min = 9999999999999
    max = 0
    if len(args) == 2:
        if args[0] < args[1]:
            max = args[1]
            min = args[0]
        else:
            max = args[0]
            min = args[1]
    else:
        for i in args:
            if max < i:
                max = i
            if min > i:
                min = i

    return max,min


#优化后

import random

def double_values(*nums):
    print(nums)
    return max(nums),min(nums)



print(*double_values(*[random.randint(10,20) for _ in range(10)]))