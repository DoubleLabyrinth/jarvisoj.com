# jarvisoj.com -- BASIC -- Help!!

## Challenge

```
出题人硬盘上找到一个神秘的压缩包，里面有个word文档，可是好像加密了呢~让我们一起分析一下吧！

word.zip.a5465b18cb5d7d617c861dee463fe58b
```

## Solution

`word.zip` 是一个虚假加密的ZIP压缩包。你只需要移除掉压缩包中文件的Encryption Flag就可以解压文件。

解压之后你会得到`word.docx`，但打开之后没有flag。

但是将`word.docx`当做zip解压之后，在`word\media`下就可以看到flag了。

