# find pair sum in a sorted array

import random
import time


def trivial_solution(array: list[int], target: int):

    length = len(array)
    for first in range(length-1):
        for second in range(first+1, length):
            if array[first] + array[second] == target:
                return array[first], array[second]
    return -1, None


def two_pointers_technique(array: list[int], target: int):

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
        array = sorted(array)
        first, second = func(array, target)
        if second != None:
            print(f"{array} --> {target} --> {first}, {second}")
        else:
            print(f"{array} --> {target} --> No")
    print()


check(trivial_solution)
check(two_pointers_technique)

"""array = [1, 3, 5, 10, 20, 21]
res = two_pointers_technique(array, 21)
print(res)"""
