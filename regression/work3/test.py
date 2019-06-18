import random

def insertionSort(sequence):
    seq = sequence[:]
    for i in range(1, len(seq)):
        value = seq[i]
        j = i - 1
        while j >= 0 and seq[j] > value:
            seq[j+1] = seq[j]
            j -= 1
        seq[j+1] = value
    return seq

random.seed(520)
seq = [random.randint(1, 100) for _ in range(12)]
print(seq)
print(insertionSort(seq))
#[2, 8, 51, 52, 18, 58, 56, 98, 54, 27, 32, 50]
#[2, 8, 18, 27, 32, 50, 51, 52, 54, 56, 58, 98]
