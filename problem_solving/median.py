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
    A = sorted(A)
    center_value = int(math.ceil((len(A) - 1) / 2))
    return A[center_value]


def my_median2(A):
    lower_numbers_must_have = int(math.floor(len(A) / 2)) + 1
    lower_numbers = A[0:lower_numbers_must_have]
    for elem in A[lower_numbers_must_have:]:
        max_number = max(lower_numbers)
        max_number_idx = lower_numbers.index(max_number)
        if max_number > elem:
            lower_numbers[max_number_idx] = elem
    return max(lower_numbers)


numbers = [10, 8, 7, 2, 1, 3, 4]
start_time = time.time()
print(linear_median(numbers))
end_time = time.time()
print((end_time - start_time) * 1000)

start_time = time.time()
print(my_median(numbers))
end_time = time.time()
print((end_time - start_time) * 1000)

start_time = time.time()
print(my_median2(numbers))
end_time = time.time()
print((end_time - start_time) * 1000)
