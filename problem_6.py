import random

def findMinMax(array):
    minNumber = 10
    maxNumber = 0

    for number in array:
        if number > maxNumber:
            maxNumber = number
        if number < minNumber:
            minNumber = number
    
    return minNumber, maxNumber

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print(findMinMax(l))





