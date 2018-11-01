# jarvisoj.com -- CRYPTO -- Medium RSA

## Challenge

```
前几题因为N太小，都被你攻破了，出题人这次来了个RSA4096，是否接受挑战就看你了。

veryhardRSA.rar.2a89300bd46d028a14e2b5752733fe98
```

## Solution

给了一个压缩包。里面有三个文件：`flag.enc1`、`flag.enc2`、`veryhardRSA.py`。

`veryhardRSA.py`应该是加密代码，可以看到对于同一个模数`N`使用了不同的加密指数`e1`和`e2`：

```python
#!/usr/bin/env python

import random

N = 0x00b0bee5e3e9e5a7e8d00b493355c618fc8c7d7d03b82e409951c182f398dee3104580e7ba70d383ae5311475656e8a964d380cb157f48c951adfa65db0b122ca40e42fa709189b719a4f0d746e2f6069baf11cebd650f14b93c977352fd13b1eea6d6e1da775502abff89d3a8b3615fd0db49b88a976bc20568489284e181f6f11e270891c8ef80017bad238e363039a458470f1749101bc29949d3a4f4038d463938851579c7525a69984f15b5667f34209b70eb261136947fa123e549dfff00601883afd936fe411e006e4e93d1a00b0fea541bbfc8c5186cb6220503a94b2413110d640c77ea54ba3220fc8f4cc6ce77151e29b3e06578c478bd1bebe04589ef9a197f6f806db8b3ecd826cad24f5324ccdec6e8fead2c2150068602c8dcdc59402ccac9424b790048ccdd9327068095efa010b7f196c74ba8c37b128f9e1411751633f78b7b9e56f71f77a1b4daad3fc54b5e7ef935d9a72fb176759765522b4bbc02e314d5c06b64d5054b7b096c601236e6ccf45b5e611c805d335dbab0c35d226cc208d8ce4736ba39a0354426fae006c7fe52d5267dcfb9c3884f51fddfdf4a9794bcfe0e1557113749e6c8ef421dba263aff68739ce00ed80fd0022ef92d3488f76deb62bdef7bea6026f22a1d25aa2a92d124414a8021fe0c174b9803e6bb5fad75e186a946a17280770f1243f4387446ccceb2222a965cc30b3929L

def pad_even(x):
	return ('', '0')[len(x)%2] + x

e1 = 17
e2 = 65537


fi = open('flag.txt','rb')
fo1 = open('flag.enc1','wb')
fo2 = open('flag.enc2','wb')


data = fi.read()
fi.close()

while (len(data)<512-11):
	data  =  chr(random.randint(0,255))+data

data_num = int(data.encode('hex'),16)

encrypt1 = pow(data_num,e1,N)
encrypt2 = pow(data_num,e2,N)


fo1.write(pad_even(format(encrypt1,'x')).decode('hex'))
fo2.write(pad_even(format(encrypt2,'x')).decode('hex'))

fo1.close()
fo2.close()
```

很显然使用共模攻击就可以得到密文。

```python
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

def GetInverse(a, n):
    g, a_, k = xgcd(a, n)
    assert(g == 1)
    while a_ < 0:
        a_ += n
    return a_

n = 0x00b0bee5e3e9e5a7e8d00b493355c618fc8c7d7d03b82e409951c182f398dee3104580e7ba70d383ae5311475656e8a964d380cb157f48c951adfa65db0b122ca40e42fa709189b719a4f0d746e2f6069baf11cebd650f14b93c977352fd13b1eea6d6e1da775502abff89d3a8b3615fd0db49b88a976bc20568489284e181f6f11e270891c8ef80017bad238e363039a458470f1749101bc29949d3a4f4038d463938851579c7525a69984f15b5667f34209b70eb261136947fa123e549dfff00601883afd936fe411e006e4e93d1a00b0fea541bbfc8c5186cb6220503a94b2413110d640c77ea54ba3220fc8f4cc6ce77151e29b3e06578c478bd1bebe04589ef9a197f6f806db8b3ecd826cad24f5324ccdec6e8fead2c2150068602c8dcdc59402ccac9424b790048ccdd9327068095efa010b7f196c74ba8c37b128f9e1411751633f78b7b9e56f71f77a1b4daad3fc54b5e7ef935d9a72fb176759765522b4bbc02e314d5c06b64d5054b7b096c601236e6ccf45b5e611c805d335dbab0c35d226cc208d8ce4736ba39a0354426fae006c7fe52d5267dcfb9c3884f51fddfdf4a9794bcfe0e1557113749e6c8ef421dba263aff68739ce00ed80fd0022ef92d3488f76deb62bdef7bea6026f22a1d25aa2a92d124414a8021fe0c174b9803e6bb5fad75e186a946a17280770f1243f4387446ccceb2222a965cc30b3929
e1 = 17
e2 = 65537

g, k1, k2 = xgcd(e1, e2)
assert(g == 1)
c1 = int.from_bytes(open('flag.enc1', 'rb').read(), 'big')
c2 = int.from_bytes(open('flag.enc2', 'rb').read(), 'big')

if k1 > 0:
    m1 = pow(c1, k1, n)
else:
    m1 = pow(c1, -k1, n)
    m1 = GetInverse(m1, n)

if k2 > 0:
    m2 = pow(c2, k2, n)
else:
    m2 = pow(c2, -k2, n)
    m2 = GetInverse(m2, n)

m = (m1 * m2) % n
print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))
```
