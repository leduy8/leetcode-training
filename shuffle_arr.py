from typing import List

# * https://leetcode.com/problems/shuffle-the-array/


def shuffle(nums: List[int], n: int) -> List[int]:
    res = []

    for i, _ in enumerate(nums):
        if (i < n):
            res.append(nums[i])

        if (i + n < len(nums)):
            res.append(nums[i + n])

    return res


print(shuffle([2, 5, 1, 3, 4, 7], 1))
print(shuffle([2, 5, 1, 3, 4, 7], 2))
print(shuffle([2, 5, 1, 3, 4, 7], 3))
print(shuffle([2, 5, 1, 3, 4, 7], 4))
print(shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
print(shuffle([1, 1, 2, 2], 2))
