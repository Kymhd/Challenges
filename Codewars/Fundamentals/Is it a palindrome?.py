"""
Write a function that checks if a given string (case insensitive) is a palindrome.
"""
def is_palindrome(s):
    s = s.upper()
    return s == s[::-1]
  
test.assert_equals(is_palindrome('a'), True)
test.assert_equals(is_palindrome('aba'), True)
test.assert_equals(is_palindrome('Abba'), True)
test.assert_equals(is_palindrome('malam'), True)
test.assert_equals(is_palindrome('walter'), False)
test.assert_equals(is_palindrome('kodok'), True)
test.assert_equals(is_palindrome('Kasue'), False)
