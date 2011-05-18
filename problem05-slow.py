__author__ = 'tfleischer'

import utils

def run():
    num = 20
    max = utils.factorial(num)

    for x in xrange(num, max + 1):
        if not any([y for y in range(1, num + 1) if x % y != 0]):
            print x
            break