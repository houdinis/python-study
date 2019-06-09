# 给定一个3*3方阵，求其转置矩阵

#    123          147
#    456   ==>    258
#    789          369


number = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def matrix(number):
    for rows in range(3):
        for cols in range(3):
            if rows == 0 or cols == 2:
                number[rows][cols], number[cols][rows] = number[cols][rows], number[rows][cols]

matrix(number)
print(number)