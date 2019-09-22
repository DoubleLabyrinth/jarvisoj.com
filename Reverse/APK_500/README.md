# jarvisoj.com -- REVERSE -- APK_500

## Challenge

```
本题必须在Android 4.3（API 18）及以下版本中运行和调试！否则将产生错误答案！

题目来源:CFF2016

CTF_500.apk.42abf30bd74ece3342e3617ccea694f8
```

## Solution

```python
def XorBytes(a: bytes, b: bytes):
    return bytes([ x ^ y for x, y in zip(a, b)])

key = bytes.fromhex('858bec836c9c838d0c01755fc645f350')
c =   bytes.fromhex('ddedd4ea02e7bef168491a6cae2bc660')
m = XorBytes(c, key)
m = m[-7:] + m[0:-7]
m = bytes([ m[i] - 1 if i < 4 else m[i] for i in range(len(m)) ])
m = XorBytes(m, bytes([ i for i in range(16) ]))
print('%s' % m.decode())
```

