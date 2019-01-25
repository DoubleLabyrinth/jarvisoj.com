[g]: https://latex.codecogs.com/gif.latex?g
[p]: https://latex.codecogs.com/gif.latex?p
[q]: https://latex.codecogs.com/gif.latex?q
[x]: https://latex.codecogs.com/gif.latex?x
[y]: https://latex.codecogs.com/gif.latex?y
[k]: https://latex.codecogs.com/gif.latex?k
[r]: https://latex.codecogs.com/gif.latex?r
[s]: https://latex.codecogs.com/gif.latex?s
[M]: https://latex.codecogs.com/gif.latex?M
[M_1]: https://latex.codecogs.com/gif.latex?M_1
[M_2]: https://latex.codecogs.com/gif.latex?M_2

# jarvisoj.com -- CRYPTO -- DSA

## Challenge

```
DSA是基于整数有限域离散对数难题的，其安全性与RSA相比差不多。DSA的一个重要特点是两个素数公开，这样，当使用别人的p和q时，即使不知道私钥x，你也能确认它们是否是随机产生的，还是作了手脚。

可以使用openssl方便地进行dsa签名和验证。

签名与验证：

openssl dgst -sha1 -sign dsa_private.pem -out sign.bin message.txt

openssl sha1 -verify dsa_public.pem -signature sign.bin message.txt

本题的攻击方法曾被用于PS3的破解，答案格式：CTF{x}(x为私钥，请提交十进制格式)


dsa.rar.fca5b1bd311ecbf50cad05f31ba995c4
```

## Solution

首先从题目中我们可以知道采用的哈希算法是sha1。

然后下载附件，里面有一份公钥文件和4份消息与签名。

```
./dsa_public.pem
./packet1/message1
./packet1/sign1.bin
./packet2/message2
./packet2/sign2.bin
./packet3/message3
./packet3/sign3.bin
./packet4/message4
./packet4/sign4.bin
```

现在先回顾下DSA签名的原理。

### 1. DSA签名

DSA用到的参数有 ![][g]，![][p] 和 ![][q]。

