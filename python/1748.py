from typing import List

# * https://leetcode.com/problems/sum-of-unique-elements/


def sum_of_unique(nums: List[int]) -> int:
    unique_nums = []
    for num in nums:
        if nums.count(num) == 1:
            unique_nums.append(num)

    return sum(unique_nums)


print(sum_of_unique([1, 2, 3, 2]))
print(sum_of_unique([1, 1, 1, 1, 1]))
print(sum_of_unique([1, 2, 3, 4, 5]))
