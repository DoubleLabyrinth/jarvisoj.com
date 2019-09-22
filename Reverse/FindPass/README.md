# jarvisoj.com -- REVERSE -- FindPass

## Challenge

```
FindPass_200.apk.722003c4d7d4c8b37f0eaa5f7109e87a
```

## Solution

1. 下载，zip解压。

2. `$ d2j-dex2jar.bat classes.dex`，得到 `classes-dex2jar.jar`。

3. `$ java -jar cfr-0.146.jar classes-dex2jar.jar > code.txt`。

4. `MainActivity` 相关代码如下：

   ```java
   public void GetKey(View object) {
       object = ((EditText)this.findViewById(2131230721)).getText().toString();
       if (TextUtils.isEmpty((CharSequence)((String)object).trim())) {
           Toast.makeText((Context)this, (CharSequence)"请输入key值！", (int)1).show();
           return;
       }
       char[] arrc = this.getResources().getString(2131034115).toCharArray();
       int n = arrc.length;
       char[] arrc2 = new char[1024];
       try {
           InputStreamReader inputStreamReader = new InputStreamReader(this.getResources().getAssets().open("src.jpg"));
           inputStreamReader.read(arrc2);
       }
       catch (Exception exception) {
           exception.printStackTrace();
       }
       int n2 = 0;
       do {
           if (n2 >= n) {
               if (!((String)object).equals(new String(arrc))) break;
               Toast.makeText((Context)this, (CharSequence)"恭喜您，输入正确！Flag==flag{Key}", (int)1).show();
               return;
           }
           int n3 = arrc2[arrc[n2]] % 10;
           arrc[n2] = n2 % 2 == 1 ? (char)((char)(arrc[n2] + n3)) : (char)((char)(arrc[n2] - n3));
           ++n2;
       } while (true);
       Toast.makeText((Context)this, (CharSequence)"not right! lol。。。。", (int)1).show();
   }
   ```

   其中 `this.getResources().getString(2131034115)` 对应名为 `fkey` 的字符串资源，你可以通过apktool反编译得到，值为 `Tr43Fla92Ch4n93`。

   `src.jpg` 位于 `assets` 文件夹下，只是一张图片。

5. 根据这个可以写出解密代码：

   ```java
   public static void main(String[] args) {
       char[] fkey = "Tr43Fla92Ch4n93".toCharArray();
       char[] jpg = new char[1024];

       try {
           FileInputStream fileInputStream = new FileInputStream("src.jpg");
           InputStreamReader reader = new InputStreamReader(fileInputStream);
           reader.read(jpg);
       } catch (Exception e) {
           e.printStackTrace();
       }

       for (int i = 0; i < fkey.length; ++i) {
           int k = jpg[fkey[i]] % 10;
           if (i % 2 == 1) {
               fkey[i] += k;
           } else {
               fkey[i] -= k;
           }
       }

       System.out.format("flag{%s}", new String(fkey));
   }
   ```
   