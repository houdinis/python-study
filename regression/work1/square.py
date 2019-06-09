# 打印一个边长为n的正方形

length_side = 5

def squ(length_side):
    for ls in range(length_side):
        if ls == 0 or ls == length_side-1:
            print('*  '*length_side)
        else:
            print('* '+'   '*(length_side-2)+' *')


squ(length_side)