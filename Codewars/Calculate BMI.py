"""
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
"""

def bmi(weight, height):
    #your code here
    bm = weight / height**2
    
    if bm <= 18.5:
         return "Underweight"
    if bm <= 25.0:
        return "Normal"
    if bm <= 30.0:
        return "Overweight"
    if bm > 30 :
        return "Obese"
        
        
