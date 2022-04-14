"""
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace 
the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

def solution(s):
    liste_paire = []
    paire = ""
    for i in s:
        paire += i
        if len(paire) == 2:
            liste_paire.append(paire)
            paire = ""
    if paire:
        liste_paire.append(paire + "_")
    return liste_paire

print(solution('abc')) #['ab', 'c_']
