from typing import List

# * https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ''

    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    
    return shortest


print(longestCommonPrefix(["flower","flow","flight"])) # 'fl'
print(longestCommonPrefix(["dog","racecar","car"])) # ''
print(longestCommonPrefix(["a"])) # 'a'
print(longestCommonPrefix(["flower","flower","flower"])) # 'flower'
print(longestCommonPrefix([])) # ''