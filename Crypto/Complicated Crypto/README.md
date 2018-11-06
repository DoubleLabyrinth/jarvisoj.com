# jarvisoj.com -- CRYPTO -- Complicated Crypto

## Challenge

```
五层密码，好复杂

来源：sunnyelf

Complicated Crypto.7z.800733a9251cab311bb5f34f15386008
```

## Solution

1. __CRC32碰撞__

   下载文件，得到一个7z压缩包。里面`pwd1.txt`、`pwd2.txt`、`pwd3.txt`三个文件的CRC32值已经给定。使用hashcat爆破。

   构造crc32.txt

   ```
   7C2DF918:00000000
   A58A1926:00000000
   4DAD5967:00000000
   ```

   使用hashcat

   ```
   $ hashcat64.exe -m 11500 -a 3 --keep-guessing crc32.txt ?a?a?a?a?a?a
   ```

   每一个CRC32值约有170种可能的结果。所以可能的密码数量在百万级。构造字典，使用hashcat爆破7z压缩包。

   首先用`7z2hashcat`对`Complicated Crypto.7z`做个处理，得到一个hash串。

   ```
   $ 7z2hashcat64-1.2.exe "Complicated Crypto.7z"
   $7z$2$19$0$$8$2bd0665b6a3cbb6a0000000000000000$2083387672$32$22$fb1abaee780a2be0f1f52e57813861be242bd6ca2c7601c10c6dba9b4f74ce05$6$0c
   ```

   这个hash串就是hashcat要爆破的密码，把它保存为`pass.txt`。然后用python脚本构造字典`dict.txt`

   ```python
   #!/usr/bin/env python3

   pwd1 = []
   pwd2 = []
   pwd3 = []
   with open('hashcat.potfile') as f:
       while True:
           line = f.readline()
           if line == '':
               break
           crc32, iv, plaintext = line.split(':')
           plaintext = plaintext.strip('\n')
           if plaintext.startswith('$HEX'):
               plaintext = bytes.fromhex(plaintext.lstrip('$HEX[').rstrip(']')).decode()
           if crc32 == '7C2DF918'.lower():
               pwd1.append(plaintext)
           elif crc32 == 'A58A1926'.lower():
               pwd2.append(plaintext)
           elif crc32 == '4DAD5967'.lower():
               pwd3.append(plaintext)
           else:
               assert(False)

   pwd1.sort()
   pwd2.sort()
   pwd3.sort()
   with open('dict.txt', 'w') as f:
       for a in pwd1:
           for b in pwd2:
               for c in pwd3:
                   f.write('%s\n' % (a + b + c))
   ```

   然后用hashcat爆破

   ```
   $ hashcat64.exe -m 11600 pass.txt dict.txt
   ...
   ...

   $7z$2$19$0$$8$2bd0665b6a3cbb6a0000000000000000$2083387672$32$22$fb1abaee780a2be0f1f52e57813861be242bd6ca2c7601c10c6dba9b4f74ce05$6$0c:_CRC32_i5_n0t_s4f3

   ...
   ...
   ```

   所以密码是`_CRC32_i5_n0t_s4f3`

2. __维吉尼亚密码__

   解压`CRC32 Collision.7z`之后，你会得到4个文件。其中`tips.txt`说了是维吉尼亚密码。

   好吧，先看看密文：

   ```
   rla xymijgpf ppsoto wq u nncwel ff tfqlgnxwzz sgnlwduzmy vcyg ib bhfbe u tnaxua ff satzmpibf vszqen eyvlatq cnzhk dk hfy mnciuzj ou s yygusfp bl dq e okcvpa hmsz vi wdimyfqqjqubzc hmpmbgxifbgi qs lciyaktb jf clntkspy drywuz wucfm
   ```

   如果明文是英语，那么长度仅为一个字符的单词也就只有`"a"`了。根据这个我们可以判断：`key[19]`、`key[29]`和`key[1]`必须分别为`"u"`、`"s"`、`"e"`。

   用python过滤掉不合要求的keys：

   ```python
   #!/usr/bin/env python3

   with open('keys.txt', 'r') as f:
       keys = [ key.strip('\n') for key in f.readlines() ]
       possible_keys_0 = []
       for key in keys:
           if key[19].lower() == 'u':
               possible_keys_0.append(key)

       possible_keys_1 = []
       for key in possible_keys_0:
           if key[29].lower() == 's':
               possible_keys_1.append(key)

       possible_keys_2 = []
       for key in possible_keys_1:
           if key[1].lower() == 'e':
               possible_keys_2.append(key)

       print(possible_keys_2)
   ```

   最后可以得到两个key：`SEKMAJBRIMQUGQZMGJHUJMTJAPYUZSAUEACHKLBD`和`YEWCQGEWCYBNHDHPXOYUBJJPQIRAPSOUIYEOMTSV`。其中只有通过后者才可以得到有意义的明文：

   ```
   the vigenere cipher is a method of encrypting alphabetic text by using a series of different caesar ciphers based on the letters of a keyword it is a simple form of polyalphabetic substitution so password is vigenere cipher funny
   ```

