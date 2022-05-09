"""
Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in th same order.

"h,o,l,a"
"""
def print_array(arr):
    #your code here
    liste = [str(i) for i in arr]
    return ",".join(liste)
