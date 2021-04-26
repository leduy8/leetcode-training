
# * https://leetcode.com/problems/water-bottles/

def numWaterBottles(num_bottles: int, num_exchange: int) -> int:
    full_bottles = num_bottles
    total_drank = num_bottles
    empty_bottles = full_bottles
    while(empty_bottles >= num_exchange):
        full_bottles = int(empty_bottles / num_exchange)
        total_drank += full_bottles
        empty_bottles = int(empty_bottles % num_exchange + full_bottles)
        
    return total_drank


print(numWaterBottles(num_bottles=9, num_exchange=3)) # ? Output: 13
print(numWaterBottles(num_bottles=15, num_exchange=4)) # ? Output: 19
print(numWaterBottles(num_bottles=5, num_exchange=5)) # ? Output: 6
print(numWaterBottles(num_bottles=2, num_exchange=3)) # ? Output: 2