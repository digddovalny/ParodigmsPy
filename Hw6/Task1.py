def binary_search(arr, value) -> int:
    result = -1
    first_index = 0
    last_index = len(arr) - 1
    while first_index <= last_index:
        middle_index = first_index + (last_index - first_index) // 2
        if arr[middle_index] == value:
            result = middle_index
            return print(result)
        elif middle_index < value:
            first_index = middle_index + 1
        else:
            last_index - 1
    return print(result)

# Считаем, что массив отсортирован
array = [1,2,3,4,5,6,7]
number = 4

binary_search(array, number)