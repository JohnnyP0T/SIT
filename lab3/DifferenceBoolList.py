
import math


def difference(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(int(bool(list1[i]) != bool(list2[i])))
    return result

def differenceRec(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(abs(list1[i] - list2[i]))
    return result
