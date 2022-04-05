"""
Write a function, which takes a non-negative integer (seconds) 
as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

"""
def make_readable(ss):
    # Do something
    (hh, ss) = divmod(ss, 3600)
    (mm, ss) = divmod(ss, 60)
    
    if len(str(ss))<2:
        ss = "0"+str(ss)
    if len(str(mm))<2:
        mm = "0"+str(mm)
    if len(str(hh))<2: 
        hh = "0"+str(hh)
    
    return f"{hh}:{mm}:{ss}"
      
      
test.assert_equals(make_readable(0), "00:00:00")
test.assert_equals(make_readable(5), "00:00:05")
test.assert_equals(make_readable(60), "00:01:00")
test.assert_equals(make_readable(86399), "23:59:59")
test.assert_equals(make_readable(359999), "99:59:59")
