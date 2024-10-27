import tracemalloc
import time

def insertion_sort(num):
    for i in range(1,n):
        elem = num[i]
        j = i-1

        while j >= 0 and num[j] > elem:
            num[j+1] = num[j]
            j -= 1
        num[j+1] = elem
    return num

if __name__ == '__main__':
    f1 = open('input.txt', 'r')
    f2 = open('output.txt', 'w')

    tracemalloc.start()
    start = time.perf_counter()

    n = int(f1.readline())
    arr = list(map(int, f1.readline().strip().split()))
    if (n < 1 or n > 10 ** 3) or not all([abs(i) <= 10 ** 9 for i in arr]):
        print('Ввод неверен')

    result = insertion_sort(arr)
    f2.write(' '.join(map(str,result)))
    stop = time.perf_counter()

    print("time:", stop - start)
    print('memory usage:', tracemalloc.get_traced_memory()[1], 'bytes')

