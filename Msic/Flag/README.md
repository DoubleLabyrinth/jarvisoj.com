# jarvisoj.com -- MISC -- Flag

## Challenge

```
就给了一张图片
```

## Solution

既然就给了一张图片，那么基本上就是隐写术了。

用 `StegSolve 1.3 by Caesum` 打开图片。__Analyse -> Data Extract__，勾上RGB的第0位，然后点击Preview就可以看到PK头。

所以图片是储存了一个ZIP压缩包的，提取出来。

结果压缩包损坏。用WinRAR就可以修复。

解压后是一个64位elf文件，运行即可得到flag。

