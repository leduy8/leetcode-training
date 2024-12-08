
from typing import List

# * https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/


def check(nums: List[int]) -> bool:
    counter = 0

    for i in range(len(nums)):
        if nums[i] > nums[(i+1) % len(nums)]:
            counter += 1
        if counter > 1:
            return False

    return True


print(check(nums=[3, 4, 5, 1, 2]))
print(check(nums=[2, 1, 3, 4]))
print(check(nums=[1, 2, 3]))
print(check(nums=[1, 1, 1]))
print(check(nums=[2, 1]))
