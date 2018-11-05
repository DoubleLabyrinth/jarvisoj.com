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

p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239
n = p * q

def Encrypt(m, n):
    return pow(m, 2, n)

def Decrypt(c, p, q, n):
    assert(p % 4 == 3)
    assert(q % 4 == 3)
    assert(p * q == n)

    r = pow(c, (p + 1) // 4, p)
    s = pow(c, (q + 1) // 4, q)
    g, a, b = xgcd(p, q)
    x = (a * p * s + b * q * r) % n
    y = (a * p * s - b * q * r) % n

    m1 = x
    m2 = n - x
    m3 = y
    m4 = n - y
    return m1, m2, m3, m4

def IntToBytes(x : int, order = 'big'):
    if x >= 0:
        return x.to_bytes((x.bit_length() + 7) // 8, order)
    else:
        ret = (1 << ((x.bit_length() + 7) // 8 * 8)) + x
        return IntToBytes(ret, order)

with open('flag.enc', 'rb') as f:
    c = int.from_bytes(f.read(), 'big')
    m1, m2, m3, m4 = Decrypt(c, p, q, n)
    print(IntToBytes(m1))
    print(IntToBytes(m2))
    print(IntToBytes(m3))
    print(IntToBytes(m4))
