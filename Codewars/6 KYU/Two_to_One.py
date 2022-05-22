"""
Take 2 strings s1 and s2 including only letters from ato z. 
Return a new sorted string, the longest possible,
containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""
def longest(a1, a2):
    # your code
    new = ""
    for i in a1:
        if i not in new:
            new += i
    for j in a2:
        if j not in new:
            new += j
            
    return "".join(sorted(new))
  
  
test.assert_equals(longest("aretheyhere", "yestheyarehere"), #"aehrsty")
test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), #"abcdefghilnoprstu")
test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"),#"acefghilmnoprstuy")
