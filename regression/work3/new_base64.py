

import string
import pdb
alphabet = (string.ascii_uppercase + string.ascii_lowercase + string.digits + '+' + '/').encode()


teststr = "ManMangv"
teststr1 = 'beyondc'

def base64(src):
    ret = bytearray()
    length = len(src)
    print(length)
    r = 0

    #将输入分成3个字节一组，不足3个字节的填充‘0’
    for offset in range(0, length, 3):
        if offset + 3 <= length:
            triple = src[offset:offset+3]
        else:
            triple = src[offset:]
            r = 3 - len(triple)
            print(hex(0))
            triple += hex(0) * r
        pdb.set_trace()
        print('+++++', triple, type(triple))
        b = int.from_bytes(triple.encode(), 'big')
        print(bin(b), hex(b), b)

        for i in range(18, -1, -6):
            if i == 18:
                index = b >> i
            else:
                index = b >> i & 0x3F

            ret.append(alphabet[index])

        for i in range(1, r+1):
            ret[-1] = 0x3D
    return ret


print(base64(teststr1))