# 随机产生10个数字
#要求
#   每个数字取值范围[1,20]
#   统计重复的数字有几个？分别是什么
#    统计不重复的数字有几个，分别是什么？
import random

number = 10
lst = [random.randrange(1,20) for _ in range(20)]

print(lst)
repeat_lst = set()
no_repeat_lst = set()
for value in lst:
    if lst.count(value) > 1:
        repeat_lst.add(value)
    else:
        no_repeat_lst.add(value)

print("重复的数是:{},有{}个".format(str(repeat_lst), len(repeat_lst)))
print("不重复的数是:{},有{}个".format(str(no_repeat_lst), len(repeat_lst)))