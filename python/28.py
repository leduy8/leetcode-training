# * https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

def strStr(haystack: str, needle: str) -> int:
    try:
        return haystack.index(needle)
    except ValueError:
        return -1


print(strStr(haystack="sadbutsad", needle="sad"))  # 0
print(strStr(haystack="leetcode", needle="leeto"))  # -1
