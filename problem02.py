__author__ = 'tfleischer'

def run():
    a = 1
    b = 1
    sum = 0
    while a <= 4000000:
        if a % 2 == 0:
            sum += a
        temp = b
        b = a + b
        a = temp
    print sum