def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    return numbers


nums = [9, 5, 12, 56, 7, 2]
print(sort_list_imperative(nums))
