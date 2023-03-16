"""
Determine the total number of digits in the integer (n>=0) given as input to the function.
For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. 
Be careful to avoid overflows/underflows.

All inputs will be valid.
"""
def digits(n):
    # your code here
    return len(str(n))
  
print(count_digits(9)) # Output: 1
print(count_digits(66)) # Output: 2
print(count_digits(128685)) # Output: 6
