
# https://leetcode.com/problems/smallest-even-multiple/

def smallestEvenMultiple(n: int) -> int:
    if n % 2 == 0:
        return n

    return n * 2


print(smallestEvenMultiple(5)) # 10
print(smallestEvenMultiple(6)) # 6