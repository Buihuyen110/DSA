import tracemalloc
import time

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        elem = arr[i]
        j = i-1

        while j >= 0 and arr[j] > elem:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = elem
    return arr

def reverse_arr(arr):
    n = len(arr)
    for i in range(n//2):
        swap(arr, i, n-i-1)

if __name__ == '__main__':
    f1 = open('input.txt', 'r')
    f2 = open('output.txt', 'w')

    tracemalloc.start()
    start = time.perf_counter()

    n = int(f1.readline())
    num = list(map(int, f1.readline().strip().split()))
    if (n < 1 or n > 10 ** 3) or not all([abs(i) <= 10 ** 9 for i in num]):
        print('Ввод неверен')

    insertion_sort(num)
    reverse_arr(num)
    f2.write(' '.join(map(str, num)))
    stop = time.perf_counter()

    print("time:", stop - start)
    print('memory usage:', tracemalloc.get_traced_memory()[1], 'bytes')


