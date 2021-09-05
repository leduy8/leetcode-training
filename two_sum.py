from typing import List
from itertools import islice

# * https://leetcode.com/problems/two-sum/


def nth_index(iterable, value, n):
    matches = (i for i, val in enumerate(iterable) if val == value)
    return next(islice(matches, n-1, n), None)

def two_sum(nums: List[int], target: int) -> List[int]:
    res = []
    for i, val in enumerate(nums):
        remain = target - val
        if remain in nums and nums.index(remain) != i:
            res.append(i)
            res.append(nums.index(remain))
            break
        elif remain == val and nth_index(nums, val, 2):
            res.append(i)
            res.append(nth_index(nums, val, 2))
            break
    return res

print(two_sum(nums=[2, 7, 11, 15], target=9)) # [0, 1]
print(two_sum(nums=[3, 2, 4], target=6)) # [1, 2]
print(two_sum(nums=[3, 3], target=6)) # [0, 1]
print(two_sum(nums=[-1, -2, -3, -4, -5], target=-8)) # [2, 4]
