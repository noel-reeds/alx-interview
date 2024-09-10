#!/usr/bin/python3
"""prime game module"""


def isWinner(nums):
    """returns name of the player that won the most rounds
    sieve prime numbers from the nums array."""
    num = len(nums)
    prime_nums = [True for _ in range(num+1)]
    m = 2
    while m * m <= num:
        n = m * m
        while n <= num:
            prime_nums[n] = False
            n += m
        m += 1
    var = 2
    prime = []
    while var <= num:
        if prime_nums[var]:
            prime.append(var)
        var += 1
    return prime
