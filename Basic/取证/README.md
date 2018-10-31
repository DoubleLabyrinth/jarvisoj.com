# jarvisoj.com -- BASIC -- 取证

## Challenge

```
有一款取证神器如下图所示，可以从内存dump里分析出TureCrypt的密钥，你能找出这款软件的名字吗？名称请全部小写。

提交格式：PCTF{软件名字}
```

![](https://dn.jarvisoj.com/umeditor/20160608/28601465358215259.JPG)

## Solution

在Bing里搜索`"TureCrypt memory dump key"`；然后在一个[reddit论坛](https://www.reddit.com/r/computerforensics/comments/3c3fh1/helpextracting_encryption_keys_from_a_memory_dump/)里你就会知道是什么软件了。

```
PCTF{volatility}
```
