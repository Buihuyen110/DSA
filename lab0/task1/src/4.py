import time
import sys
start = time.perf_counter()
f1 = open('D:\\Python\\CTDL&GT\\Lab0\\Task1\\input.txt', 'r')
f2 = open('D:\\Python\\CTDL&GT\\Lab0\\Task1\\output.txt', 'w')
a, b = map(int, f1.readline().split())
if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
    f2.write(str(a+b*b))
else:    print('Ввод неверен')
stop = time.perf_counter()
print("time:", stop - start)
memory_usage = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(a+b)
print('memory usage:', memory_usage, 'bytes')    