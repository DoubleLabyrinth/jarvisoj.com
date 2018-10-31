# jarvisoj.com -- BASIC -- 手贱

## Challenge

```
某天A君的网站被日，管理员密码被改，死活登不上，去数据库一看，啥，这密码md5不是和原来一样吗？为啥登不上咧？

d78b6f302l25cdc811adfe8d4e7c9fd34

请提交PCTF{原来的管理员密码}
```

## Solution

```python
>> len('d78b6f302l25cdc811adfe8d4e7c9fd34')
33
```

显然多出了一个字符。

仔细看看，你会发现有一个`"l"`。

显然这不是md5字符串里会出现的字符；去掉它，然后在[https://www.cmd5.com/](https://www.cmd5.com/)里反查。

```
PCTF{hack}
```
