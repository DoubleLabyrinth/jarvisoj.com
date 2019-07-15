#!/usr/bin/env python3

def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

plaintext = b'TWCTF{*******CENSORED********}'
ciphertext = bytes.fromhex('805eed80cbbccb94c36413275780ec94a857dfec8da8ca94a8c313a8ccf9')
assert(len(plaintext) == len(ciphertext))
indexes_of_known_chars = (0, 1, 2, 3, 4, 5, len(plaintext) - 1)
possible_keys = []
for a in range(0, 251):
    for b in range(0, 251):
        ok = True
        for i in indexes_of_known_chars:
            if (a * plaintext[i] + b) % 251 != ciphertext[i]:
                ok = False
                break
        if ok:
            possible_keys.append((a, b))
        
assert(len(possible_keys) != 0)

for a, b in possible_keys:
    g, a_inv, _ = xgcd(a, 251)
    assert(g == 1)
    if a_inv < 0:
        a_inv += 251
    m = bytes([ (((ciphertext[i] - b) % 251) * a_inv) % 251 for i in range(len(ciphertext)) ])
    print(m.decode())
