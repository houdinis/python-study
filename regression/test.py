#
# from collections import OrderedDict
# import random
# d = {"banana":3,"apple":4,"pear":1,"orange":2}
# print(d)
# keys = list(d.keys())
# random.shuffle(keys)
# print(keys)
# od = OrderedDict()
# for key in keys:
#     od[key] = d[key]
# print(od)
# print(od.keys())
#
#
# d = {}
# number = input("请输入一个数字: ")
# for i in number:
#     d[i] = number.count(i)
# print(d)

from collections import OrderedDict
import random
d1 = OrderedDict()
l = [random.randrange(-1000, 1000) for _ in range(100)]
l.sort()
# for i in l:
#     d1[i] = l.count(i)
# print(d1)
print({i:l.count(i) for i in l})

# print(ord("a"), chr(97))
# s = "".join([chr(x) for x in range(ord("a"), ord("z")+1)])
# print(s)
# s1 = [random.choice(s)+random.choice(s) for _ in range(100)]
# s1.sort(reverse=True)
# print(s1)
# for i in s1:
#     d1[i] = s1.count(i)
#
# print(d1)


import math
