def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array)//2]
    first = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    second = [x for x in array if x > pivot]
    return list(quickSort(first)) + [pivot] + list(quickSort(second))

print(quickSort([5,4,3,2,1]))