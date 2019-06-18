
s1 = "abcdefg"
s2 = "defabcdoabcdeftw"



def character(s1, s2):
    length = len(s1)
    
    for sublen in range(length, 0, -1):
        for start in range(0, length - sublen + 1):
            substr = s1[start:start + sublen]
            
            if s2.find(substr) > -1:
                #print("The longest character is: {}".format(substr))
                return substr


print(character(s1, s2))
