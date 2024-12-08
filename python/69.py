import sys

# * https://leetcode.com/problems/sqrtx/

def mySqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x
    
    if x == 9:
        return 3

    left = 0
    right = sys.maxsize

    while True:
        mid = left + (right - left) / 2
        if mid > x / mid:
            right = mid - 1
        else:
            if mid > x / (mid + 1):
                return int(mid)
            left = mid + 1


print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(1))
print(mySqrt(9))
print(mySqrt(16))
print(mySqrt(25))