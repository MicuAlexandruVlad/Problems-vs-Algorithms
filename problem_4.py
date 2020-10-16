def singleTraversalSort(array):
    count = {0: 0, 1: 0, 2: 0}
    
    for item in array:
        if item == 0:
            count[0] += 1
        elif item == 1:
            count[1] += 1
        elif item == 2:
            count[2] += 1
    
    sortedArray = []
    print(count)

    appendElements(sortedArray, 0, count[0])
    appendElements(sortedArray, 1, count[1])
    appendElements(sortedArray, 2, count[2])

    return sortedArray

def appendElements(array, element, count):
    while count != 0:
        array.append(element)
        count -= 1


array = [0, 0, 1, 2,0,1,2,0,0,0,2,0,0,1,2,1]
print(singleTraversalSort(array))
