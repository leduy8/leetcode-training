from typing import List
from itertools import islice

# * https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


def nth_index(iterable, value, n):
    matches = (i for i, val in enumerate(iterable) if val == value)
    return next(islice(matches, n-1, n), None)

def two_sum(nums: List[int], target: int) -> List[int]:
    res = []
    for i, val in enumerate(nums):
        remain = target - val
        if remain in nums and nums.index(remain) != i:
            res.append(i + 1)
            res.append(nums.index(remain) + 1)
            break
        elif remain == val and nth_index(nums, val, 2):
            res.append(i + 1)
            res.append(nth_index(nums, val, 2) + 1)
            break
    return res

print(two_sum(nums=[2, 7, 11, 15], target=9)) # [1, 2]
print(two_sum(nums=[2, 3, 4], target=6)) # [1, 3]
print(two_sum(nums=[-1, 0], target=6)) # [1, 2]