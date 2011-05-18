__author__ = 'tfleischer'

def run():
    print sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0])