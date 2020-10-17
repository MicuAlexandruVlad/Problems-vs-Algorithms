def mergeSort(array): 
    if len(array) > 1: 
        mid = len(array) // 2
        left = array[:mid] 
        right = array[mid:]
  
        mergeSort(left)
        mergeSort(right)
  
        i = j = k = 0
          
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                array[k] = left[i] 
                i += 1
                # print(left)
            else: 
                array[k] = right[j] 
                j += 1
                # print(right)
            k += 1

        while i < len(left): 
            array[k] = left[i] 
            i += 1
            k += 1
            # print(left)
          
        while j < len(right): 
            array[k] = right[j] 
            j += 1
            k += 1
            # print(right)

def findNumbers(sortedArray):
    if len(sortedArray) == 2:
        return sortedArray[1], sortedArray[0]
    elif len(sortedArray) <= 1:
        return sortedArray
    elif len(sortedArray) > 2:
        num1 = 0
        num2 = 0

        i = len(sortedArray) - 1
        while i >= 0:
            num1 = num1 * 10 + sortedArray[i]
            i -= 2

        i = len(sortedArray) - 2
        while i >= 0:
            num2 = num2 * 10 + sortedArray[i]
            i -= 2

        return num1, num2




def test_function(test_case):
    mergeSort(test_case[0])
    output = findNumbers(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case1 = [[1, 2, 3, 4, 5], [542, 31]]
test_case2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case3 = [[1, 2], [1, 2]]
test_case4 = [[1], [1]]
test_case5 = [[], []]
test_function(test_case1)
test_function(test_case2)
test_function(test_case3)
test_function(test_case4)
