# jarvisoj.com -- CRYPTO -- 简单ECC概念

## Challenge

```
已知椭圆曲线加密Ep(a,b)参数为

p = 15424654874903

a = 16546484

b = 4548674875

G(6478678675,5636379357093)

私钥为

k = 546768

求公钥K(x,y)

提示：K=kG

提交格式XUSTCTF{x+y}(注意，大括号里面是x和y加起来求和，不是用加号连接)

注：题目来源XUSTCTF2016
```

## Solution

用sage可以完成计算

```sage
#!/usr/bin/env sage
F = Zmod(15424654874903)
Curve = EllipticCurve(F, [16546484, 4548674875])
G = Curve(6478678675, 5636379357093)
K = 546768 * G
x, y = K.xy()
print 'XUSTCTF{%d}' % (int(x) + int(y))
```
