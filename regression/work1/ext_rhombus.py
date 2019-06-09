


number = 7


def rhom(number):
    num = number // 2
    center = round(number / 2)
    for row in range(num, (-num-1), -1):
        if row > 0:
            print(" " * row + "*" * (center - row))
        if row == 0:
            print(" " * row + "*" * (number - row))
        if row < 0:
            print(" " * (center-1) + "*" * (center - (-row)) + " " * row)

rhom(number)
