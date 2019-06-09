# 打印一个杨辉三角形
# 求第M行第K个元素
ROWS = 11
M = 4
K = 3

def triangle(row, r, c):
    lst = [[1]]
    for line in range(1, row):
        lst.append([0]*(line+1))
        for columns in range(line+1):
            if line == columns or columns == 0:
                lst[line][columns] = 1
            else:
                lst[line][columns] = lst[line-1][columns-1] + lst[line-1][columns]
                if line == r and columns == c:
                    number = lst[line][columns]
    return lst, number



lst, number= triangle(ROWS, M, K)
print(lst)
print(number)
row = 11
for line in range(0, row):
    space = row - line
    print(" " * space, end="")
    for col in range(line+1):
        print("{:}".format(lst[line][col]), end=" ")
    print()


