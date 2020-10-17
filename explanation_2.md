# Search in a Rotated Sorted Array

- The algorithm searches for a pivot value which can be looked at as a point where the initial array is split into 2 subarrays that are sorted.
- After the pivot value is found, we can compare its value to the target value and then apply Binary Search accordingly
- The time complexity is the same as Binary Search, which is O(logn), n being the length of the array
- This algorithm takes constant space; O(1)
