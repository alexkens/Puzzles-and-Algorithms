"""
Egg Floor Problem:
- usually told as this: with 2 eggs and a 100 storey building, we want to find out at what
floor when dropped the eggs break
- but what if we generalize the problem by using variables for N eggs and K floors
- the normal solution is normally: x + (x-1) + (x-2) + ... + 2 + 1 = n*(n+1)/2 = K, there by
we can optimize for every K the amount of droppings

"""


import math
import sys


def egg_floor_formula(floors: int):
    return math.floor(1/2 + math.sqrt(1/4 + 2 * floors))


def egg_floor(eggs: int, floors: int):

    if eggs == 0:
        return -1
    if eggs == 1:
        return floors

    min_trials = floors
    min_trials = egg_floor_formula(floors)
    while eggs > 2:
        print(f"Eggs: {eggs}, Floors: {floors}, Minimum Trials: {min_trials}")
        min_trials = egg_floor_formula(min_trials - 1) + 1
        eggs -= 1
    
    return min_trials


def eggDrop(eggs: int, floors: int):
    """Recursive function that finds the least amount of egg drops."""

    print(f"eggs: {eggs}, floors: {floors}")

    # base case one egg --> all the floors count
    # base case zero or one floor --> only zero or one floor can be counted, no matter how many eggs
    if eggs == 1 or floors <= 1:
        return floors
    if eggs == 0:
        return 0
    
    min_trials = sys.maxsize
    for step in range(1, floors + 1):
        result = max(eggDrop(eggs, floors-step), eggDrop(eggs-1, step-1))
        if result < min_trials:
            min_trials = result

    return 1 + min_trials


N = 3 # eggs
K = 4 # floors

result1 = egg_floor(N, K)
result2 = eggDrop(N, K)
print(result1, result2)
