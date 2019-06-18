import string
import pdb
#pdb.set_trace()
original = (string.ascii_uppercase + string.ascii_lowercase + string.digits + "+" + "/").encode()



s = "abc"
s1 = "abcd"
s2 = "this is a example"


def base64(s):
    length = len(s)
    zore = 0
    ret = bytearray()

    for num in range(0, length, 3):
        if num +3 < length:
            triple = s[num:num + 3]
        else:
            triple = s[num:]
            zore = 3 - len(triple)
            triple += "\x00" * zore

        b  = int.from_bytes(triple.encode(), "big")
        
        for i in range(18, -1, -6):
            if i == 18:
                index = b >> i
            else:
                index = b >> i & 0x3F
            
            ret.append(original[index])
    
        for j in range(1, zore+1):
            ret[-j] = 0x3D        
    return ret


print(base64(s1))
 
            
