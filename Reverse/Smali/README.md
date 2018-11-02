# jarvisoj.com -- REVERSE -- Smali

## Challenge

```
都说学好Smali是学习Android逆向的基础，现在刚好有一个smali文件，大家一起分析一下吧~~

Crackme.smali.36e0f9d764bb17e86d3d0acd49786a18
```

## Solution

下载文件，并用文本编辑器打开。

虽然看不懂Smali文件，但是开头有两个字符串很值得注意：

```
cGhyYWNrICBjdGYgMjAxNg==
sSNnx1UKbYrA1+MOrdtDTA==
```

经过base64解码之后，第一个是标准的文本：

```
phrack  ctf 2016
```

第二个是二进制数据。

继续看Smali文件，你可以看到似乎有一个`decrypt`函数，然后里面有`AES/ECB/NoPadding`字样。那么我们可以大胆猜测：

1. 第一个base64字符串解码后应该是AES加密的Key，而且解码后刚好是16字节，可以作为AES-128算法的Key。

2. 第二个base64字符串解码后应该是密文，解码后的长度也是16字节，刚好一个block的大小。

所以试试看吧：

```python
#!/usr/bin/env python3
import base64
from Crypto.Cipher import AES

pkcs7_padding = lambda msg, block_size: msg + bytes([block_size - len(msg) % block_size]) * (block_size - len(msg) % block_size)
pkcs7_unpadding = lambda msg: msg[0:-msg[-1]]

cipher = AES.new(b'phrack  ctf 2016', AES.MODE_ECB)
ciphertext = base64.b64decode('sSNnx1UKbYrA1+MOrdtDTA==')
plaintext = cipher.decrypt(ciphertext)
print(plaintext.decode())
```

解密出来的明文刚好是flag。
