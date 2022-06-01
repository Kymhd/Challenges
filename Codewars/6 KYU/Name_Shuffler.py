"""
Write a function that returns a string in which firstname is swapped with last name.

name_shuffler('john McClane'); => "McClane john"
"""

def name_shuffler(str_):
    #your code here
    l = str_.split()
    return " ".join(l[::-1])
  
  
  
