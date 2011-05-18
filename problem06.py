__author__ = 'tfleischer'

def run():
    max_n = 100
    sum_of_squares = sum([x**2 for x in range(1, max_n + 1)])
    square_of_sums = sum([x for x in range(1, max_n + 1)])**2
    print square_of_sums - sum_of_squares