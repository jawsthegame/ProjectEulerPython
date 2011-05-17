__author__ = 'tfleischer'

import utils
import math

def run():
    n = 600851475143
    max_factor = int(math.sqrt(n))
    primes = utils.get_primes(max_factor)
    primes.reverse()
    for p in primes:
        if n % p == 0:
            print p
            break