from typing import List

# * https://leetcode.com/problems/concatenation-of-array/


def get_concatenation(nums: List[int]) -> List[int]:
    return [*nums, *nums]


print(get_concatenation(nums=[1, 2, 1]))
print(get_concatenation(nums=[1, 3, 2, 1]))
