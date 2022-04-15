"""
Given an array of integers.

Return an array, where the first element is the count of positives numbers and
the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15],
you should return [10, -65].
"""
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    som_negative = 0
    count_positive = 0
    for i in arr:
        if i > 0:
            count_positive = count_positive + 1
        else:
            som_negative += i
    return [count_positive, som_negative]

print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])) #[8, -50]
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])) #[10, -65]
print(count_positives_sum_negatives([])) #[]
