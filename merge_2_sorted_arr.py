from typing import List

# * https://leetcode.com/problems/merge-sorted-array/


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
        k -= 1

    while i >= 0:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1


num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 5, 6]
merge(num1, 3, num2, 3)
print(num1)  # [1,2,2,3,5,6]

num1 = [1]
num2 = []
merge(num1, 1, num2, 0)
print(num1)  # [1]

num1 = [0]
num2 = [1]
merge(num1, 0, num2, 1)
print(num1)  # [1]