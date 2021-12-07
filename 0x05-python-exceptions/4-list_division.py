#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for x in range(0, list_length):
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
            res.append(result)
    return (res)
