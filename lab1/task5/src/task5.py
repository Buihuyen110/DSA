import tracemalloc
import time

def selection_sort(l, arr):
    for i  in range(l):
        min_index = i
        for j in range(i+1, l):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == '__main__':
    f1 = open('input.txt', 'r')
    f2 = open('output.txt', 'w')
    tracemalloc.start()
    start = time.perf_counter()

    n = int(f1.readline())
    num = list(map(int, f1.readline().strip().split()))
    if (n < 1 or n > 10 ** 3) or not all([abs(i) <=10 ** 9 for i in num]):
        print('Ввод неверен')

    arr_sorted = selection_sort(n, num)
    f2.write(' '.join(map(str, arr_sorted)))
    stop = time.perf_counter()
    print("time:", stop - start)
    print('memory usage:', tracemalloc.get_traced_memory()[1], 'bytes')
