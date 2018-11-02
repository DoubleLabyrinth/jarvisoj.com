#!/usr/bin/env python3

table = bytearray.fromhex('411011111b0a64676a6862686e67686b623d656a6a3d6804050803020255085d61550a5f0d5d6132171d191f1820040212161e54201314')

def Decode(ba, key):
    ret = bytearray()
    for i in range(len(ba)):
        ret.append(ba[i] - 2)
        ret[-1] ^= (key & 0xff)
        key += 1
    return bytes(ret[1:])

print(Decode(table, 73).decode())
