#编写一个函数，接受一个参数n,n为正整数,左右两种打印方式，要求数字必须对齐

def triangle(n):

    for row in range(1,n+1):
        print((n-row)*'   ',end='')
        for col in range(row,0,-1):
            print(' {:>2}'.format(col),end='')
        print('\n')

    print('-----------------------------------------')
    for row in range(n,0,-1):
        print((n-row)*'   ',end='')
        for col in range(row,0,-1):
            print(' {:>2}'.format(col),end='')
        print('\n')

triangle(12)
