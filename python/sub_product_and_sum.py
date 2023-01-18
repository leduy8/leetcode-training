
# * https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

def subtractProductAndSum(n: int) -> int:
    product_digits = 1
    digits = [int(d) for d in str(n)]
    sum_digits = sum(digits)
    for digit in digits:
        product_digits *= digit
    return product_digits - sum_digits


print(subtractProductAndSum(n = 234)) # 15
print(subtractProductAndSum(n = 4421)) # 21