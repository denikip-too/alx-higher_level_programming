#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    length = 0
    avg = 0
    for i in my_list:
        sum += (i[0] * i[1])
        length += i[1]
        avg = sum / length
    return avg
