#!/usr/bin/env python3
import random

# See http://people.csail.mit.edu/jaffer/III/EZFPRW
def mant_exp_to_float(mant, point):
    if point >= 0:
        return float(mant * 10**point)
    return mant / 10**-point

def random_decimal():
    digits = ''.join(random.choice('0123456789') for _ in range(17))
    exponent = random.randrange(-324, 308)
    as_string = "{}e{}".format(digits, exponent)
    f = float(as_string)
    p = mant_exp_to_float(int(digits), exponent)
    return as_string, f, p, f == p

def main():
    print(random_decimal())

if __name__ == '__main__':
    main()
