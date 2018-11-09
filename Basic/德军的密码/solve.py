#!/usr/bin/env python3

Table = { chr(ord('A') + i) : '{:07b}'.format(0b1000001 + i) for i in range(26) }
TableInv = { '{:07b}'.format(0b1000001 + i) : chr(ord('A') + i) for i in range(26) }

def Decrypt(s : str, key : str):
    assert(len(s) % 7 == 0)
    ret = bytearray([ int(s[i * 7:i * 7 + 7], 2) for i in range(len(s) // 7) ])
    key = bytes([ int(Table[key[i]], 2) for i in range(len(key)) ])
    for i in range(len(ret)):
        ret[i] ^= key[i % len(key)]
    ret = [ TableInv['{:07b}'.format(ret[i])] for i in range(len(ret)) ]
    return ''.join(ret)

def Encrypt(s : str, key : str):
    ret = bytearray([ int(Table[s[i]], 2) for i in range(len(s)) ])
    key = bytes([int(Table[key[i]], 2) for i in range(len(key))])
    for i in range(len(ret)):
        ret[i] ^= key[i % len(key)]
    ret = [TableInv['{:07b}'.format(ret[i])] for i in range(len(ret))]
    return ''.join(ret)

enc = '000000000000000000000000000000000000000000000000000101110000110001000000101000000001'
print(Decrypt(enc, 'WELCOMETOCFF'))
