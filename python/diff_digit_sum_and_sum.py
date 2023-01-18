from typing import List

# * https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/


def differenceOfSum(nums: List[int]) -> int:
    digit_nums = []
    sum_nums = sum(nums)
    for num in nums:
        for d in str(num):
            digit_nums.append(int(d))
    digit_nums_sum = sum(digit_nums)
    return abs(sum_nums - digit_nums_sum)


print(differenceOfSum(nums = [1,15,6,3])) # 9
print(differenceOfSum(nums = [1,2,3,4])) # 0