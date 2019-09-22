# jarvisoj.com -- REVERSE -- [61dctf]androideasy

## Challenge

```
androideasy.apk.17e528e9498d4ae25dc82ad43730a03d
```

## Solution

下载下来是一个apk文件。装到手机里打开，就是一个文本框+check按钮。

随便输入什么，然后点check。会有一个 `Sorry your flag is wrong` 的提示。

既然知道了有这么一个字符串，那就解压apk，把 `classes.dex` 丢到IDA里看一番。先找到字符串 `Sorry your flag is wrong`，然后通过Xref找到引用该字符串的代码。发现是在 `com.a.sample.androidtest.MainActivity$1.onClick` 里。

既然知道在哪了，把 `classes.dex` 丢给 `d2j-dex2jar.bat`、转化成`classes-dex2jar.jar`，然后再用 [cfr](http://www.benf.org/other/cfr/) 转化成可阅读的java代码。

```console
$ java -jar .\cfr-0.146.jar .\androideasy\classes-dex2jar.jar > code.txt
```

在 `code.txt` 里搜索 `public class MainActivity` 就可以看到相关代码了。重点是 `MainActivity` 的 `check` 函数：

```java
private byte[] s = new byte[]{113, 123, 118, 112, 108, 94, 99, 72, 38, 68, 72, 87, 89, 72, 36, 118, 100, 78, 72, 87, 121, 83, 101, 39, 62, 94, 62, 38, 107, 115, 106};

public boolean check() {
    boolean bl = false;
    byte[] arrby = this.editText.getText().toString().getBytes();
    if (arrby.length != this.s.length) {
        return bl;
    }
    int n = 0;
    while (n < this.s.length) {
        if (n >= arrby.length) return true;
        boolean bl2 = bl;
        if (this.s[n] != (arrby[n] ^ 0x17)) return bl2;
        ++n;
    }
    return true;
}
```

可以看到是一个经典的XOR加密，密钥只有一个字节 `0x17`，解密即可得到flag。