3. __SHA1__

   解压`Find password.7z`文件之后，你会得到2个文件。根据`U need unzip password.txt`文件的提示，你需要爆破出压缩包密码。

   ```python
   #!/usr/bin/env python3
   from hashlib import sha1

   for a in range(0x20, 0x7f):
       for b in range(0x20, 0x7f):
           for c in range(0x20, 0x7f):
               for d in range(0x20, 0x7f):
                   msg = '%c7%c5-%c4%c3?' % (a, b, c, d)
                   hash = sha1(msg.encode()).hexdigest()
                   if hash.startswith('619c20c'):
                       print(msg)
       print('[*] Next a = %d' % a)
   ```

   最后你会看到密码是`I7~5-s4F3?`。

4. __MD5碰撞__

   提示提到的两个程序是

   * [http://www.win.tue.nl/hashclash/SoftIntCodeSign/HelloWorld-colliding.exe](http://www.win.tue.nl/hashclash/SoftIntCodeSign/HelloWorld-colliding.exe)

   * [http://www.win.tue.nl/hashclash/SoftIntCodeSign/GoodbyeWorld-colliding.exe](http://www.win.tue.nl/hashclash/SoftIntCodeSign/GoodbyeWorld-colliding.exe)

   其中第二个程序的输出是

   ```
   Goodbye World :-(
   ```

   用这个解压文件即可。

5. __RSA__

   解压后得到密文和公钥。但是公钥的加密指数e太大了，可以考虑wiener attack。

   ```
   $ ./RsaWienerAttack.py 460657813884289609896372056585544172485318117026246263899744329237492701820627219556007788200590119136173895989001382151536006853823326382892363143604314518686388786002989248800814861248595075326277099645338694977097459168530898776007293695728101976069423971696524237755227187061418202849911479124793990722597 354611102441307572056572181827925899198345350228753730931089393275463916544456626894245415096107834465778409532373187125318554614722599301791528916212839368121066035541008808261534500586023652767712271625785204280964688004680328300124849680477105302519377370092578107827116821391826210972320377614967547827619

   p = 28805791771260259486856902729020438686670354441296247148207862836064657849735343618207098163901787287368569768472521344635567334299356760080507454640207003

   q = 15991846970993213322072626901560749932686325766403404864023341810735319249066370916090640926219079368845510444031400322229147771682961132420481897362843199

   phi = 460657813884289609896372056585544172485318117026246263899744329237492701820627219556007788200590119136173895989001382151536006853823326382892363143604314473888750043749516439871285230667406455969596891945686682745892812368553799974292759397989011855202767757616311733833560322346312220532018978135441987672396

   d = 8264667972294275017293339772371783322168822149471976834221082393409363691895

   e = 354611102441307572056572181827925899198345350228753730931089393275463916544456626894245415096107834465778409532373187125318554614722599301791528916212839368121066035541008808261534500586023652767712271625785204280964688004680328300124849680477105302519377370092578107827116821391826210972320377614967547827619

   n = 460657813884289609896372056585544172485318117026246263899744329237492701820627219556007788200590119136173895989001382151536006853823326382892363143604314518686388786002989248800814861248595075326277099645338694977097459168530898776007293695728101976069423971696524237755227187061418202849911479124793990722597

   -----BEGIN RSA PRIVATE KEY-----
   MIICOgIBAAKBgQKP/53T5v6XgWSet/5ekwPPaWNHxBELxLo5afCxFmmEDFHYGmhC
   tt8rCQ8hzXbUNxqMDkcEjJZeyltGkTr7uNoFIHKgVm1wOcYYq6kGV1mwWeKeSF3F
   BhoWrGMSlDjZNU5l31dHVGuF2z1pmBnEt3Mt+SfHCEpdUtbm1qrBRGI0JQKBgQH4
   +6QQBS337aNGLxqs1p5AdgQzyjNXZ81zBaPQkIBaX9QF3W7qcOmPDKHhzyVHSGcb
   8MmABsIO7h1ieQQ1Cf56mCOLQ5FgpWEtpx6QRRToEoBhfjB8PNMxP6TG/KMxWdBE
   H7sY2DyvS9Rva5KXqAoULdab8aNXzLXkwgC22Q8VowIgEkWi5MMhraVZBcJJt+CW
   QPiKQcq9Y8kytE4BDTeIyXcCQQIl/8b3xtiVlpZmPkzbkNSiUKmaISK/az2aRDGh
   qNLmzXhIr045a5fsEQnqnPMM9nryIVzCy9OnVP8KpkB9+bSbAkEBMVaFDQVZVRk2
   9CXoPsJL8JBVkfE+SgeFf4hJ82tPkEQxtQqkUJuvE2lYPjL/8rJa8Q453oaM6ncG
   7+6MNvtmPwIgEkWi5MMhraVZBcJJt+CWQPiKQcq9Y8kytE4BDTeIyXcCIBJFouTD
   Ia2lWQXCSbfglkD4ikHKvWPJMrROAQ03iMl3AkEBi2zSOR7TqgaL9Nk3IgtIOmWW
   nkAMnPrBAdnE3YQ34U34VlS12L4kyIB1fl5XERSqBnt+KLce0ttoaF8uOUVKfA==
   -----END RSA PRIVATE KEY-----
   ```

   然后用openssl解密即可

   ```
   $ openssl rsautl -decrypt -in flag.enc -inkey .\rsa_private_key.pem
   ```

