# jarvisoj.com -- CRYPTO -- 好多盐

## Challenge

```
某遗留系统采用固定格式+6-10位数字类型密码，今天他们发生了数据泄露事件，已知固定格式为{FLAG:}，做为一名黑客，你要开始干活了。字符串长度为10位

题目来源：CFF2016

password.rar.df9dd18a22b5ae9f31dd2b190e21306e
```

## Solution

下载附件，打开来看看：

```
f09ebdb2bb9f5eb4fbd12aad96e1e929 p5Zg6LtD
6cea25448314ddb70d98708553fc0928 ZwbWnG0j
2629906b029983a7c524114c2dd9cc36 1JE25XOn
2e854eb55586dc58e6758cfed62dd865 ICKTxe5j
7b073411ee21fcaf177972c1a644f403 0wdRCo1W
...
...
```

可以看到一堆的hash和salt。这个时候hashcat就派上用场了：

保留其中一个条目，然后

```
$ hashcat64.exe -a 3 -m 10 -p " " -o password.crack password {FLAG:?d?d?d?d?d?d?d?d?d?d}
```

10秒就可以破解，flag会在 `password.crack` 文件中。

