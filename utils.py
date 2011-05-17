__author__ = 'tfleischer'

import math

def get_factors(n):
    max = int(math.sqrt(n))
    factors = []
    for x in range(1, max):
        if n % x == 0:
            factors.append(x)
            factors.append(n / x)
    factors.sort()
    return factors

def has_multiple_of_as_factor(a, b): return a != b and a % b == 0

def get_primes(n):
    primes = range(2, n)
    max_non_prime = int(math.sqrt(n))

    for p in range(2, max_non_prime):
        primes = filter(lambda x: x == p or x % p != 0, primes)

    return primes


def is_prime(n):
    for x in range(2, n - 1):
        if n % x == 0:
            return 0

    return n != 1
