from typing import List


# * https://leetcode.com/problems/decompress-run-length-encoded-list/

def decompressRLElist(nums: List[int]) -> List[int]:
    res = []

    for i in range(len(nums))[::2]:
        for _ in range(nums[i]):
            res.append(nums[i+1])

    return res


print(decompressRLElist(nums=[1, 2, 3, 4]))  # [2,4,4,4]
print(decompressRLElist(nums=[1, 1, 2, 3]))  # [1,3,3]
