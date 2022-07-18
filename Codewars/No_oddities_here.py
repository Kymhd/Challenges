"""
Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given.
"""

def no_odds(values):
    # Return list of only even values
    return [x for x in values if x % 2 == 0]
  
  
  
  
test.assert_equals(no_odds([0, 1]), [0], 'Zero through one')
test.assert_equals(no_odds([0, 1, 2, 3]), [0, 2], 'Zero through three')
test.assert_equals(no_odds([1, 3, 5, 7, 9]), [], 'Odds through ten')
test.assert_equals(no_odds([0, 2, 4, 6, 8, 10]), [0, 2, 4, 6, 8, 10], 'Evens through ten')
test.assert_equals(no_odds([-1, -3, -5, -7, -9]), [], 'Negative odds')
