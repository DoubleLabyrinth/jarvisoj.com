# jarvisoj.com -- CRYPTO -- Medium RSA

## Challenge

```
你没看错，这还真是密码学系列了，相信你已经解出前两题了，那么继续看这题吧。

mediumRSA.rar.07aab25c9c54464a8c9821ca28503330
```

## Solution

给了一个压缩包。里面有`pubkey.pem`和`flag.enc`。

那么打开`pubkey.pem`看看吧：

```
-----BEGIN PUBLIC KEY-----
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAMJjauXD2OQ/+5erCQKPGqxsC/bNPXDr
yigb/+l/vjDdAgMBAAE=
-----END PUBLIC KEY-----
```

很显然这个公钥太短了，

```
n = 87924348264132406875276140514499937145050893665602592992418171647042491658461
e = 65537
```

使用yafu可以分解n得到p、q。

```
PS C:\Users\DoubleSine\Tools\yafu-1.34> .\yafu-x64.exe
factor(87924348264132406875276140514499937145050893665602592992418171647042491658461)


fac: factoring 87924348264132406875276140514499937145050893665602592992418171647042491658461
fac: using pretesting plan: normal
fac: no tune info: using qs/gnfs crossover of 95 digits
div: primes less than 10000
fmt: 1000000 iterations
rho: x^2 + 3, starting 1000 iterations on C77
rho: x^2 + 2, starting 1000 iterations on C77
rho: x^2 + 1, starting 1000 iterations on C77
pm1: starting B1 = 150K, B2 = gmp-ecm default on C77
ecm: 30/30 curves on C77, B1=2K, B2=gmp-ecm default
ecm: 74/74 curves on C77, B1=11K, B2=gmp-ecm default
ecm: 149/149 curves on C77, B1=50K, B2=gmp-ecm default, ETA: 0 sec

starting SIQS on c77: 87924348264132406875276140514499937145050893665602592992418171647042491658461

==== sieving in progress (1 thread):   36224 relations needed ====
====           Press ctrl-c to abort and save state           ====
33056 rels found: 16939 full + 16117 from 182094 partial, (2561.49 rels/sec)

SIQS elapsed time = 83.6719 seconds.
Total factoring time = 96.0947 seconds


***factors found***

P39 = 319576316814478949870590164193048041239
P39 = 275127860351348928173285174381581152299

ans = 1
```

知道p、q之后就可以构造RSA私钥了。

```
$ ./RsaCtfTool.py --private -p 319576316814478949870590164193048041239 -q 275127860351348928173285174381581152299 -e 65537
-----BEGIN RSA PRIVATE KEY-----
MIGrAgEAAiEAwmNq5cPY5D/7l6sJAo8arGwL9s09cOvKKBv/6X++MN0CAwEAAQIg
GAZ5m9RM5kkSK3i0MGDHhvi3f7FZPghC2gY7oNhyi/ECEQDwbCjpHIkiucI24jVg
wJcXAhEAzvuyz34YqY6+3Dbj58OwKwIQaN4kshl6T6VK63mb4snenQIRAJulRkcl
qWIHx5pNZIAp9VUCEQCzufLwcMVFMaQ7MGqzqBUl
-----END RSA PRIVATE KEY-----
```

然后用openssl解密即可：

```
$ openssl rsautl -decrypt -in flag.enc -inkey prikey.pem
```
