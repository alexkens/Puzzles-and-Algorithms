def linear_search(sorted_list, target_number ,start=0):

    print(f"Commence linear search in the interval [{start} to {len(sorted_list)}]")

    for i in range(start, len(sorted_list)):
        if target_number == sorted_list[i]:
            print(f"{i - start} steps were taken")
            return 1
    return -1


def sentinel_linear_search(sorted_list, target_number):
    sorted_list.append(target_number)
    print(f"Commence sentinel linear search with new list: {sorted_list}")
    i = 0
    while target_number != sorted_list[i]:
        i += 1
    if i < len(sorted_list) - 1:
        print(f"{i} steps were taken")
        return 1
    else:
        return -1


sorted_list = [i+1 for i in range(10)]
target_number = 44
print(sorted_list, " --> ", target_number)
result = sentinel_linear_search(sorted_list, target_number)
print(result)
