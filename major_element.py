from typing import List

# * https://leetcode.com/problems/majority-element/


def majority_element(nums: List[int]) -> int:
    elements = []
    occurrences = {}
    for num in nums:
        if num not in elements:
            elements.append(num)
            occurrences[num] = 1
        else:
            occurrences[num] += 1

    return max(occurrences, key=occurrences.get)


print(majority_element([3, 2, 3])) # 3
print(majority_element([2, 2, 1, 1, 1, 2, 2])) # 2
