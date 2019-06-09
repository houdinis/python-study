

lst = [45, 3, 23, 2, 4, 2, 24, 23, 23, 21]

num = len(lst)
def run():
    for row in range(num-1):
        max_seq = 0
        min_seq = 0
        for col in range(1, num-row):
            if lst[max_seq] < lst[col]:
                max_seq = col
            if lst[min_seq] > lst[col]:
                min_seq = col

        if max_seq != col:
            lst[max_seq], lst[col] = lst[col], lst[max_seq]
        if min_seq != row:
            lst[min_seq], lst[row] = lst[row], lst[min_seq]

def run1():
    for row in range(num-1):
        max_seq = 0
        for col in range(1, num-row):
            if lst[max_seq] < lst[col]:
                max_seq = col

        if max_seq != col:
            lst[max_seq], lst[col] = lst[col], lst[max_seq]

from datetime import datetime
import time
def test_time(func):
    start_time = datetime.now()
    func()
    time.sleep(1)
    end_time = (datetime.now() - start_time).total_seconds()
    print(end_time)


test_time(run)
test_time(run1)


