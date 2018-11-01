# jarvisoj.com -- CRYPTO -- Tell Me Something

## Challenge

```
Do you have something to tell me?

nc pwn.jarvisoj.com 9876

guestbook.d3d5869bd6fb04dd35b29c67426c0f05
```

## Solution

下载文件，这是一个64位的ELF文件。

丢到IDA里反编译：`main`函数有栈溢出，`good_game`函数会打印出flag。

所以修改main的返回地址为`good_game`的地址即可。

