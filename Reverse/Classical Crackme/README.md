# jarvisoj.com -- CRYPTO -- Classical Crackme

## Challenge

```
经典Crackme题目，FLAG就是注册码。

CrackMe.rar.4b81595bfc90d446ba30f9c9bb03fb49
```

## Solution

下载文件并解压，你可以得到一个exe程序。尽管图标是一个MFC图标，但程序是一个.Net程序。

使用 __.Net Reflector__ 打开，会发现有乱码，但是仅仅是经过混淆了，好像是把方法名等全部倒序了。但是没关系，我们重点看成员函数，尤其是事件处理函数。

```cs
private void ‬​⁪‪⁭⁫‭⁯‭‌‎⁫‮‮‬‫⁪⁭⁮‫⁮‏‭‎‬‏‍‏‫‌‪⁭⁪⁮‭‍‌⁫‪‭‮(object, EventArgs)
{
    string s = this.‎⁯⁪‏⁮‬⁬‌⁪​⁮‭⁫‭‏⁫‫‌⁫‭⁭‫⁫‌⁯⁭⁪‭‏‮​⁭‬‍‍‬‏‮‮⁪‮.Text.ToString();
    if (Convert.ToBase64String(Encoding.Default.GetBytes(s)) == "UENURntFYTV5X0RvX05ldF9DcjRjazNyfQ==")
    {
        MessageBox.Show("注册成功！", "提示", MessageBoxButtons.OK);
    }
    else
    {
        MessageBox.Show("注册失败！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Hand);
    }
}
```

找到这个函数你也就知道flag是什么了。

```
$ echo "UENURntFYTV5X0RvX05ldF9DcjRjazNyfQ==" | base64 -d
```

