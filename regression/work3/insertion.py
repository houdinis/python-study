# 插入排序
import random
lst = [random.randint(0,100) for _ in range(10)]
temp = 0
length = len(lst)
print(lst)

for row in range(1, length):
    temp = lst[row]
    j = row -1
    while j >= 0 and temp < lst[j]:
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = temp


print(lst)    
