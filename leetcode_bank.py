
# * https://leetcode.com/problems/calculate-money-in-leetcode-bank/

def total_money_from_banking(n: int) -> int:
    total_money = 0
    weeks = int(n / 7)
    remaining_days = int(n % 7)
    money_from_monday = 1

    for _ in range(weeks):
        money_today = money_from_monday
        for _ in range(7):
            total_money += money_today
            money_today += 1
        money_from_monday += 1

    if remaining_days != 0:
        for _ in range(remaining_days):
            total_money += money_from_monday
            money_from_monday += 1

    return total_money


print(total_money_from_banking(4))
print(total_money_from_banking(10))
print(total_money_from_banking(20))
