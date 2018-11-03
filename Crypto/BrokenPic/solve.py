#!/usr/bin/env python3
from Crypto.Cipher import AES

cipher = AES.new(b'PHRACK-BROKENPIC', AES.MODE_ECB)
with open('brokenpic.bmp', 'rb') as f:
    ciphertext = f.read()
    plaintext = cipher.decrypt(ciphertext)
    plaintext = bytes.fromhex('42 4D 36 0C 30 00 00 00 00 00 36 00 00 00 28 00 00 00 56 05 00 00 00 03 00 00 01 00 18 00 00 00 00 00 00 00 00 00 C4 0E 00 00 C4 0E 00 00 00 00 00 00 00 00 00 00') + plaintext
    with open('brokenpic_dec.bmp', 'wb') as f:
        f.write(plaintext)

