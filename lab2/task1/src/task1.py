# Сортировка слиянием

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        result.append(left.pop(0))
    result.extend(left)
    result.extend(right)
    return result

if __name__ == '__main__':
    f1 = open('input.txt', 'r')
    f2 = open('output.txt', 'w')

    n = int(f1.readline())
    num = list(map(int, f1.readline().strip().split()))
    if (n <= 1 or n >= 2 * (10 ** 4)) or not all([abs(i) <= 10 ** 9 for i in num]):
        print('Ввод неверен')

    f2.write(' '.join(map(str, merge_sort(num))))

