#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mylist = list(my_list)
    for i in mylist:
        if i % 2 == 0:
            mylist[i] = True
        else:
            mylist[i] = False
    return mylist
