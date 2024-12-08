from typing import List


# * https://leetcode.com/problems/search-insert-position/

def searchInsert(nums: List[int], target: int) -> int:
    for i, val in enumerate(nums):
        if target <= val:
            return i

    return len(nums)


print(searchInsert(nums=[1, 3, 5, 6], target=5))  # 2
print(searchInsert(nums=[1, 3, 5, 6], target=2))  # 1
print(searchInsert(nums=[1, 3, 5, 6], target=7))  # 4
