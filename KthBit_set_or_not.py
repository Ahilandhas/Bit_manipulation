"""
How It Works

.	Bitwise Shift (1 << (k-1)):
o	This shifts the binary number 1 left by k−1k-1k−1 positions.
o	For example, if k=3k = 3k=3, then 1 << (3 - 1) = 1 << 2 results in 100 in binary, which is 4 in decimal.
o	This produces a mask with a 1 only in the kkkth bit position.


Bitwise AND n & (1 << (k-1)):
•	This performs a bitwise AND between nnn and the shifted value.
•	If the kkkth bit in nnn is 1, the result of the AND operation will be non-zero, indicating that the kkkth bit is set.
•	If the kkkth bit in nnn is 0, the result will be 0, meaning the bit is not set.
"""

def kthbitset(n,k):
    if n & (1 << k-1):
        print('set')

    else:
        print("Not set")


kthbitset(5,3)

or


def kthbitset(n,k):
    if ((n >> (k-1)) & 1 ):
        print('set')

    else:
        print("Not set")


kthbitset(5,3)
