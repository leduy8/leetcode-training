
# * https://leetcode.com/problems/reverse-integer/

def reverse(x: int) -> int:
    is_negative = False
    if x < 0:
        x *= -1
        is_negative = True
    int_as_arr = [d for d in str(x)]
    int_as_arr.reverse()
    res = int(''.join(int_as_arr))
    if res > pow(2, 31):
        return 0
    return res*-1 if is_negative else res

print(reverse(x=123))
print(reverse(x=-123))
print(reverse(x=120))
print(reverse(x=0))
print(reverse(x=1534236469))