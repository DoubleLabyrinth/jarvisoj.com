#!/usr/bin/env python3

ciphertext = b'jeihjiiklwjnk{ljj{kflghhj{ilk{k{kij{ihlgkfkhkwhhjgly'

def Encrypt(bs):
    ret = bytearray()
    for i in bs:
        if 47 < i and i <= 96:
            i += 53
        elif i <= 46:
            i += i % 11
        else:
            i = i // 61 * 61
        ret.append(i)
    return bytes(ret)

DecryptTable = Encrypt(bytes([i for i in range(0, 128)]))
plaintext = bytearray()
for i in ciphertext:
    plaintext.append(DecryptTable.find(bytes([i])))
plaintext = bytes(plaintext)
print(bytes.fromhex(plaintext.decode()).decode())
