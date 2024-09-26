def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1

        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key
    return list

arr = [1,42,3,5,4,567,23,78,5,45,65.6456]
print(insertion_sort(arr))