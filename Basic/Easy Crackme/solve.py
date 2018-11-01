#!/usr/bin/env python3
key = b'\xab\xdd\x33\x54\x35\xef'
ciphertext = bytes.fromhex('fb9e67124e9d98ab0006468af4b4060b43dcd9a46c31749cd2a0')

plaintext = bytearray()
for i in range(len(ciphertext)):
    plaintext.append(ciphertext[i] ^ key[i % len(key)])
print(plaintext.decode())
