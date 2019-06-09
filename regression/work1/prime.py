# 给一个数，判断它是否是素数(质数)
    # 质数：一个大于1的自然只能被1和它本身整除


number = 5

def prime(number):
    for num in range(2, number):
        if not number % num:
            return False
    return True


print(prime(number))