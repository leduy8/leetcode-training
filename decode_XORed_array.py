from typing import List

# * https://leetcode.com/problems/decode-xored-array/


def decode(encoded: List[int], first: int) -> List[int]:
    res = [first]
    prev = first
    for code in encoded:
        prev = code ^ prev
        res.append(prev)

    return res


print(decode(encoded=[1, 2, 3], first=1))  # [1,0,2,1]
print(decode(encoded=[6, 2, 7, 3], first=4))  # [4,2,0,7,4]
