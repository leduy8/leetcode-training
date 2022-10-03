
# * https://leetcode.com/problems/max-consecutive-ones/

from typing import List


def max_consecutive_ones(nums: List[int]):
    max_ones = 0
    ones = 0

    for num in nums:
        if num == 1:
            ones += 1
        elif num == 0:
            max_ones = ones if ones > max_ones else max_ones
            ones = 0

    return ones if ones > max_ones else max_ones


print(max_consecutive_ones(nums=[1, 1, 0, 1, 1, 1]))  # 3
print(max_consecutive_ones(nums=[1, 0, 1, 1, 0, 1]))  # 2
