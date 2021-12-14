from typing import List

# * https://leetcode.com/problems/final-value-of-variable-after-performing-operations/


def final_values_after_operations(operations: List[str]) -> int:
    result = 0
    for operation in operations:
        result = result + 1 if operation[1] == "+" else result - 1

    return result


print(final_values_after_operations(operations=["--X", "X++", "X++"]))  # 1
print(final_values_after_operations(operations=["++X", "++X", "X++"]))  # 3
print(final_values_after_operations(operations=["X++", "++X", "--X", "X--"]))  # 0
