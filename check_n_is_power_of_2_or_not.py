"""
check a given number is power of 2

"""

def ispow2(n):
    if n == 0:
        return False

    while n!=0:
        if n % 2 != 0:
            return False

        n = n // 2

    return True

n = 6
ispow2(n)


"""
using bitwise operation
More effient one
"""

def ispow2(n):

    if n == 0:
        return False

    return ( n & (n-1) == 0)


print(ispow2(8))
