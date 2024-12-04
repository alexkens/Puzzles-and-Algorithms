"""
Egg Floor Problem:
- usually told as this: with 2 eggs and a 100 storey building, we want to find out at what
floor when dropped the eggs break
- but what if we generalize the problem by using variables for N eggs and K floors
- the normal solution is normally: x + (x-1) + (x-2) + ... + 2 + 1 = n*(n+1)/2 = K, there by
we can optimize for every K the amount of droppings

"""


import math


def egg_floor_formula(floors: int):
    return math.floor(1/2 + math.sqrt(1/4 + 2 * floors))


def egg_floor(eggs: int, floors: int):

    if eggs == 0:
        return -1
    if eggs == 1:
        return floors

    min_trials = 0
    print(f"i: {0}, Floors: {floors}, Minimum Trials: {min_trials}")
    for i in range(eggs-1):
        floors = egg_floor_formula(floors)
        min_trials += floors
        floors -= 1
        print(f"i: {i}, Floors: {floors}, Minimum Trials: {min_trials}")
    
    return min_trials





N = 3 # eggs
K = 100 # floors

result = egg_floor(N, K)
print(result)
