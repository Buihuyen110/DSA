import time
import sys
start = time.perf_counter()
n = 0
a1 = open('D:\\Python\\CTDL&GT\\Lab0\\Task3\\input.txt', 'r')
a2 = open('D:\\Python\\CTDL&GT\\Lab0\\Task3\\output.txt', 'w')
n = int(a1.read())
if n<0 or n>10**7:
    print("Неправильный формат данных.")
elif n==0:
    f1=f0=0
else:
    f0, f1 = 0, 1
    for _ in range(2, n+1):
        f0, f1 = f1, (f0 + f1)
a2.write(str(f1 % 10))
stop = time.perf_counter()
print("time:", stop - start)
memory_usage = sys.getsizeof(n) + sys.getsizeof(f0) + sys.getsizeof(f1)
print('memory usage:', memory_usage, 'bytes')