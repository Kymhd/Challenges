"""
Your task in order to complete this Kata is to write a function which formats a duration,
given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer.
If it is zero, it just returns "now". Otherwise,
the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
    
    
 MORE INFORMATION VISIT THIS ===> https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
 
 """

def format_duration(seconds):
    if (seconds == 0):
        return ("now")
    minute = 0
    hour = 0
    temp = 0
    res = ""
    day = 0
    year = 0
    while (seconds >= 60):
        seconds = seconds - 60
        minute += 1
        if (minute % 60 == 0):
            hour += 1
            minute = 0
        if (hour % 24 == 0) & (hour > 0):
            day += 1
            hour = 0
        if (day % 365 == 0) & (day > 0):
            year += 1
            day = 0
    if (year > 0):
        if (year == 1):
            res = str(year) + " year"
        else:
            res = str(year) + " years"
    if (day > 0):
        if (year > 0):
            if (day == 1):
                res = res + ", " + str(day) + " day"
            else:
                res = res + ", " + str(day) + " days"
        else:
            if (day == 1):
                res = str(day) + " day"
            else:
                res = str(day) + " days"
    if (hour > 0):
        if (day < 1):
            if (hour == 1):
                res = "" + str(hour) + " hour"
            else:
                res = "" + str(hour) + " hours"
        else:
            if (hour == 1):
                res = res = res + ", " + str(hour) + " hour"
            else:
                res = res = res + ", " + str(hour) + " hours"
    if (minute > 0):
        if (hour > 0):
            if (minute == 1):
                if (seconds != 0):
                    res = res + ", " + str(minute) + " minute"
                else:
                    res = res + " and " + str(minute) + " minute"
            else:
                if (seconds != 0):
                    res = res + ", " + str(minute) + " minutes"
                else:
                    res = res + " and " + str(minute) + " minutes"
        else:
            if (minute == 1):
                if (seconds != 0):
                    res = res + ", " + str(minute) + " minute"
                else:
                    res = res + " and " + str(minute) + " minute"
                res = str(minute) + " minute"
            else:
                if (seconds != 0):
                    res = res + ", " + str(minute) + " minutes"
                else:
                    res = res + " and " + str(minute) + " minutes"
                res = str(minute) + " minutes"
    if (seconds > 0):
        if (minute > 0) | (hour > 0):
            if (seconds == 1):
                res = res + " and " + str(seconds) + " second"
            else:
                res = res + " and " + str(seconds) + " seconds"
        else:
            if (seconds == 1):
                res = str(seconds) + " second"
            else:
                res = str(seconds) + " seconds"

    return (res)
