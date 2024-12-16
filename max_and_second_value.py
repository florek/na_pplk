import random
import timeit


def generate_random_list(size, start=0, end=100):
    return [random.randint(start, end) for _ in range(size)]


def largest_two(A):
    my_max, second = A[:2]
    if my_max < second:
        my_max, second = second, my_max
    for idx in range(2, len(A)):
        if my_max < A[idx]:
            my_max, second = A[idx], my_max
        elif second < A[idx]:
            second = A[idx]
    return my_max, second


def sorting_two(A):
    return tuple(sorted(A, reverse=True)[:2])


def double_two(A):
    my_max = max(A)
    copy = list(A)
    copy.remove(my_max)
    return my_max, max(copy)


def mutable_two(A):
    idx = max(range(len(A)), key=A.__getitem__)
    print(list(range(len(A))))
    my_max = A[idx]
    del A[idx]
    second = max(A)
    A.insert(idx, my_max)
    return my_max, second


random_list = generate_random_list(size=1000000, end=1000)
elapsed_time_ms = timeit.timeit(lambda: largest_two(random_list), number=1) * 1000
print(f"Czas wykonania largest_two: {elapsed_time_ms:.2f} ms")
elapsed_time_ms = timeit.timeit(lambda: sorting_two(random_list), number=1) * 1000
print(f"Czas wykonania sorting_two: {elapsed_time_ms:.2f} ms")
elapsed_time_ms = timeit.timeit(lambda: double_two(random_list), number=1) * 1000
print(f"Czas wykonania double_two: {elapsed_time_ms:.2f} ms")
elapsed_time_ms = timeit.timeit(lambda: mutable_two(random_list), number=1) * 1000
print(f"Czas wykonania mutable_two: {elapsed_time_ms:.2f} ms")
