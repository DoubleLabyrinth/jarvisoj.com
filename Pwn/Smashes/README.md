# jarvisoj.com -- PWN -- Smashes

## Challenge

```
Smashes, try your best to smash!!!

nc pwn.jarvisoj.com 9877

smashes.44838f6edd4408a53feb2e2bbfe5b229
```

## Solution

下载文件，这是一个64位的ELF文件。

丢到IDA里反编译：`sub_4007E0`函数里有`gets`函数的调用，可以栈溢出。

栈溢出之后，`sub_4007E0`返回时会触发`___stack_chk_fail`，但是这个函数会打印出`argv[0]`地址指向的字符串，也就是程序的路径名。如果栈溢出覆盖了`argv[0]`的值，就可以实现任意地址读。

但是flag字符串会被`memset`给抹掉。不过不用担心，因为flag字符串在ELF文件里的偏移是`+0xD20`，还不到一个页，所以在`0x400000 + 0xD20 = 0x400D20`的地方还会有一份，读取这里就行了。

