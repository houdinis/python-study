#编写一个函数，接受一个参数n,n为正整数，左右两种打印方式。要求数字必须对齐



number = 12
def triangle(num):
    for row in range(12):
        print('{:{}d}'.format(' ' * (num-row)), end='')
        for col in range(row+1, 0, -1):
            print(col, end=' ')
        print()

triangle(number)