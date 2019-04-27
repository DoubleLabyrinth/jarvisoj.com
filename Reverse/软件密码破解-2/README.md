# jarvisoj.com -- REVERSE -- 软件密码破解-2

## Challenge

```
对压缩包中的程序进行分析并获取flag。flag形式为16位大写md5。

题目来源：CFF2016

CTF_100_1.rar.aa33faecac5307c4b1021a072e90e1d3
```

## Solution

```python
#!/usr/bin/env python3

def SubstractOne(bs : bytes):
    return bytes([ b - 1 for b in bs ])

def XorBytes(a, b):
    return bytes([ i ^ j for i, j in zip(a, b) ])

ct = int(0x2B5C5C25).to_bytes(4, 'little') + \
     int(0x36195D2F).to_bytes(4, 'little') + \
     int(0x7672642C).to_bytes(4, 'little') + \
     int(0x524E6680).to_bytes(4, 'little')

print(XorBytes(SubstractOne(ct), b'Welcome to CFF test!'[1:]).decode())
```

