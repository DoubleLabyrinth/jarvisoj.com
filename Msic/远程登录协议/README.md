# jarvisoj.com -- MISC -- 远程登录协议

## Challenge

```
分析压缩包中的数据包文件并获取flag。flag为32位小写md5。

题目来源：CFF2016

telnet.rar.e7dedd279f225957aad6dc69e874eaae
```

## Solution

下载文件，压缩包里是一个pcapng文件，用wireshark打开即可。

既然压缩包名是telnet，那么重点关注TELNET协议。

Telnet协议是明文协议，在wireshark过滤掉除TELNET以外的协议，然后Follow TCP Stream就可以看到数据流。浏览一下你就可以看到

```
sshd:x:74:
apache:x:48:
mysql:x:27:
ira:x:500:
.]0;ira@localhost:~.[ira@localhost ~]$ cat /etc/noobflag.txt 
{FLAG:f69dd04e38ef85e38b2f148475ce32bc}
.]0;ira@localhost:~.[ira@localhost ~]$ ping 10.10.10.10
PING 10.10.10.10 (10.10.10.10) 56(84) bytes of data.
64 bytes from 10.10.10.10: icmp_seq=1 ttl=64 time=1.16 ms
```

注：

这个数据包里还有其他三个flag，当然都不是答案。
