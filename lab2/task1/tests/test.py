import random
import time
import psutil

from lab2.task1.src.task1 import merge_sort


def generate_random_array(size):
    return [random.randint(-10**9, 10**9) for _ in range(size)]

def test_merge_sort(size):
    arr = generate_random_array(size)
    process = psutil.Process()
    start_time = time.time()
    mem_before = process.memory_info().rss / 1024**2
    sorted_arr = merge_sort(arr)
    end_time = time.time()
    mem_after = process.memory_info().rss / 1024**2
    print(f"Merge sort on array of size {size}: {end_time - start_time:.5f} seconds, memory usage: {mem_after - mem_before:.2f} MB")

def test_insertion_sort(size):
    arr = generate_random_array(size)
    process = psutil.Process()
    start_time = time.time()
    mem_before = process.memory_info().rss / 1024**2
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.time()
    mem_after = process.memory_info().rss / 1024**2
    print(f"Insertion sort on array of size {size}: {end_time - start_time:.5f} seconds, memory usage: {mem_after - mem_before:.2f} MB")

# Test merge sort
test_merge_sort(1000)
test_merge_sort(10000)
test_merge_sort(100000)

# Test insertion sort
test_insertion_sort(1000)
test_insertion_sort(10000)
test_insertion_sort(100000)

