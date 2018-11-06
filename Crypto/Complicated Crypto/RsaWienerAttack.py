#!/usr/bin/env python3
import sys
from Crypto.PublicKey import RSA

# from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
# return (g, x, y) where g = gcd(a, b) and g == a * x + b * y
def xgcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

# from https://stackoverflow.com/questions/15390807/integer-square-root-in-python
def IntegerSqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def GetContinuedFraction(e : int, n : int):
    ret = []
    while True:
        q, r = divmod(e, n)
        ret.append(q)
        if r == 0:
            break
        else:
            e, n = n, r
    return ret

def GetPQ(e, n, cfs : list):
    prev_k, prev_d = 1, 0
    k, d = cfs[0], 1

    for i in range(1, len(cfs)):
        tmp_k, tmp_d = cfs[i] * k + prev_k, cfs[i] * d + prev_d
        prev_k, prev_d = k, d
        k, d = tmp_k, tmp_d

        kphi = e * d - 1
        phi, r = divmod(kphi, k)
        if r == 0:
            delta = IntegerSqrt((n - phi + 1) ** 2 - 4 * n)
            p = (n - phi + 1 + delta) // 2
            q = (n - phi + 1 - delta) // 2
            if p * q == n:
                return p, q, d
    return 0, 0, 0

def help():
    print('Usage:')
    print('    RsaWienerAttack.py <n> <e>')
    print()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        help()
        exit(0)

    n = int(sys.argv[1])
    e = int(sys.argv[2])
    p, q, d = GetPQ(e, n, GetContinuedFraction(e, n))
    if p == 0 and q == 0 and d == 0:
        print('Failed!')
    else:
        phi = (p - 1) * (q - 1)
        print()
        print('p = %d' % p); print()
        print('q = %d' % q); print()
        print('phi = %d' % phi); print()
        print('d = %d' % d); print()
        print('e = %d' % e); print()
        print('n = %d' % n); print()

        key = RSA.construct((n, e, d, p, q))
        print(key.export_key().decode()); print()
else:
    print('Please run this python script in console.')
