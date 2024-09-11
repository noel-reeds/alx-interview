#!/usr/bin/python3
"""prime game module"""


def sieve_of_eratosthenes(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    return is_prime


def game(n, prime_nums):
    prime_numbers = [num for num in range(n + 1) if prime_nums[num]]
    turn = 0

    while prime_numbers:
        chosen = prime_numbers.pop(0)
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
