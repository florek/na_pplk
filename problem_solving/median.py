import math
import random
import time


def partition(A, lo, hi, idx):
    if lo == hi:
        return lo
    A[idx], A[lo] = A[lo], A[idx]
    i = lo
    j = hi + 1
    while True:
        while True:
            i += 1
            if i == hi:
                break
            if A[lo] < A[i]:
                break
        while True:
            j -= 1
            if j == lo:
                break
            if A[j] < A[lo]:
                break
        if i >= j:
            break
        A[i], A[j] = A[j], A[i]
    A[lo], A[j] = A[j], A[lo]
    return j


def linear_median(A):
    lo = 0
    hi = len(A) - 1
    mid = hi // 2
    while lo < hi:
        idx = random.randint(lo, hi)
        j = partition(A, lo, hi, idx)
        if j == mid:
            return A[j]
        if j < mid:
            lo = j + 1
        else:
            hi = j - 1
    return A[lo]


def my_median(A):
    sorted(A)
    center_value = int(math.ceil((len(A) - 1) / 2))
    return A[center_value]


numbers = [1, 7, 10, 12, 14, 15, 19, 22, 27, 33, 41, 100, 104]
start_time = time.time()
print(linear_median(numbers))
end_time = time.time()
print((end_time - start_time) * 1000)

start_time = time.time()
print(my_median(numbers))
end_time = time.time()
print((end_time - start_time) * 1000)