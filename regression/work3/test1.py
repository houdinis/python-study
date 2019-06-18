import random
lst = [random.randint(0, 100) for _ in range(10)]
print(lst)
tmp = 0
length = len(lst)


for row in range(1, length):
    tmp = lst[row]
    j  = row - 1
    while j >= 0 and tmp < lst[j]:
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = tmp

print(lst)
