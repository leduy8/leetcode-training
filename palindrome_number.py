
# * https://leetcode.com/problems/palindrome-number/

def isPalindrome(x: int) -> bool:
    if x < 0 or x > pow(2, 31) - 1:
        return False

    reversed_x_list = list(reversed(list(str(x))))
    reserved_x = ''.join(reversed_x_list)
    return int(reserved_x) == x

print(isPalindrome(121))
print(isPalindrome(13231))
print(isPalindrome(1313))
print(isPalindrome(-21212))
print(isPalindrome(-1421))
print(isPalindrome(1424112354621235))
