# jarvisoj.com -- CRYPTO -- 神秘的压缩包

## Challenge

```
就不告诉你密码，看你怎么办。

注：题目来源XUSTCTF2016

flag.rar.2284020e9e3dd220ead6295f7996ee68
```

## Solution

下载文件，是一个加密的RAR压缩包。里面有`1.txt`、`2.txt`……`6.txt`和`flag.txt`。

值得注意的是它们的CRC32值是给定的，并且`1.txt`、`2.txt`……`6.txt`的文件大小仅仅5个字节。这样直接用hashcat爆破即可。

1. 构造文件`crc32.txt`，以当做hashcat的输入

   ```
   20AE9F17:00000000
   D2D0067E:00000000
   6C53518D:00000000
   80DF4DC3:00000000
   3F637A50:00000000
   BCD9703B:00000000
   ```

2. 使用hashcat爆破

   这里需要加上`--keep-guessing`参数，因为一个CRC32值可能对应到多个结果。

   ```
   $ hashcat64.exe -m 11500 -a 3 --keep-guessing crc32.txt ?a?a?a?a?a
   ...
   ...

   6c53518d:00000000:~Z-;l
   3f637a50:00000000:a-|23
   20ae9f17:00000000:passw
   20ae9f17:00000000:l./rc
   6c53518d:00000000:CKaS4
   d2d0067e:00000000:s=8;r
   bcd9703b:00000000:hyAo5
   d2d0067e:00000000:$HEX[6f72643a66]
   d2d0067e:00000000:"_YWn
   6c53518d:00000000:/8LWp
   80df4dc3:00000000:apEwF
   3f637a50:00000000:\<0Zk
   d2d0067e:00000000:N,tS*
   3f637a50:00000000:}b 3'
   d2d0067e:00000000:Rc(R>

   ...
   ...
   ```

整理一下应该可以得到

```
20ae9f17:00000000:passw
20ae9f17:00000000:l./rc

d2d0067e:00000000:s=8;r
d2d0067e:00000000:ord:f
d2d0067e:00000000:"_YWn
d2d0067e:00000000:N,tS*
d2d0067e:00000000:Rc(R>

6c53518d:00000000:CKaS4
6c53518d:00000000:/8LWp
6c53518d:00000000:~Z-;l

80df4dc3:00000000:apEwF

3f637a50:00000000:\<0Zk
3f637a50:00000000:}b 3'
3f637a50:00000000:a-|23

bcd9703b:00000000:hyAo5
```

最有可能的几个明文应该是

```
password:fCKaS4apEwF\<0ZkhyAo5
password:fCKaS4apEwF}b 3'hyAo5
password:fCKaS4apEwFa-|23hyAo5
password:f/8LWpapEwF\<0ZkhyAo5
password:f/8LWpapEwF}b 3'hyAo5
password:f/8LWpapEwFa-|23hyAo5
password:f~Z-;lapEwF\<0ZkhyAo5
password:f~Z-;lapEwF}b 3'hyAo5
password:f~Z-;lapEwFa-|23hyAo5
```

一个一个测试，最后密码是`f~Z-;lapEwF\<0ZkhyAo5`。

解压，得到flag。

