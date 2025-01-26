from typing import List

# * https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


## Old, is hard due to using find algo
# def nth_index(iterable, value, n):
#     matches = (i for i, val in enumerate(iterable) if val == value)
#     return next(islice(matches, n-1, n), None)

# def twoSum(nums: List[int], target: int) -> List[int]:
#     res = []
#     for i, val in enumerate(nums):
#         remain = target - val
#         if remain in nums and nums.index(remain) != i:
#             res.append(i + 1)
#             res.append(nums.index(remain) + 1)
#             break
#         elif remain == val and nth_index(nums, val, 2):
#             res.append(i + 1)
#             res.append(nth_index(nums, val, 2) + 1)
#             break
#     return res

def twoSum(nums: List[int], target: int) -> List[int]:
    first_idx = 0
    last_idx = len(nums) - 1

    while True:
        temp_sum = nums[first_idx] + nums[last_idx]

        if temp_sum > target:
            last_idx -= 1
        elif temp_sum < target:
            first_idx += 1

        if temp_sum == target:
            return [first_idx + 1, last_idx + 1]


print(twoSum(nums=[2, 7, 11, 15], target=9)) # [1, 2]
print(twoSum(nums=[2, 3, 4], target=6)) # [1, 3]
print(twoSum(nums=[-1, 0], target=-1)) # [1, 2]