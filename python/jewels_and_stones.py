
# * https://leetcode.com/problems/jewels-and-stones/


def num_jewels_in_stones(jewels: str, stones: str) -> int:
    jewels_in_stones = 0

    for jewel in jewels:
        for stone in stones:
            if jewel == stone:
                jewels_in_stones += 1
    
    return jewels_in_stones
    


print(num_jewels_in_stones(jewels='aA', stones='aAAbbbb')) # 3
print(num_jewels_in_stones(jewels='z', stones='ZZ')) # 0