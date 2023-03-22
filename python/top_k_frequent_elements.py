from typing import List

# * https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent(nums: List[int], k: int) -> List[int]:
    res = []
    occ = {}

    for num in nums:
        if num in occ:
            occ[num] += 1
        else:
            occ[num] = 1

    occ = sorted(occ.items(), key=lambda item: item[1], reverse=True)
    
    for i in range(k):
        res.append(occ[i][0])

    return res


print(topKFrequent(nums = [1,1,1,2,2,3], k = 2)) # [1,2]
print(topKFrequent(nums = [1], k = 1)) # [1]
