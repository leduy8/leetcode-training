from typing import List

# * https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums: List[int]) -> bool:
    occ = {}

    for num in nums:
        if num not in occ:
            occ[num] = 1
        else:
            return True

    return False


print(containsDuplicate(nums = [1,2,3,1])) # True
print(containsDuplicate(nums = [1,2,3,4])) # False
print(containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2])) # True