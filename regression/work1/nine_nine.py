# 打印九九乘法表

# def nine_nine():
#     for row in range(1, 10):
#         for col in range(1, row+1):
#             print("{}*{}={}".format(col, row, col*row), end="\t")
#         print()
#
#
# nine_nine()



def nine_nine():
    for row in range(1, 10):
        print(" " * (7 * (row-1)), end="")
        for col in range(row, 10):
            if (col*row) >= 10:
                space = " "
            else:
                space = " " * 2
            print("{}*{}={}".format(row, col, col*row), end=space)
        print()

nine_nine()