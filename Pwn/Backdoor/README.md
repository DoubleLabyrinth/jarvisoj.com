# jarvisoj.com -- CRYPTO -- Backdoor

## Challenge

```
这是一个有后门的程序，有个参数可以触发该程序执行后门操作，请找到这个参数，并提交其SHA256摘要。(小写)

FLAG：PCTF{参数的sha256}

vulnerable.rar.10d720f2dcf2b4133ec512813d7b89ce
```

## Solution

下载文件，得到一个exe程序。

丢到IDA里看看。重点关注`wmain`和`sub_401000`这两个函数。

`wmain`主要是对一块区域填充了一定数量的`"A"`字符，然后写入了一个看样子像地址的DWORD——`0x7FFA4512`，之后又附加了0x1A个`"\x90`（汇编的nop，估计是slidecode），最后就是像shellcode的0x91字节。我们输入的参数会影响`"A"`字符的数目，可见我们要确定要填充多少个`"A"`。

`sub_401000`函数就是将上述说的区域复制到该函数的栈上。

`0x7FFA4512`是xp时代用于跳转的地址，这个地址对应的汇编是`jmp esp`。可见我们要让`sub_401000`返回时跳到这个地址上。

在`sub_401000`函数里填充0x24个`"A"`刚好能覆盖返回地址。所以我们可以确定需要的参数应该为`\x43\x64 ^ \x24\x00 = \x67\x64`，也就是`"gd"`。

所以flag就是：

```python
import hashlib
print('PCTF{%s}' % hashlib.sha256(b'gd').hexdigest())
```

注：

这个程序你想看到效果的话得到XP及XP以下的windows操作系统中才能看到，因为XP以上的操作系统默认都开启了ASLR，`0x7FFA4512`多半会是无效的地址。

