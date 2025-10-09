def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
# Exemplo de uso
print(quick_sort([4, 2, 6, 3, 9]))

print(quick_sort([1,5,7,9,2,15,4]))