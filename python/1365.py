from typing import List

# * https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

def smaller_numbers_than_current(nums: List[int]) -> List[int]:
    num_bigger_counter = {}
    sorted_num = sorted(nums)

    for i, num in enumerate(sorted_num):
        num_bigger_counter.setdefault(num, i)

    return [num_bigger_counter.get(n) for n in nums]


print(smaller_numbers_than_current(nums = [8, 1, 2, 2, 3]))
print(smaller_numbers_than_current(nums = [6, 5, 4, 8]))
print(smaller_numbers_than_current(nums = [7, 7, 7, 7]))
