#递归实现猴子偷桃问题

def monkey(day=10,x=1):
    if day == 1:
        return x
    return monkey(day-1,(x*2)+1)


print(monkey(10))
