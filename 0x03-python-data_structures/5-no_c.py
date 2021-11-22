#!/usr/bin/env python3
def no_c(my_string):
    mystring = list(my_string)
    j = 0
    for i in mystring:
        if i == 'c' and i == 'C':
            mystring[j] = ""
        j += 1
    return "".join(mystring)
