# find pair sum in a sorted array

def my_first_solution(array: list[int], target: int):

    length = len(array)

    for first in range(length-1):
        for second in range(first+1, length):
            print(first, second)
            if array[first] + array[second] == target:
                return 1 
    return -1


array = [1, 3, 5, 10, 20, 21]
res = my_first_solution(array, 4)
print(res)
