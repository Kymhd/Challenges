"""
Your task is to make two functions (max and min, or maximum and minimum, etc., 
depending on the language) that receive a list of integers as input and return,
respectively, the largest and lowest number in that list.

Examples (Input -> Output)
* [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
* [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
* [42, 54, 65, 87, 0]             -> min = 0, max = 87
* [5]                             -> min = 5, max = 5
Notes
You may consider that there will not be any empty arrays/vectors.
"""

def minimum(arr):
    #your code here...
    # return min(arr)
    minim = arr[0]
    for nombre in arr:
        if minim > nombre:
            minim = nombre
    return minim

  
def maximum(arr):
    #...and here
    return max(arr)
  
  
test.assert_equals(minimum([-52, 56, 30, 29, -54, 0, -110]), -110)
test.assert_equals(minimum([42, 54, 65, 87, 0]), 0)
test.assert_equals(minimum([1, 2, 3, 4, 5, 10]), 1)
test.assert_equals(minimum([-1, -2, -3, -4, -5, -10]), -10)
test.assert_equals(minimum([9]), 9)
