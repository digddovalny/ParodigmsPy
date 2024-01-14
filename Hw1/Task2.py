def sort_list_declarative(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers


nums = [9, 5, 12, 56, 7, 2]
print(sort_list_declarative(nums))
