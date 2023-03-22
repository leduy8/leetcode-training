from typing import List

# * https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = {}
    res = []

    for string in strs:
        sorted_str = "".join(sorted(string))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(string)
        else:
            anagrams[sorted_str] = [string]

    for item in anagrams.values():
        res.append(item)

    return res


print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams(strs = [""])) # [[""]]
print(groupAnagrams(strs = ["a"])) # [["a"]]