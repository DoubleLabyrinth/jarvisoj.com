# jarvisoj.com -- CRYPTO -- BrokenPic

## Challenge

```
这里有个图片，可是好像打不开？

Hint1: 图片大小是1366*768

brokenpic.bmp.d82d5d25027ff5e9e3ae90022ec386f9
```

## Solution

下载附件 `brokenpic.bmp`，用010 Editor打开看看。你会观察到数据以16字节为一个周期循环。

```
0000h: D5 5F 7A B0 79 37 BA 26 B2 24 68 32 8A 68 C1 F2
0010h: D5 5F 7A B0 79 37 BA 26 B2 24 68 32 8A 68 C1 F2
0020h: D5 5F 7A B0 79 37 BA 26 B2 24 68 32 8A 68 C1 F2
0030h: D5 5F 7A B0 79 37 BA 26 B2 24 68 32 8A 68 C1 F2
0040h: D5 5F 7A B0 79 37 BA 26 B2 24 68 32 8A 68 C1 F2
0050h: D5 5F 7A B0 79 37 BA 26 B2 24 68 32 8A 68 C1 F2
0060h: D5 5F 7A B0 79 37 ...
```

既然题目提示图片大小为 `1366 * 768`，我们不妨用windows自带的画图生成一个相同大小的空白图片。然后将刚生成的图片丢到010 Editor看看：

```
0000h: 42 4D 36 0C 30 00 00 00 00 00 36 00 00 00 28 00
0010h: 00 00 56 05 00 00 00 03 00 00 01 00 18 00 00 00
0020h: 00 00 00 0C 30 00 00 00 00 00 00 00 00 00 00 00
0030h: 00 00 00 00 00 00 FF FF FF FF FF FF FF FF FF FF
0040h: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0050h: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0060h: FF FF FF FF FF FF FF ...
```

看样子破损的图片应该是缺了BMP文件头，我们不妨直接把新图片的BMP文件头插入到破损图片的开头试下。

你会发现破损的图片可以看了，似乎有密码，还有个二维码，但二维码不清楚，扫不了。

看样子应该要解密。从数据的高度重复性来看，应该使用的是ECB加密模式；至于是哪个算法，不妨先用AES试试。

```python3
#!/usr/bin/env python3
from Crypto.Cipher import AES

cipher = AES.new(b'PHRACK-BROKENPIC', AES.MODE_ECB)
with open('brokenpic.bmp', 'rb') as f:
    ciphertext = f.read()
    plaintext = cipher.decrypt(ciphertext)
    plaintext = bytes.fromhex('42 4D 36 0C 30 00 00 00 00 00 36 00 00 00 28 00 00 00 56 05 00 00 00 03 00 00 01 00 18 00 00 00 00 00 00 00 00 00 C4 0E 00 00 C4 0E 00 00 00 00 00 00 00 00 00 00') + plaintext
    with open('brokenpic_dec.bmp', 'wb') as f:
        f.write(plaintext)
```

解密后你就可以看到flag。
