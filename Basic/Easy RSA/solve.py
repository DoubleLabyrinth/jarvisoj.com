#!/usr/bin/env python3
from sympy import *

# from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
# return (g, x, y) where g = gcd(a, b) and g == a * x + b * y
def xgcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

enc = 0xdc2eeeb2782c
n = 322831561921859
e = 23
p, q = factorint(n).keys()
phi = (p - 1) * (q - 1)
g, d, k = xgcd(e, phi)
assert(g == 1)
while d < 0:
    d += phi
msg = pow(enc, d, n)
msg = msg.to_bytes((msg.bit_length() + 7) // 8, 'big')

print('p = %d' % p)
print('q = %d' % q)
print('d = %d' % d)
print('msg =', msg)
print('flag = PCTF{%s}' % msg.decode())
