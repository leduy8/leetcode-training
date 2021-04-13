from typing import List


def smaller_numbers_than_current(nums: List[int]) -> List[int]:
    res = []
    count = 0

    for num in nums:
        for num_2 in nums:
            if num_2 < num:
                count += 1
        res.append(count)
        count = 0

    return res


print(smaller_numbers_than_current([6, 5, 4, 8]))
print(smaller_numbers_than_current([7, 7, 7, 7]))
