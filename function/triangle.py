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




#优化后

def show(n):

    tail = ' '.join([str(col) for col in range(n,0,-1)])
    size = len(tail)

    for col in range(1,n):
        print('{:>{}}'.format(' '.join([str(i) for i in range(col,0,-1)]),size))

    print(tail)


show(12)



def tangle(n):

    tail = ' '.join([str(i) for i in range(n,0,-1)])
    print(tail)

    for i in range(len(tail)):
        if tail[i] == ' ':
            print(' '*i,tail[i+1:])

tangle(12)
