import linear_search


def exponential_search_adjustable(sorted_list, target_number, basis=2, exponent=1, flag="exponent"):
    """
    Function that performs expontial search on a list. Default is 2 as basis.
    Flag has two possible String inputs: 'exponent' and 'basis'. It decides what is increased durign search.
    """
    
    index = 0
    start = 0
    while index < len(sorted_list):

        print(f"Basis: {basis}, Exponent: {exponent}, Index: {index}, current Number: {sorted_list[index]}")

        if sorted_list[index] == target_number:
            return 1
        elif sorted_list[index] < target_number:
            if flag == "exponent":
                exponent += 1
            elif flag == "basis":
                basis += 1
            else:
                print("Invalid flag")
                return -1
        else:
            # linear search if sorted_list[index] > target_number
            if flag == "exponent":
                start = (index + 1) // basis
            elif flag == "basis":
                start = index ** basis - index ** (basis - 1)
            else:
                print("Invalid flag")
                return -1
            return linear_search(sorted_list, target_number, start)

        # index operation
        index = basis ** exponent - 1
        if index == 0: return -1

    if flag == "exponent":
        start = (index + 1) // basis
    elif flag == "basis":
        start = basis ** exponent - (basis - 1) ** exponent
    else:
        print("Invalid flag")
        return -1
    print(f"Basis: {basis}, Exponent: {exponent}, Index: {index}")
    return linear_search(sorted_list, target_number, start)


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


def checkup(list_length, func):
    list_length = 100
    for i in range(list_length + 1):
        sorted_list = [i+1 for i in range(i)]
        for target in range(1, i + 1):
            print(sorted_list, " --> ", target)
            assert func(sorted_list, target)
        

# checkup(100, exponential_search_adjustable)
# checkup(100, exponential_search_iterative)


sorted_list = [i+1 for i in range(100)]
target_number = 88
print(sorted_list, " --> ", target_number)
result = exponential_search_adjustable(sorted_list, target_number, exponent=3, flag="basis")
print(result)
