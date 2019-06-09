# 依次接收用户输入的3个数，排序后打印
# 1.转换int后,判断大小排序
# 2。使用MAX函数
# 3。作用列表的sort方法
# 冒泡法


# 1.
# a = int(input("请输入a的值:").strip())
# b = int(input("请输入b的值:").strip())
# c = int(input("请输入c的值:").strip())
# tmp = 0
# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b
#
# print(a, b, c)

# 3.
# a = int(input("请输入a的值:").strip())
# b = int(input("请输入b的值:").strip())
# c = int(input("请输入c的值:").strip())
# lst = [a, b ,c]
# lst.sort()
# print(lst)

# 4
lst = []
for i in range(9):
    lst.append(int(input("请输入第{}个数: ".format(i+1))))


for outer in range(len(lst)-1):
    flag = False
    for iner in range(len(lst)-1-outer):
        if lst[iner] > lst[iner+1]:
            lst[iner], lst[iner+1] = lst[iner+1], lst[iner]
            flag = True
    if not flag:
        break

print(lst)
