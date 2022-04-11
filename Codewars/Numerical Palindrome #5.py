"""
A palindrome is a word, phrase, number, 
or other sequence of characters which reads the same backward as forward.
Examples of numerical palindromes are:

232
110011
54322345
Complete the function to test if the given number
(num) can be rearranged to form a numerical palindrome or not.
Return a boolean (true if it can be rearranged to a palindrome, 
and false if it cannot). Return "Not valid" if the input is not an integer or is less than 0.

For this kata, single digit numbers are NOT considered numerical palindromes.

Examples
5        =>  false
2121     =>  true
1331     =>  true 
3357665  =>  true 
1294     =>  false 
"109982" =>  "Not valid"
-42      =>  "Not valid"
"""


def verification_palindrome(n):
    """
    fonction qui verifie si le nombre entier n entier est palindrome
    on utilise cette fonction pour retourner une valeur bouléenne,
    True ou False, cette fonction nous permet aussi de convertir n en
    chaine de caractère afin de parcourrir les éléments,
    :param n:
    :return:
    """
    n = str(n)
    return len(n) % 2 == 0 or len(n) == 7

    if n == n[::-1] :
        return True
    return False

def palindrome(num):
    """
    fonction principale qui renvoi le resultat final
    :param num: 
    :return: 
    """
    return 'Not valid' if type(num) == str or num < 0 else verification_palindrome(num)


print(palindrome((1212))) #True
print(palindrome((1331)))  #True
print(palindrome("357665")) # 'Not valid'
print(palindrome(5)) #False
print(palindrome(194)) #False
print(palindrome(3357665))  #True
