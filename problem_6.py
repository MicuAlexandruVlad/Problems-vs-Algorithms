import random
import math

def findMinMax(array):
    if len(array) > 0:
        minNumber = array[0]
        maxNumber = array[0]

        for number in array:
            if number > maxNumber:
                maxNumber = number
            if number < minNumber:
                minNumber = number

        return minNumber, maxNumber
    
    return None, None



print(findMinMax([1, 2, -1, 2, 4]))
print(findMinMax([2, 2, 2, 2, 2, 2, 2, 2]))
print(findMinMax([1, 2, 2, 3, 4, 5, 6, 1, 1, 2, 0]))
print(findMinMax([1]))
print(findMinMax([]))





