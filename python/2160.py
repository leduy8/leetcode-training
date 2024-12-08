
# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

def minimumSum(num: int) -> int:
    s = sorted(str(num))
    s1 = s[0] + s[2]
    s2 = s[1] + s[3]
    return int(s1) + int(s2)


print(minimumSum(2932)) # 52
print(minimumSum(4009)) # 13