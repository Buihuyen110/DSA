# Бинарный поиск

import time
import tracemalloc

def binary_search(arr,x):
    left, right = 0, len(arr)
    while left <= right:
        mid = (left + right) // 2
        if mid < 0 or mid >= len(arr):
            return -1
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def count_indices(list1, list2):
    result = []
    for j in list2:
        index = binary_search(list1, j)
        result.append(index)
    return result

if __name__ == '__main__':
    f1 = open('input.txt', 'r')
    f2 = open('output.txt', 'w')
    start = time.perf_counter()

    n = int(f1.readline())
    a = list(map(int, f1.readline().strip().split()))
    m = int(f1.readline())
    b = list(map(int, f1.readline().strip().split()))
    if (n < 1 or n > 10**5) and (m < 1 or m > 10**5) or not all([abs(i) <= 10**9 for i in a]) or not all([abs(j) <= 10**9 for j in b]):
        print('Ввод неверен')

    result = count_indices(a, b)
    f2.write(' '.join(map(str, result)))
    stop = time.perf_counter()
    print(f'time: {stop-start: .20f} s')
    print('memory usage:', tracemalloc.get_traced_memory()[1], 'bytes')
