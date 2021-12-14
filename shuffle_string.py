from typing import List

# * https://leetcode.com/problems/shuffle-string/


def restore_string(s: str, indices: List[int]) -> str:
    result = []
    s_str = list(s)
    for i in range(len(indices)):
        index = indices.index(i)
        result.append(s_str[index])

    return ''.join(result)


print(restore_string(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))  # "leetcode"
print(restore_string(s="abc", indices=[0, 1, 2]))  # "abc"
print(restore_string(s="aiohn", indices=[3, 1, 4, 2, 0]))  # "nihao"
print(restore_string(s="aaiougrt", indices=[4, 0, 2, 6, 7, 3, 1, 5]))  # "arigatou"
print(restore_string(s="art", indices=[1, 0, 2]))  # "rat"
