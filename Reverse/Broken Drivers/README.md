# jarvisoj.com -- REVERSE -- Broken Drivers

## Challenge

```
这是一个有问题的驱动程序，请尝试patch并获得flag

通过本题可以掌握驱动程序调试技术

360dst.sys.8a991f86ccd91b7c4d15e5b8912d3740
```

## Solution

```python
#!/usr/bin/env python3
from Crypto.Cipher import Blowfish
from Crypto.Hash import MD5

def XorBytes(a, b):
    return bytes([ i ^ j for i, j in zip(a, b) ])

iv0 = bytes.fromhex('a8d583f31b7ec36a')
iv1 = bytes.fromhex('7c9e2ac786b2ecf3')

key = bytearray.fromhex('3638d25c1a8874cd9832dc239b2635a662935639047f0a9ae59327b6d408e7fa2c9eaa43557637e66cc4881c47bf8a9705911c04f2fba769')
hint = MD5.new(int(360).to_bytes(4, 'little')).digest()
key[1] = hint[0]
key[2] = hint[1]
key[4] = hint[2]
key[7] = hint[3]
key[9] = hint[4]
key[10] = hint[5]
key[13] = hint[6]
key[15] = hint[7]
key[18] = hint[8]
key[21] = hint[9]
key[25] = hint[10]
key[27] = hint[11]
key[33] = hint[12]
key[39] = hint[13]
key[47] = hint[14]
key[52] = hint[15]

cipher = Blowfish.new(key, Blowfish.MODE_ECB)
ciphertext = bytes.fromhex('cab7f13c5d24bca6096b27fcea26c00490829b6d6cb0949d8905e67195479b2e449497aff54e348c2a585ad5f340640c9cd36bc2a2db1781571c718e4fa06e9b702fc8bd443290f37cb03f4658d4770a9c0fadc42dec2c95c91f8af22f6a3f5812ac207aec61685c86759274cdd27515879eba776bcb7d415a3bde4e08cb2e423cf4e83ca7b3592141c836d93f75d5837b468a929e5bca7b32cd60298dbc0b30368d8f96659eead0ce782f2b8123b0c06764b6e5a99f3b3f20384cc074b9c68a3a34c76eca4430754889ccb8ce51239d5c754953fdd48df46e0771067487bd97d42d84164cffbeda13ae1cb2f757ad6e31aa97a2c924f784d78de3b431d5a81f')
plaintext = b''

for i in range(0, len(ciphertext), 8):
    ct = XorBytes(ciphertext[i:i + 8], iv1)
    pt = cipher.decrypt(ct[0:4][::-1] + ct[4:8][::-1])
    pt = XorBytes(pt[0:4][::-1] + pt[4:8][::-1], iv0)
    plaintext += pt
    iv0 = ct

print(plaintext.rstrip(b'\x00').decode())
```

