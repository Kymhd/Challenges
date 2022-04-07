"""
The Zemour's Algorithm
As you might know, Eric Zemour wants to make a person's name a bit more French.
Your mission here is to create a function that takes a person's name and returns their French name.

You will need to take the closest name from the calendar that you can find here. It is pre-loaded in the kata as NAMES.

The closest name will be the name in alphabetical order that follows the stranger's name.

Exceptions
Do not take the first two name of January (Marie mère de Dieu Basile de Césarée et Grégoire de Nazianze)

The algorithm doesn't consider the gender.

The algorithm doesn't contain the name Victor (Victor Hugo) because his political ideas were not the same as Zemour
"""

def Zemour(name):
    for i in sorted(NAMES):
        if i >= name:
            return i
               
test.assert_equals(Zemour("Alan")  , "Alban")
test.assert_equals(Zemour("Simon") , "Simon")
test.assert_equals(Zemour("Malwenn"), "Marc")
test.assert_equals(Zemour("John"), "Joseph")
