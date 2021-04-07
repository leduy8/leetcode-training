from typing import List

# * https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    after_give_candies = [candy + extraCandies for candy in candies]
    return [candy == max(after_give_candies) for candy in after_give_candies]


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
