# find pair sum in a sorted array

import random
import time


def my_first_solution(array: list[int], target: int):

    length = len(array)
    for first in range(length-1):
        for second in range(first+1, length):
            if array[first] + array[second] == target:
                return array[first], array[second]
    return -1, None

def check(func):
    for i in range(10):
        seed_time = time.time() * 5372654932**i
        random.seed(seed_time)
        array = []
        target = random.randint(0, 100)
        for _ in range(10):
            array.append(random.randint(0, 100))
        first, second = func(array, target)
        if second != None:
            print(f"{array} --> {target} --> {first}, {second}")
        else:
            print(f"{array} --> {target} --> No")


check(my_first_solution)

"""array = [1, 3, 5, 10, 20, 21]
res = my_first_solution(array, 4)
print(res)"""
