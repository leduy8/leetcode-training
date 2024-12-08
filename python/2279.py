from typing import List

# * https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/


def maximumBags(capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    full_bags = 0
    remaining_capacity = [cap - rock for cap, rock in zip(capacity, rocks)]
    remaining_capacity.sort()

    for cur_capacity in remaining_capacity:
        if additionalRocks >= cur_capacity:
            additionalRocks -= cur_capacity
            full_bags += 1
        else:
            break

    return full_bags


print(maximumBags(capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2)) # 3
print(maximumBags(capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100)) # 3