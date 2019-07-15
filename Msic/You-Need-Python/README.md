# jarvisoj.com -- MISC -- You Need Python

## Challenge

```
人生苦短我用Python。

题目：you_need_python.zip.74d515955b9aa607b488a48437591a14
```

## Solution

下载附件，你会得到 `flag.py` 和 `key_is_here_but_do_you_know_rfc4042` 两个文件。

针对 `flag.py` 我们可以用 `uncompyle6` 还原成源代码：

```python
#!/usr/bin/env python2
import marshal, zlib, base64, uncompyle6

co = marshal.loads(zlib.decompress(base64.b64decode('eJxtVP9r21YQvyd/ieWm66Cd03QM1B8C3pggUuzYCSWstHSFQijyoJBhhGq9OXJl2ZFeqAMOK6Q/94f9Ofvn1s+d7Lgtk/3O997du/vc584a0eqpYP2GVfwDEeOrKCU6g2LRRyiK4oooFsVVUSqkqxTX6J1F+SfSNYrrdKPorC76luhbpOEGCZNFZw2KG3Rmk26QtuXi3xTb7ND6/aVu0g2RuvhEcZNut5lAGbTvAFbyH57TkYLKy8J6xpDvQxiiiaIlcdqJxVcHbXY6bXNlZgviPCrO0+StqfKd88gzNh/qRZyMdWHE29TZZvIkG7eZFRGGRcBmsXJaUoKCQ9fWKHwSqNeKFnsM5PnwJ7q2aKk4AFhcWtQCh+ChB5+Lu/RmyYUxmtOEYxas7i/2iuR7Ti14OEOSmU0RADd4+dQzbM1FJhukAUeQ+kZROuLyioagrau76kc1slY1NNaY/y3LAxDQBrAICJisV2hMdF2lxQcyFuMoqcX3+TCl6xotqzSpkqmxYVmjXVjAXiwBsEfBrd1VvTvLCj2EXRnhoryAKdpxcIgJcowUB68yAx/tlCAuPHqDuZo0CN3CUGHwkPhGMA7aXMfphjbmQLhLhJcHa0a+mpgB191c1U1lnHJQbgkHx+WGxeJbejnpkzSavo2jkxZ7i725npGAaTc8FXmUjbUETHUmkxXN5zqL5WiWxwE7Bc11yyYzNJpN02jerq+DzNNodfxOX8kE4FcmYKscDdYD1oPGGucXYNmgs1F+NTf3GOt3Mg7b+NTVruqoQyX1hOEUacKw+AGbP38ZOq9THRXaSbL5pXGQ8bho/Z/lrzQaHxdoCrlev+t6nZ7re57r+57rHXag93Deh37k+vuw9zorO/Qj/B50cAf2oyOsvut3D+ADWxdxfN/1Drqu39mHzvcRswv/Hvz7sHeg9w8Qzy99DzuFwxhPhs6zWTbOI3OZRiaZZcVj5wVwOklx7OwVxR47PR46r/SVM8ulBJic9zku/eqY/MqJxiDj+Gd55wS3f35pbLCzHoEwzKKpDkN5i+TR+1AYCWTo5IV0Z0P9H3phDDd6lMzPdS5bbo9eJGbTsW9nbDqLL1N9Iq+rRxDbll2x67a9Lf27hw5uK1s1rZr6DOPF+FI=')))
print(uncompyle6.code_deparse(co, compile_mode = 'single'))
```

针对 `key_is_here_but_do_you_know_rfc4042` 文件，因为文件名提示rfc4042，所以通过查阅可知应该是utf9编码的。

使用 `utf9` 模块解码可以得到：

```
_____*((__//__+___+______-____%____)**((___%(___-_))+________+(___%___+_____+_______%__+______-(______//(_____%___)))))+__*(((________/__)+___%__+_______-(________//____))**(_*(_____+_____)+_______+_________%___))+________*(((_________//__+________%__)+(_______-_))**((___+_______)+_________-(______//__)))+_______*((___+_________-(______//___-_______%__%_))**(_____+_____+_____))+__*(__+_________-(___//___-_________%_____%__))**(_________-____+_______)+(___+_______)**(________%___%__+_____+______)+(_____-__)*((____//____-_____%____%_)+_________)**(_____-(_______//_______+_________%___)+______)+(_____+(_________%_______)*__+_)**_________+_______*(((_________%_______)*__+_______-(________//________))**_______)+(________/__)*(((____-_+_______)*(______+____))**___)+___*((__+_________-_)**_____)+___*(((___+_______-______/___+__-_________%_____%__)*(___-_+________/__+_________%_____))**__)+(_//_)*(((________%___%__+_____+_____)%______)+_______-_)**___+_____*((______/(_____%___))+_______)*((_________%_______)*__+_____+_)+___//___+_________+_________/___
```

下划线的数量代表数字，在Python2中eval即可算出结果，为 `0x495f346d2d6b3379`。

然后再用hex解码，得到密钥为 `I_4m-k3y`。

之后写解密算法即可得到flag。

