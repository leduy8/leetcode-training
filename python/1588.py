from typing import List

# ? Guide: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/1222855/44ms-Python-(with-comments-and-detailed-walkthrough)

# * https://leetcode.com/problems/sum-of-all-odd-length-subarrays/


def sum_odd_length_subarrays(arr: List[int]) -> int:
    res = sum(arr)
    length = len(arr)

    for j in range(3, length + 1, 2):
        for i in range(length):
            if i + j > length:
                break

            res += sum(arr[i: i+j])

    return res


print(sum_odd_length_subarrays(arr=[1, 4, 2, 5, 3]))  # 58
print(sum_odd_length_subarrays(arr=[1, 2]))  # 3
print(sum_odd_length_subarrays(arr=[10, 11, 12]))  # 66
