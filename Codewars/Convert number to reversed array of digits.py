"""
Given a random non-negative number,
you have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
0 => [0]
"""

def digitize(n):
    """
    liste = []
    n = str(n)
    for i in n[::-1]:
        liste.append(int(i))
    return liste
    """
    return [int(i) for i in str(n)[::-1]]
print(digitize(35231))
