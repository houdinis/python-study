# 给定一个不超过5位的正整数，判断其有几位数，依次打印个位，十位，百位，千位，万位的数字

number = input("请输入一个不超过5位的正整数: ").strip()
digit = 0
if len(number) < 5:
    number = int(number)
    while number:
        result = number % 10
        number //= 10
        digit += 1
        print(result, end='')
    print("这是一个{}位数".format(digit))
else:
    print("不符合输入的条件!")
