# * https://leetcode.com/problems/consecutive-characters/

def maxPower(s: str) -> int:
    if s is None:
        return -1

    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1

    prev = ''
    cur = s[0]
    powers = []
    cur_len = 1

    for c in s[1:]:
        prev = cur
        cur = c
        if prev == cur:
            cur_len += 1
        else:
            powers.append(cur_len)
            cur_len = 1

    powers.append(cur_len)

    return max(powers)


print(maxPower("leetcode"))
print(maxPower("abbcccddddeeeeedcba"))