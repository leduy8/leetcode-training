from typing import List

# * https://leetcode.com/problems/richest-customer-wealth/


def maximum_wealth(accounts: List[List[int]]) -> int:
    wealths = [sum(account) for account in accounts]
    return max(wealths)


print(maximum_wealth([[1, 2, 3], [3, 2, 1], [2, 1]]))
