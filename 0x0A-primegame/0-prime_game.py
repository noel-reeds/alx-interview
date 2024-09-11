#!/usr/bin/python3
"""prime game module"""


def sieve_of_eratosthenes(num):
    """returns prime_nums"""
    if num < 2:
        return []
    prime = [True] * (num + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(num ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, num + 1, i):
                prime[j] = False

    return prime


def game(n, prime_nums):
    """determines winner"""
    prime_numbers = [num for num in range(n + 1) if prime_nums[num]]
    turn = 0

    while prime_numbers:
        chosen = prime_numbers.pop(0)
        prime_numbers = [m for m in prime_numbers if m % chosen != 0]
        turn = 1 - turn

    return "Ben" if turn == 0 else "Maria"


def isWinner(x, nums):
    """returns winner"""
    if x == 0 or not nums:
        return None
    num = max(nums) if nums else 0
    if num < 2:
        return None
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
