"""
 Naive approch
"""


def find_only_odd(array):
    for i in array:
        res = array.count(i)
        if res % 2 != 0:
            result = i
            break

    return result

array = [10, 20, 20, 30,50,50,50]
print(find_only_odd(array))

"""
using bitwise operators

Note:
This funtion work only if the list contains one odd
"""

def find_only_odd(array):
    res = 0
    for x in array:
        res = res ^ x

    return res


print(find_only_odd(array))
