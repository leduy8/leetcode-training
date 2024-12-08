
# * https://leetcode.com/problems/valid-anagram/description/


def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


print(isAnagram(s = "anagram", t = "nagaram")) # True
print(isAnagram(s = "rat", t = "car")) # False