# jarvisoj.com -- REVERSE -- 文件数据恢复

## Challenge

```
有个文件加密工具，能将一个文件加密到一个.ctf文件中去。

有一个犯罪分子将存有犯罪记录的一个名为“CTFtest.ctf”的加密文件被删除了。

现经过数据恢复，我们已经恢复了该文件。但是很不幸，该文件头部的部分数据已经被覆盖掉了。这个.ctf文件已经不能正常打开了。

而且加密该文件的口令，犯罪分子也不愿意交代，我们只知道他惯用的口令是一个8位纯数字口令。

请分析压缩包里的.ctf文件以及解密程序最大限度地恢复出文件中的内容，flag就在里面。Flag形式为大写32位md5。


题目来源：CFF2016

CTF_300_1.rar.da1592ea56e1512f71f301e96410d1fb
```

## Solution

```python
#!/usr/bin/env python3
import sys

def XorBytes(a, b):
    return bytes([ i ^ j for i, j in zip(a, b) ])

def UpdateKey(k):
    return bytes([ (b + 1) % 256 for b in k ])

def PreviousKey(k):
    return bytes([ (b - 1) % 256 for b in k ])

key = bytes.fromhex('17 86 02 4B E8 BD 92 DC 6C 00 A5 D9 4E 53 3A 06')
key = PreviousKey(key)
key = PreviousKey(key)
key = PreviousKey(key)
key = PreviousKey(key)

assert(len(sys.argv) == 3)

with open(sys.argv[1], 'rb') as f:
    ct = f.read()[0x2D:]

pt = b''
for i in range(0, len(ct), 16):
    pt += XorBytes(ct[i:i + 16], key)
    key = UpdateKey(key)

with open(sys.argv[2], 'wb') as f:
    f.write(pt)
```

用法：

```console
$ ./solve.py CTF_300_1.ctf CTF_300_1.ctf.docx
```

然后打开`CTF_300_1.ctf.docx`。

