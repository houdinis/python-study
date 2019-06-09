# 求10万内的所有素数

number = 100000

def prime(number):
    for num in range(2, number):
        for ran in range(2, num):
            if not num % ran:
                break
        else:
            print(num)

prime(number)



