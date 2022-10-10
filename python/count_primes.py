
# * https://leetcode.com/problems/count-primes/


def count_primes(limit: int) -> int:
    if limit <= 2:
        return 0
    elif limit == 3:
        return 1
    elif limit == 4:
        return 2

    count = 2

    for i in range(4, limit):
        if is_prime(i):
            count += 1

    return count


def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


print(count_primes(1))
