# ARRANGE NUMBER TO FORM BIGGER NUMBER
from itertools import permutations


def printLargest(arr):
    max = 0
    for j in permutations(arr, len(arr)):

        temp = "".join(map(str, j))
        if int(temp) > max:
            max = int(temp)

    return (max)
arr = [3, 30, 34, 5, 9, 34, 23, 98]

print(printLargest(arr))
