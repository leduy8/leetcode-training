from typing import List


# * https://leetcode.com/problems/remove-element/

def removeElement(nums: List[int], val: int) -> int:
    count = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1

    return count


print(removeElement(nums=[3, 2, 2, 3], val=3))  # 2, nums = [2,2,_,_]
print(removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))  # 5, nums = [0,1,4,0,3,_,_,_]
