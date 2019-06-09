import string

ascii_list = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+' + '/'
base64_dict = {key:value for key,value in enumerate(ascii_list)}
print(base64_dict)
s = "beyond"
s1 = 'Man'
s2 = "this is a example"
s3 = 'a'
print("Before coding: {}".format(s3))

def encode_base64(chars):
    # 将每个字符转换成二进制
    lst = []
    c = ""
    for s in chars:
        # ['0b1100010', '0b1100101', '0b1111001', '0b1101111', '0b1101110', '0b1100100']
        lst.append(bin(ord(s)).replace('0b', '0'))
    result = ''.join(lst)
    # 将二进制分为6位一组，不足6位的填0
    lst = []
    print(result)
    for item in range(0, len(result), 6):
        lst.append(result[item:item+6])
        if len(lst[-1]) != 6:
            lst[-1] += (6 - len(lst[-1])) * '0'
        
    # 将二进制转换成索引
    lst = [int(i,2) for i in lst]
    lst = "".join(base64_dict[i] for i in lst)
    print("After encoding: {}".format(lst))


encode_base64(s3)

