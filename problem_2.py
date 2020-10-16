def binarySearch(array, left, right, target): 
    if right >= left: 
  
        mid = left + (right - left) // 2
  
        if array[mid] == target: 
            return mid 
        elif array[mid] > target: 
            return binarySearch(array, left, mid-1, target) 
        else: 
            return binarySearch(array, mid + 1, right, target) 
  
    else: 
        return -1

def findPivot(array, left, right): 
      
    # base cases 
    if right < left: 
        return -1
    if right == left: 
        return left 
      
    mid = int((left + right)/2) 
      
    if mid < right and array[mid] > array[mid + 1]: 
        return mid 
    if mid > left and array[mid] < array[mid - 1]: 
        return mid - 1
    if array[left] >= array[mid]: 
        return findPivot(array, left, mid - 1) 
    return findPivot(array, mid + 1, right) 

def rotatedArraySearch(array, target): 
  
    n = len(array)
    pivot = findPivot(array, 0, n - 1)
  
    if pivot == -1: 
        return binarySearch(array, 0, n - 1, target)
  
    if array[pivot] == target: 
        return pivot 
    if array[0] <= target: 
        return binarySearch(array, 0, pivot - 1, target)
    return binarySearch(array, pivot + 1, n - 1, target)

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