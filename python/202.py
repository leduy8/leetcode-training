
# * https://leetcode.com/problems/happy-number/

def is_happy(n: int) -> bool:
    occurrence = {}
    sum = 0
    while True:
        for num in str(n):
            sum += pow(int(num), 2)
        if sum == 1:
            break
        if sum not in occurrence:
            occurrence[sum] = True
            n = sum
            sum = 0
        else:
            return False

    return True

print(is_happy(n=19)) # true
###
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
###

print(is_happy(n=2)) # false

print(is_happy(n=1111111))