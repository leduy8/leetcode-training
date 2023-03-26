from collections import defaultdict

# * https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    longest_substr = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_map and char_map[char] >= start:
            longest_substr = max(longest_substr, i - start)
            start = char_map[char] + 1

        char_map[char] = i
    
    return max(longest_substr, len(s) - start)


print(lengthOfLongestSubstring(s = "abcabcbb")) # 3
print(lengthOfLongestSubstring(s = "bbbbb")) # 1
print(lengthOfLongestSubstring(s = "pwwkew")) # 3
print(lengthOfLongestSubstring(s = " ")) # 1
print(lengthOfLongestSubstring(s = "c")) # 1
print(lengthOfLongestSubstring(s = "au")) # 2
print(lengthOfLongestSubstring(s = "dvdf")) # 3