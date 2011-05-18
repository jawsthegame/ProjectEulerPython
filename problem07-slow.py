__author__ = 'tfleischer'

import utils

def run():
    i = 1
    count = 0
    while count < 10091:
        i += 1
        if utils.is_prime(i):
            count += 1
    print i