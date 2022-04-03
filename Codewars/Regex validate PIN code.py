"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""
def validate_pin(pin):
    #return true or false
    if pin.isdigit() :
        if len(pin) == 6 or len(pin) == 4:
            return True
        else:
            return False
    else:
        return False
      
# def validate_pin(pin):
   # return len(pin) in (4, 6) and pin.isdigit()
  
  # return pin.isdigit() and (len(pin) == 6 or len(pin) == 4)


      
