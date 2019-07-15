# jarvisoj.com -- CRYPTO -- superexpress

## Challenge

```
题目来源：TWCTF2016

superexpress.7z.b25a070afa73bdb3a2e425f8a68498ee
```

## Solution

把附件下载下来，可以看到代码：

```python
import sys
key = '****CENSORED***************'
flag = 'TWCTF{*******CENSORED********}'

if len(key) % 2 == 1:
    print("Key Length Error")
    sys.exit(1)

n = len(key) / 2
encrypted = ''
for c in flag:
    c = ord(c)
    for a, b in zip(key[0:n], key[n:2*n]):
        c = (ord(a) * c + ord(b)) % 251
    encrypted += '%02x' % c

print encrypted
```

以及密文：

```
805eed80cbbccb94c36413275780ec94a857dfec8da8ca94a8c313a8ccf9
```

分析代码可以发现，采用的加密算法是有限域 `GF(251)` 上的多次线性变换。

多次线性变换只是唬人的，因为它们与单个线性变换等价，所以找到单个线性变换的系数就可以了。

遍历空间大小为 `251 * 251 = 63001`，这个很快就找得到。

