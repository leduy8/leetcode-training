# * https://leetcode.com/problems/neighboring-bitwise-xor/

from typing import List


def doesValidArrayExist(derived: List[int]) -> bool:
    # Because
    # A ^ B = C
    # A ^ C = B
    # B ^ C = A
    # Assume first item is 0
    derivedXOR = 0
    
    for bit in derived:
        derivedXOR = derivedXOR ^ bit
    
    # Expect last item is also 0 (0 ^ 0 = last derived item (either 0 or 1 still valid) )
    return derivedXOR == 0


print(doesValidArrayExist(derived=[1,1,0]))  # True
print(doesValidArrayExist(derived=[1,1]))  # True
print(doesValidArrayExist(derived=[1,0]))  # False
print(doesValidArrayExist(derived=[0,1,0,0,0]))  # False
print(doesValidArrayExist(derived=[0,1,0,1,0,1,1]))  # True