# jarvisoj.com -- WEB -- PORT51

## Challenge

```
题目链接：http://web.jarvisoj.com:32770/
```

## Solution

打开网页，提示用51端口访问。当然不是去访问网站的51端口，而是要在本地用51端口访问网站。

用curl就可以了：

```console
$ sudo curl --local-port 51 http://web.jarvisoj.com:32770/
```
