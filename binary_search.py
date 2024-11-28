def binary_search_with_mid(sorted_list, number):
    # print(f"Sorted List: {sorted_list} --> Target number: {number}")

    while len(sorted_list) > 0:
        mid_index = int(len(sorted_list)//2)
        mid_number = sorted_list[mid_index]

        # print(sorted_list, mid_index, mid_number)

        if number == mid_number:
            return mid_number
        elif number < mid_number:
            sorted_list = sorted_list[:mid_index]
        else: # number > sorted_list[divide]
            sorted_list = sorted_list[mid_index+1:]

    return "Target number is not in the given List."


def binary_search_without_mid(sorted_list, number):
    # print(f"Sorted List: {sorted_list} --> Target number: {number}")

    divide = len(sorted_list)
    while len(sorted_list) > 1:
        
        divide = 1 if int(divide//2) == 0 else int(divide//2)

        if number < sorted_list[divide]:
            sorted_list = sorted_list[:divide]
        else: # number > sorted_list[divide]
            sorted_list = sorted_list[divide:]

    return sorted_list[0]


def check_with_output(number_of_range, func):

    for list_len in range(number_of_range+1):
        sorted_list = [i+1 for i in range(list_len)]
        print(f"Sorted List {sorted_list} --> Length: {list_len}")
        for target_number in range(1, list_len):
            result = func(sorted_list, target_number)
            assert target_number == result
            print(f"Target number: {target_number} --> Result: {result}")
        print()


def binary_search_indices(sorted_list, target_number):
    low = 0
    high = len(sorted_list) - 1
    mid = (high + 1 - low) // 2 + low

    while low <= high:
        mid = (high + 1 - low) // 2 + low

        if target_number == sorted_list[mid]:
            return sorted_list[mid]
        elif target_number < sorted_list[mid]:
            high = mid - 1
        else: # target_number > sorted_list[mid]
            low = mid + 1
    
    return sorted_list[mid]


"""sorted_list = [i+1 for i in range(10)]
print(sorted_list)
result = binary_search_indices(sorted_list, 6)
print(result)"""


# check_with_output(100, binary_search_without_mid)
# check_with_output(100, binary_search_with_mid)
check_with_output(100, binary_search_indices)
