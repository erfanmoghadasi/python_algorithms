
def bubble_sort(array):
    n = len(array)
    for i in range(0, len(array)):
        flag = False
        for j in range(0, n - i - 1):
            if array[j] >= array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if not flag:
            break

array = [10, 9, 8, 7, 1, 2, 3, 4]
bubble_sort(array)
print(array)