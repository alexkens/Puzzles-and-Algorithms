def binary_search_with_mid(sorted_list, number):
    pass


def binary_search_without_mid(sorted_list, number):
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
        print(sorted_list, "-->", list_len)
        for target_number in range(1, list_len):
            result = func(sorted_list, target_number)
            assert target_number == result
            print(f"target: {target_number} --> result: {result}")
        print()

"""
sorted_list = [i+1 for i in range(10)]
result = binary_search(sorted_list, 11)
print(result)
"""

check_with_output(100, binary_search_without_mid)
