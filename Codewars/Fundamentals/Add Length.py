"""
What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

add_length('apple ban') => ["apple 5", "ban 3"]
add_length('you will win') => ["you 3", "will 4", "win 3"]
Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

Note: String will have at least one element; words will always be separated by a space.



def concatenation(l): 
    """
    fonction qui va prendre en fonction la liste pour concatener chaque element de la 
    liste avec se longueur.
    """ 
    liste = [] #nouvelle liste 
    for i in l:
        a = i + " " + str(len(i)) #chaque element i + len(i)
        liste.append(a) #ajouter i + len(i) à la nouvelle liste
        
    return liste
        

def add_length(str_): 
    """
    fonction qui va prendre une chaine de caractère en parametre et qui la 
    trnsforme en liste.
    """ 
    #your code here
    nouvel_liste = str_.split() #Transformation de la chaine en liste
    reponse = concatenation(nouvel_liste) # appele la fonction pour 
    return reponse 
"""
    
    
    
    
    
def add_length(str_): 
    #your code here
    nouvel_liste = str_.split() #Transformation de la chaine en liste
    return [i + " " + str(len(i)) for i in nouvel_liste] 
  
  
test.assert_equals(add_length('apple ban'),["apple 5", "ban 3"])
test.assert_equals(add_length('you will win'),["you 3", "will 4", "win 3"])
test.assert_equals(add_length('you'),["you 3"])
test.assert_equals(add_length('y'),["y 1"])
