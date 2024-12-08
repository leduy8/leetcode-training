
# * https://leetcode.com/problems/split-a-string-in-balanced-strings/

def balanced_string_split(s: str) -> int:
    balanced_string = 0
    balance = 0
    for ch in s:
        balance = balance + 1 if ch == 'R' else balance - 1

        if balance == 0:
            balanced_string += 1

    return balanced_string


print(balanced_string_split('RLRRLLRLRL'))
print(balanced_string_split('RLLLLRRRLR'))
print(balanced_string_split('LLLLRRRR'))
print(balanced_string_split('RLRRRLLRLL'))
