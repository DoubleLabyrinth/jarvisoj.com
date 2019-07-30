# jarvisoj.com -- WEB -- LOCALHOST

## Challenge

```
题目入口：http://web.jarvisoj.com:32774/
```

## Solution

打开网页，提示只能本地访问。这里只要构造 `X-FORWARDED-FOR` 项即可骗过网站。

```console
$ curl --header "X-FORWARDED-FOR: 127.0.0.1" http://web.jarvisoj.com:32774/
```

