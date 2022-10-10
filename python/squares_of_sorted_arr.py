from typing import List

# * https://leetcode.com/problems/squares-of-a-sorted-array/


def sortedSquares(nums: List[int]) -> List[int]:
    nums = [num * num for num in nums]
    nums.sort()
    return nums


print(sortedSquares([-4, -1, 0, 3, 10]))  # [0,1,9,16,100]
print(sortedSquares([-7, -3, 2, 3, 11]))  # [4,9,9,49,121]
