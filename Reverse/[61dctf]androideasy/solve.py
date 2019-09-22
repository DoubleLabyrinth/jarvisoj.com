#!/usr/bin/env python3

def XorBytes(a: bytes, b: bytes):
    return bytes([ x ^ y for x, y in zip(a, b) ])

s = bytes([113, 123, 118, 112, 108, 94, 99, 72, 38, 68, 72, 87, 89, 72, 36, 118, 100, 78, 72, 87, 121, 83, 101, 39, 62, 94, 62, 38, 107, 115, 106])
key = bytes([0x17] * len(s))

print(XorBytes(s, key))
