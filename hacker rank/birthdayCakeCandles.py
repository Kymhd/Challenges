

def birthdayCakeCandles(candles):
    # Write your code here
    """
    comprehension de liste qui retourne le nombre
    de doublon d'une liste donneé en parametre
    """
    return len([i for i in candles if candles.count(i) > 1])
