# Поиск максимального подмассива за линейное время

import time
import tracemalloc

def find_max_subarray(arr):
    max_sum = float('-inf')
    current_sum = 0
    start_index = 0
    end_index = 0
    temp_start_index = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = temp_start_index
            end_index = i

        if current_sum < 0:
            current_sum = 0
            temp_start_index = i+1

    return start_index, end_index, max_sum

if __name__ == '__main__':
    f1 = open('input.txt', 'r')
    f2 = open('output.txt', 'w')

    start = time.perf_counter()
    n = int(f1.readline())
    num = list(map(int, f1.readline().strip().split()))
    if (n <= 1 or n >= 2 * (10 ** 4)) or not all([abs(i) <= 10 ** 9 for i in num]):
        print('Ввод неверен')
    start_i, end_i, max_sum = find_max_subarray(num)
    f2.write(' '. join(map(str, num[start_i:end_i + 1])))

    stop = time.perf_counter()
    print(f'time: {stop - start: .20f} s')
    print('memory usage:', tracemalloc.get_traced_memory()[1], 'bytes')
