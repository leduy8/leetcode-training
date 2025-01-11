# * https://leetcode.com/problems/score-of-a-string/description/


def scoreOfString(s: str) -> int:
    res = 0

    for i in range(len(s)-1):
        res += abs(ord(s[i]) - ord(s[i+1]))

    return res


print(scoreOfString(s="hello"))  # 13
print(scoreOfString(s="zaz"))  # 50
