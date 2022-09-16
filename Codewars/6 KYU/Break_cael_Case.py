"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

"""



def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
  
 
# def solution(s):
#     new_chaine = ""
    
#     for i in chain:
#         if i.isupper():
#             new_chaine += " " + i
#         else:
#             new_chaine += i  
#     return new_chaine
        
# print(solution(chain)) #chain = "camelCasing"
  
  
