"""
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
"""
def remove_exclamation_marks(s):
    #your code here
    return s.replace("!","")
  
test.assert_equals(remove_exclamation_marks("Hello World!"), "Hello World")
test.assert_equals(remove_exclamation_marks("Hello World!!!"), "Hello World")
test.assert_equals(remove_exclamation_marks("Hi! Hello!"), "Hi Hello")
test.assert_equals(remove_exclamation_marks(""), "")
test.assert_equals(remove_exclamation_marks("Oh, no!!!"), "Oh, no")
