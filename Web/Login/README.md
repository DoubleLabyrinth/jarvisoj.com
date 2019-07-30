# jarvisoj.com -- WEB -- Login

## Challenge

```
需要密码才能获得flag哦。

题目链接：http://web.jarvisoj.com:32772/
```

## Solution

打开网页，要求输入密码。不妨随便敲一个，但是注意打开浏览器的调试控制台，以便查看http报文的情况。

在response中给了一个提示：

```
Hint: "select * from `admin` where password='".md5($pass,true)."'"
```

这就很显然是一个sql注入漏洞了，只要 `md5($pass,true)` 以 `"or "` 打头，就可以泄漏出某些东西。

当然你可以暴力搜索，但是我们不必花时间。因为有一个现成的 `ffifdyop`。

输入后即可看到flag。
