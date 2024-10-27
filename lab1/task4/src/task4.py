import tracemalloc
import time

def linear_search(arr, x):
    indices = []
    count = 0
    for i in range(len(arr)):
        if arr[i] == x:
            indices.append(i)
            count += 1

    if count == 0:
        return -1
    else:
        return count, indices

if __name__ == '__main__':
    tracemalloc.start()
    num = list(map(int, input().split()))
    target = int(input())
    if (len(num) < -10**3 or len(num) > 10**3) or not all([i >= -10**3 for i in num]) or target > 10**3:
        print('Ввод неверен. Введите еще раз!')
        num = list(map(int, input().split()))
    start = time.perf_counter()
    result = linear_search(num, target)
    count, indices = result
    if count == 1:
        print(indices)
    else:
        print(f'{count}, {' '.join(map(str,indices))}')
    stop = time.perf_counter()

    print(f'time: {stop-start:.15f} second')
    print('memory usage:', tracemalloc.get_traced_memory()[1], 'bytes')