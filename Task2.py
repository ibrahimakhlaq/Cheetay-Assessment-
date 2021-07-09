# ARRANGE NUMBER TO FORM BIGGER NUMBER
from itertools import permutations


def printLargest(arr):
    log = []
    for j in permutations(arr, len(arr)):

        log.append("".join(map(str, j)))
    return max(log)


arr = [3, 30, 34, 5, 9, 34, 23, 98]

printLargest(arr)
