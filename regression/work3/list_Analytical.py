# "0001.abadicddws" 是ID格式，要求ID格式是以点号分割，
# 左边是4位从1开始的整数，右边是10位随机小写英文字母。
# 请依次生成前100个ID的列表
import random
import string
print(["{:0>4}.{}".format(i,''.join(random.choice(string.ascii_lowercase) for j in range(10)))  for i in range(1, 100)])