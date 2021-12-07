#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    x = 0
    while x < list_length:
        try:
            result = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("Wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            x += 1
            res.append(result)
    return (res)
