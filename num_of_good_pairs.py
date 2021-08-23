from typing import List

# * https://leetcode.com/problems/number-of-good-pairs/

# * HINT: Count how many N occurrences in the list and use the formula: n * (n - 1) // 2


def num_identical_pairs(nums: List[int]) -> int:
    res = 0
    occurrences = {}
    for num in nums:
        if num not in occurrences:
            occurrences[num] = 1
        else:
            occurrences[num] += 1
        
    for key, value in occurrences.items():
        res += value * (value - 1) // 2
    
    return res


print(num_identical_pairs([1, 2, 3, 1, 1, 3])) # 4
print(num_identical_pairs([1, 1, 1, 1]))  # 6
print(num_identical_pairs([1, 2, 3]))  # 0
