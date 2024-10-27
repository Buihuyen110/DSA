import time
import tracemalloc

def bubble_sort(num):
     for i in range(len(num)-1):
         for j in range(len(num)-1, i, -1):
             if num[j] < num[j-1]:
                 num[j], num[j-1] = num[j-1], num[j]

     return num
if __name__ == '__main__':
    f1 = open('input.txt', 'r')
    f2 = open('output.txt', 'w')
    start = time.perf_counter()
    tracemalloc.start()

    n = int(f1.readline())
    arr = list(map(int, f1.readline().strip().split()))
    if (n < 1 or n > 10 ** 3) or not all([abs(i) <= 10 ** 9 for i in arr]):
        print('Ввод неверен')
    result = bubble_sort(arr)
    f2.write(' '.join(map(str, result)))
    stop = time.perf_counter()

    print("time:", stop - start)
    print('memory usage:', tracemalloc.get_traced_memory()[1], 'bytes')