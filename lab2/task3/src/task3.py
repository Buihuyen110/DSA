# Числоинверсий

import time
import tracemalloc

def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid+1
    m = left
    count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[m] = arr[i]
            i += 1
        else:
            temp_arr[m] = arr[j]
            count += mid - i + 1
            j += 1
        m += 1

    while i <= mid:
        temp_arr[m] = arr[i]
        i += 1
        m += 1

    while j <= right:
        temp_arr[m] = arr[j]
        j += 1
        m += 1

    for i in range(left, right+1):
        arr[i] = temp_arr[i]

    return count

def merge_sort(arr, temp_arr, left, right):
    count = 0
    if left < right:
        mid = (left + right)//2

        count += merge_sort(arr, temp_arr, left, mid)
        count += merge_sort(arr, temp_arr, mid + 1, right)
        count += merge(arr, temp_arr, left, mid, right)

    return  count

def count_inversion(arr):
    temp_arr = [0]*len(arr)
    return merge_sort(arr, temp_arr, 0, len(arr)-1)

if __name__ == '__main__':
    f1 = open('input.txt', 'r')
    f2 = open('output.txt', 'w')

    start = time.perf_counter()
    n = int(f1.readline())
    num = list(map(int, f1.readline().strip().split()))
    if (n <= 1 or n >= 10 ** 5) or not all([abs(i) <= 10 ** 9 for i in num]):
        print('Ввод неверен')

    result = count_inversion(num)
    f2.write(str(result))
    stop = time.perf_counter()
    print("time:", stop - start)
    print('memory usage:', tracemalloc.get_traced_memory()[1], 'bytes')
