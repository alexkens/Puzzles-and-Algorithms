
def exponential_search(sorted_list, target_number):
    
    basis = 0
    exponent = 2
    index = 0
    
    while index < len(sorted_list):
        index = basis ** exponent

        print(basis, exponent, index)

        if sorted_list[index] == target_number:
            return 1
        elif sorted_list[index] < target_number:
            basis += 1
        else:
            # linear search
            for i in range(index, len(sorted_list)):
                if sorted_list[i] == target_number:
                   return 1
    return -1


sorted_list = [i+1 for i in range(11)]
target_number = 4
result = exponential_search(sorted_list, target_number)
print(result)
