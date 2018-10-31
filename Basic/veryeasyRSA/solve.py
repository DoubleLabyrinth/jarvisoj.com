#!/usr/bin/env python3

# from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
# return (g, x, y) where g = gcd(a, b) and g == a * x + b * y
def xgcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

p = 3487583947589437589237958723892346254777
q = 8767867843568934765983476584376578389
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
g, d, k = xgcd(e, phi)
assert(g == 1)
while d < 0:
    d += phi

print('PCTF{%d}' % d)
