"""
2 sum problem: find pair sum in an array
3 sum problem: find triple sum in an array
4 sum problem: find quadruple sum in an array

"""



import random
import time
import math


def two_sum_trivial(array: list[int], target: int):
    """The first pair sum is returned in an ascending lsit in O(N^2) complexity."""

    length = len(array)
    for first in range(length-1):
        for second in range(first+1, length):
            if array[first] + array[second] == target:
                return array[first], array[second]
    return -1, None


def two_sum_two_pointers_technique(array: list[int], target: int):
    """The first pair sum is returned in an ascending sorted list in O(N) complexity."""

    end = len(array) - 1
    for i in range(len(array)):
        if array[i] >= target:
            end = i
            break
    
    start = 0
    while start < end:
        current_sum = array[start] + array[end]
        if current_sum == target:
            return array[start], array[end]
        if current_sum < target:
            start += 1
            continue
        if current_sum > target:
            end -= 1
    
    return -1, None


def check(func):
    for i in range(10):
        seed_time = time.time() * 5372654932**i
        random.seed(seed_time)
        array = []
        target = random.randint(0, 100)
        for _ in range(10):
            array.append(random.randint(0, 100))
        first, second = func(array.sort(), target)
        if second != None:
            print(f"{array} --> {target} --> {first}, {second}")
        else:
            print(f"{array} --> {target} --> No")
    print()


def three_sum_trivial(array: list[int], target: int):

    n = len(array)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if target == array[i] + array[j] + array[k]:
                    return array[i], array[j], array[k]
    return -1


def three_sum(array: list[int], target: int):
    
    n = len(array)

    start = 0
    end = n - 1
    for i in range(n):
        if array[i] > target:
            end = i
    middle = int(end // 2)

    
    
    while start < middle and middle < end:
        print(start, middle, end)
        current_sum = array[start] + array[middle] + array[end]

        if current_sum == target:
            return start, middle, end
        elif current_sum < target:
            if middle == start + 1:
                start += 1
                middle = int((end - start) / 2 + start)
            middle -= 1
        else: # current_sum > target
            if middle == end - 1:
                end -= 1
                middle = int((end - start) / 2 + start)
            middle += 1
    
    return -1
            



array = [1, 3, 5, 10, 20, 21]
res = three_sum(array, 9)
print(res)


# check(two_sum_trivial)
# check(two_sum_two_pointers_technique)
