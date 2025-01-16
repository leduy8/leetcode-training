# * https://leetcode.com/problems/product-of-array-except-self/
# Guide: https://neetcode.io/solutions/product-of-array-except-self

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
    prefix = [0] * n
    suffix = [0] * n

    prefix[0] = suffix[n-1] = 1
    for i in range(1, n):
        prefix[i] = nums[i-1] * prefix[i-1]
    for i in range(n-2, -1, -1):
        suffix[i] = nums[i+1] * suffix[i+1]
    for i in range(n):
        result[i] = prefix[i] * suffix[i]
    
    return result


print(productExceptSelf(nums=[1,2,3,4]))  # [24,12,8,6]
print(productExceptSelf(nums=[-1,1,0,-3,3]))  # [0,0,9,0,0]

