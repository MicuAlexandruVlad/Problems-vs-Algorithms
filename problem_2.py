def binarySearch(array, left, right, target): 
    if right >= left: 
  
        middle = (left + right) // 2
  
        if array[middle] == target: 
            return middle 
        elif array[middle] < target: 
            return binarySearch(array, middle + 1, right, target) 
        else: 
            return binarySearch(array, left, middle - 1, target) 
  
    else: 
        return -1

def findPivot(array, left, right): 
    if right == left: 
        return left
    elif right < left: 
        return -1

    # print('Array: ', array)
    # print('Left: ', left)
    
    middle = (left + right) // 2 
      
    if middle > left and array[middle] < array[middle - 1]: 
        return middle - 1
    elif middle < right and array[middle] > array[middle + 1]: 
        return middle 
    elif array[left] >= array[middle]: 
        return findPivot(array, left, middle - 1) 
    return findPivot(array, middle + 1, right) 

def rotatedArraySearch(array, target): 
  
    n = len(array)
    pivot = findPivot(array, 0, n - 1)
  
    if pivot == -1: 
        return binarySearch(array, 0, n - 1, target)

    if array[pivot] == target: 
        return pivot 
    if array[0] > target: 
        return binarySearch(array, pivot + 1, n - 1, target)
    return binarySearch(array, 0, pivot - 1, target)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotatedArraySearch(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])