其中 ![][g] 是生成元，![][p] 是域的特征，![][q] 是子域特征，并且 ![][q] 是 ![](https://latex.codecogs.com/gif.latex?p-1) 的素因子。三者满足

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?1%20%3D%20g%5Eq%5C%20%28mod%5C%20p%29"/>
</p>

私钥为![][x] ，公钥为 ![][y] ，并且私钥和公钥满足

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?y%20%3D%20g%5Ex%5C%20%28mod%5C%20p%29"/>
</p>

#### 1.1 签名

1. 随机选取一个数 ![][k]，要求 

   <p align="center">
   <img src="https://latex.codecogs.com/gif.latex?1%3Ck%3Cq"/>
   </p>

2. 计算

   <p align="center">
   <img src="https://latex.codecogs.com/gif.latex?r%3D%28g%5Ek%5C%20mod%5C%20p%29%5C%20mod%5C%20q"/>
   </p>

3. 如果 ![][r] 为0，则返回步骤1。

4. 计算

   <p align="center">
   <img src="https://latex.codecogs.com/gif.latex?s%3D%5Cfrac%7BM&plus;xr%7D%7Bk%7D%5C%20mod%5C%20q"/>
   </p>

   其中 ![][M] 一般是消息的哈希

5. 如果 ![][s] 为0，则返回步骤1；否则签名为 ![](https://latex.codecogs.com/gif.latex?%28r%2C%5C%20s%29)

#### 1.2 验证

1. 计算

   <p align="center">
   <img src="https://latex.codecogs.com/gif.latex?w%3Ds%5E%7B-1%7D%5C%20mod%5C%20q"/>
   <br></br>
   <img src="https://latex.codecogs.com/gif.latex?u_1%3DM%5Ccdot%20w%5C%20mod%5C%20q"/>
   <br></br>
   <img src="https://latex.codecogs.com/gif.latex?u_2%3Dr%5Ccdot%20w%5C%20mod%5C%20q"/>
   <br></br>
   <img src="https://latex.codecogs.com/gif.latex?v%3D%28g%5E%7Bu_1%7D%5Ccdot%20y%5E%7Bu_2%7D%5C%20mod%5C%20p%29%5C%20mod%5C%20q">
   </p>

2. 当且仅当 ![](https://latex.codecogs.com/gif.latex?v%3Dr) 时，签名有效。

#### 1.3 简单证明

考虑到

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?s%3D%5Cfrac%7BM&plus;xr%7D%7Bk%7D%5C%20mod%5C%20q"/>
</p>

故

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Balign*%7D%20k%26%3D%5Cfrac%7BM&plus;xr%7D%7Bs%7D%5C%20mod%5C%20q%5C%5C%20%26%3DM%5Ccdot%20s%5E%7B-1%7D&plus;xr%5Ccdot%20s%5E%7B-1%7D%5C%20mod%5C%20q%5C%5C%20%26%3DM%5Ccdot%20w&plus;xr%5Ccdot%20w%5C%20mod%5C%20q%5C%5C%20%26%3Du_1&plus;x%5Ccdot%20u_2%5C%20mod%5C%20q%5C%5C%20%5Cend%7Balign*%7D"/>
</p>

又考虑到

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?r%3D%28g%5Ek%5C%20mod%5C%20p%29%5C%20mod%5C%20q"/>
</p>

代入 ![][k]，得到

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Balign*%7D%20r%26%3D%28g%5E%7Bu_1&plus;x%5Ccdot%20u_2%7D%5C%20mod%5C%20p%29%5C%20mod%5C%20q%5C%5C%20%26%3D%28g%5E%7Bu_1%7D%5Ccdot%20g%5E%7Bx%5Ccdot%20u_2%7D%5C%20mod%5C%20p%29%5C%20mod%5C%20q%5C%5C%20%26%3D%28g%5E%7Bu_1%7D%5Ccdot%20y%5E%7Bu_2%7D%5C%20mod%5C%20p%29%5C%20mod%5C%20q%5C%5C%20%26%3Dv%20%5Cend%7Balign*%7D"/>
</p>

故 ![](https://latex.codecogs.com/gif.latex?v%3Dr) 是签名有效的必要条件。

至于充分条件，抱歉我不知道怎么证明。

### 2. 寻找私钥

这道题怎么寻找私钥呢？关键就在随机数 ![][k] 上。如果在对不同的消息的签名过程中，随机数 ![][k] 使用了两次，那么我们可以绕过有限域下的离散对数难题，直接在多项式时间内算出私钥 ![][x]。过程如下：

假设有不同的消息（哈希）![][M_1] 和 ![][M_2]，签名分别为 ![](https://latex.codecogs.com/gif.latex?%28r_1%2C%5C%20s_1%29) 和 ![](https://latex.codecogs.com/gif.latex?%28r_2%2C%5C%20s_2%29)，但是使用了相同的随机数 ![][k]

那么我们有

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Balign*%7D%20s_2-s_1%26%3D%5Cfrac%7BM_2&plus;xr%7D%7Bk%7D-%5Cfrac%7BM_1&plus;xr%7D%7Bk%7D%5C%20mod%5C%20q%5C%5C%20%26%3D%5Cfrac%7BM_2-M_1%7D%7Bk%7D%5C%20mod%5C%20q%20%5Cend%7Balign*%7D"/>
</p>

从而可以算得

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?k%3D%5Cfrac%7BM_2-M_1%7D%7Bs_2-s_1%7D%5C%20mod%5C%20q"/>
</p>

进而也可以知晓 ![][r]。

于是私钥 ![][x] 可以通过下面的公式算出

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Balign*%7D%20s_1%26%3D%5Cfrac%7BM_1&plus;xr%7D%7Bk%7D%5C%20mod%5C%20q%5C%5C%20%26%5CRightarrow%20%5C%5C%20x%26%3D%5Cfrac%7Bs_1%5Ccdot%20k-M_1%7D%7Br%7D%5C%20mod%5C%20q%20%5Cend%7Balign*%7D"/>
</p>

### 3. PS

1. openssl中所有大数的表示都是大端字节序。

2. 你可以使用`openssl asn1parse`来提取签名文件的里的 ![][r] 和 ![][s]

   ```shell
   $ openssl asn1parse -inform DER < ./sign1.bin
   ```

3. 你可以使用pycryptodome库来加载DSA公钥，并提取 ![][g]、![][q]、![][p] 和 ![][y]

   ```python
   from Crypto.PublicKey import DSA
   with open('dsa_public.pem') as f:
       key = DSA.import_key(f.read())
   print('g = %d' % key._key['g'])
   print('q = %d' % key._key['q'])
   print('p = %d' % key._key['p'])
   print('y = %d' % key._key['y'])
   ```