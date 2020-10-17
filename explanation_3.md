# Rearrange Array Elements

- This algorithm uses the Merge Sort method to achieve a time complexity of O(nlogn), where n is the length of the array, and a time complexity of O(1)
- After the array is sorted, we can traverse the array to get the 2 numbers that will lead to the maximum possible sum. This is achieved by incrementing the index by a value of 2 starting at index 0 and then at `i = len(sortedArray) - 1` and then at `i = len(sortedArray) - 2`
