# jarvisoj.com -- REVERSE -- DD - Android Normal

## Challenge

```
提交下一关的邮箱地址。

解压密码 infected。

6.Android Normal.zip.a5cfb93ac5f5bc28cfed35a1dea052db
```

## Solution

1. 下载，zip解压。

2. 用 `d2j-dex2jar.bat` 将 `classes.dex` 转化为 `classes-dex2jar.jar`。

3. 将 `classes-dex2jar.jar` 丢到 `jd-gui` 查看。在 `MainActivity` 看到相关代码如下：

   ```java
   static  {
       System.loadLibrary("hello-libs");
   }

   public void onClickTest(View paramView) {
       if (this.mFlagEntryView.getText().toString().equals(stringFromJNI())) {
           this.mFlagResultView.setText("Correct");
           return;
       } 
       this.mFlagResultView.setText("Wrong");
   }
   ```

   显然它是用了JNI。我们到 `lib` 文件夹下找 `hello-libs` 库，把它丢到IDA里。幸运的是题目提供了多平台的 `hello-libs`。

4. x86-64平台下 `hello-libs` 因为编译器优化的缘故，解密直接在编译时就完成了，所以在IDA里可以直接看到flag。

