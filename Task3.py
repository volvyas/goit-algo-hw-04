import functools
import random

from datetime import datetime

def bench_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        delta = datetime.now() - start
        print(f"Time passed for {func.__name__}: {delta}")
        return result
    return wrapper

@bench_decorator
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

@bench_decorator
def merge_sort(arr):
    merge_sort_func(arr)

def merge_sort_func(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort_func(left_half), merge_sort_func(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

@bench_decorator
def tim_sort(lst):
    return sorted(lst)


arr_100 = random.sample(range(0, 100), 100)
arr_1000 = random.sample(range(0, 1000), 1000)
arr_100000 = random.sample(range(0, 100000), 100000)


merge_sort(arr_100)
insertion_sort(arr_100)
tim_sort(arr_100)

merge_sort(arr_1000)
insertion_sort(arr_1000)
tim_sort(arr_1000)

merge_sort(arr_100000)
insertion_sort(arr_100000)
tim_sort(arr_100000)
