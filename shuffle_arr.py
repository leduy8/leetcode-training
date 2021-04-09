from typing import List

# * https://leetcode.com/problems/shuffle-the-array/


def shuffle(nums: List[int], n: int) -> List[int]:
    res = []

    for i, num in enumerate(nums):
        if(i == n or i + n == len(nums) - 1):
            break
        res.append(nums[i])
        res.append(nums[i + n])
        i += 1

    while i <= n:
        res.append(nums[i])
        i += 1

    while i + n <= len(nums) - 1:
        res.append(nums[i + n])
        i += 1

    return res


# print(shuffle([2, 5, 1, 3, 4, 7], 3))
print(shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
# print(shuffle([1, 1, 2, 2], 2))
