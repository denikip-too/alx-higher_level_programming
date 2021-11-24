#!/usr/bin/python3
def uniq_add(my_list=[]):
    mylist = []
    sum = 0
    for i in my_list:
        if i not in mylist:
            mylist.append(i)
    for i in mylist:
        sum += i
    return sum
