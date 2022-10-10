
# * https://leetcode.com/problems/valid-perfect-square/

def mySqrt(x: int) -> int:
    left = 0
    right = x

    while left <= right:
        mid = left + (right - left) // 2
        if x < mid * mid:
            right = mid - 1
        elif x > mid * mid:
            left = mid + 1
        else:
            return True

    return False


print(mySqrt(5))
print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(1))
print(mySqrt(9))
print(mySqrt(16))
print(mySqrt(25))
print(mySqrt(5))