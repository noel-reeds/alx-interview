#!/usr/bin/python3
"""prime game module"""


def sieve_of_eratosthenes(num):
    """returns name of the player that won the most rounds
    sieve prime numbers from the nums array."""
    if num < 2:
        return []

    prime_nums = [True for _ in range(num+1)]
    prime_nums[0] = prime_nums[1] = False

    m = 2
    while m * m <= num:
        n = m * m
        while n <= num:
            prime_nums[n] = False
            n += m
        m += 1
    prime = [x for x in range(2, num + 1) if prime_nums[x]]
    return prime


def game(n, prime_nums):
    prime_numbers = [num for num in range(n + 1) if prime_nums[num]]
    turn = 0

    while prime_numbers:
        chosen = prime_numbers.pop(0)
        print(f"Chosen prime: {chosen}")
        prime_numbers = [m for m in prime_numbers if m % chosen != 0]
        turn = 1 - turn

    return "Ben" if turn == 0 else "Maria"


def isWinner(x, nums):
    num = max(nums)
    prime_nums = sieve_of_eratosthenes(num)

    Maria = 0
    Ben = 0
    for m in nums:
        winner = game(m, prime_nums)
        if winner == "Maria":
            Maria += 1
        else:
            Ben += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
