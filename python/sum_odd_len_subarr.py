from typing import List

# * https://leetcode.com/problems/sum-of-all-odd-length-subarrays/


def sum_odd_length_subarrays(arr: List[int]) -> int:
    res = 0
    i = 0
    j = i

    for num in arr:
        res += num

        print('outer', res)
        while True:
            i += 1
            j = i + 2
            print(j, len(arr))
            if j < len(arr):
                print(arr[i:j])
                res += sum(arr[i:j])
            else:
                break
            print('inner', res)

        j = i

    return res


# print(sum_odd_length_subarrays(arr=[1, 4, 2, 5, 3]))  # 58
# print(sum_odd_length_subarrays(arr=[1, 2]))  # 3
print(sum_odd_length_subarrays(arr=[10, 11, 12]))  # 66
