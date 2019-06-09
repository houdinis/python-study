# 打印下面的菱形


#          *
#         ***
#        *****
#       *******
#        *****
#         ***
#          *
#

number = 7


def rhom(number):
    num = number // 2
    for row in range(num, (-num-1), -1):
        star = row if row >= 0 else -row
        print(" " * star + "*" * (number - 2 * star) + " " * star)
rhom(number)
