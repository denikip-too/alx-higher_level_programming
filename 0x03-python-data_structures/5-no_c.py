#!/usr/bin/env python3
def no_c(my_string):
    mystring = list(my_string)
    for i in mystring:
        if i == 'c' or i == 'C':
            mystring.remove(i)
    return "".join(mystring)
