# jarvisoj.com -- MISC -- 简单网管协议

## Challenge

```
分析压缩包中的数据包文件并获取flag。flag为32位小写md5。

题目来源：CFF2016

simple_protocol.rar.57175cf6f8e21242822fb828735b4155
```

## Solution

既然是简单网管协议，那就是SNMP（Simple Network Management Protocol）。

用wireshark打开pcapng文件，过滤掉所有除snmp协议外的其他数据包，Follow UDP Stream，然后你就可以看到flag了。

```
02.....public.%.........0.0...+.........webshellhttp0&.....public...........0.0...+.........0p.....public.c.........0X0V..+........JUnknown (edit /etc/snmp/snmpd.conf/flag{077149a68b9d4f25f52bb11530f44028})0&.....public...........0.0...+.........0'.....public...........0.0
..+.......C..0&.....public...........0.0...+.........02.....public.%.........0.0..
+.....	....
```
