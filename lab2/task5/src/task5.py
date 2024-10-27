# Представитель большинства

import time
import tracemalloc

def majority_num(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2
    left_num = majority_num(arr, left, mid)
    right_num = majority_num(arr, mid + 1, right)
    if left_num == right_num:
        return left_num

    left_count = sum(1 for i in range(left, right + 1) if arr[i] == left_num)
    right_count = sum(1 for i in range(left, right + 1) if arr[i] == right_num)
    if left_count > (right - left + 1) // 2:
        return left_num
    return right_num

def find_majority_num(arr):
    n = len(arr)
    num = majority_num(arr, 0, n-1)
    count = sum(1 for x in arr if x == num)
    return 1 if count > n//2 else 0

if __name__ == '__main__':
    f1 = open('input.txt', 'r')
    f2 = open('output.txt', 'w')
    start = time.perf_counter()
    n = int(f1.readline())
    num = list(map(int, f1.readline().strip().split()))
    if (n < 1 or n > 10 ** 5) or not all([abs(i) <= 10 ** 9 for i in num]):
        print('Ввод неверен')

    f2.write(str(find_majority_num(num)))
    stop = time.perf_counter()
    print(f'time: {stop-start: .20f} s')
    print('memory usage:', tracemalloc.get_traced_memory()[1], 'bytes')