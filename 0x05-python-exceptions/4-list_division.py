#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i, result = 0, 0
    new_list = []

    while i < list_length:
        try:
            if my_list_1[i] % my_list_2[i] != 0:
                result = 0
            else:
                result = my_list_1[i] / my_list_2[i]
            new_list.append(result)

        except IndexError:
            new_list.append(0)
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except TypeError:
            print("wrong type")
            print("out of range")
            new_list.append(0)
        finally:
            i += 1

    return new_list
