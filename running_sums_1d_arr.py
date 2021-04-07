from typing import List

# * https://leetcode.com/problems/running-sum-of-1d-array/


def running_sum(nums: List[int]) -> List[int]:
    res = []
    cur_arr = []

    for num in nums:
        cur_arr.append(num)
        res.append(sum(cur_arr))

    return res


print(running_sum([1, 2, 3, 4]))
