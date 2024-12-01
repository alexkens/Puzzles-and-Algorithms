def linear_search(sorted_list, target_number ,start=0):

    print(f"Commence linear search in the interval [{start} to {len(sorted_list)}]")

    for i in range(start, len(sorted_list)):
        if target_number == sorted_list[i]:
            print(f"{i - start} steps were taken")
            return 1
    return -1


def exponential_search_adjustable(sorted_list, target_number, basis=2, exponent=1, flag="exponent"):
    
    index = 0
    while index < len(sorted_list):

        print(f"Basis: {basis}, Index: {index}, current Number: {sorted_list[index]}")

        if sorted_list[index] == target_number:
            return 1
        elif sorted_list[index] < target_number:
            basis += 1
        else:
            # linear search if sorted_list[index] > target_number
            return linear_search(sorted_list, target_number, )

        # index operation
        index = basis ** exponent - 1 if index > 0 else basis ** exponent
        if index == 0: return -1



    return -1


def exponential_search_iterative(sorted_list, target_number):
    
    basis = 0
    exponent = 2
    index = 0
    
    while index < len(sorted_list):
        
        print(f"Basis: {basis}, Index: {index}, current Number: {sorted_list[index]}")

        if sorted_list[index] == target_number:
            return 1
        elif sorted_list[index] < target_number:
            basis += 1
        else:
            # linear search if sorted_list[index] > target_number
            return linear_search(sorted_list, target_number, )

        # index operation
        index = basis ** exponent - 1 if index > 0 else basis ** exponent
        if index == 0: return -1
    
    return linear_search(sorted_list, target_number, index - (basis**exponent - (basis-1)**exponent))


sorted_list = [i+1 for i in range(0)]
target_number = 0
print(sorted_list, " --> ", target_number)
result = exponential_search_iterative(sorted_list, target_number)
print(result)
