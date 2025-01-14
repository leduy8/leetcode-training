# * https://leetcode.com/problems/power-of-two/
from itertools import count


def isPowerOfTwo(n: int) -> bool:
    for i in count(start=0):
        if n == 1:
            return True

        if 2 << i == n:
            return True
        elif 2 << i > n:
            return False

print(isPowerOfTwo(n=1))  # True
print(isPowerOfTwo(n=16))  # True
print(isPowerOfTwo(n=3))  # False