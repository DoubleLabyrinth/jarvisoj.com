# jarvisoj.com -- BASIC -- 神秘的文件

## Challenge

```
出题人太懒，还是就丢了个文件就走了，你能发现里面的秘密吗？

haha.f38a74f55b4e193561d1b707211cf7eb
```

## Solution

```
$ binwalk haha.f38a74f55b4e193561d1b707211cf7eb

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Linux EXT filesystem, rev 1.0, ext2 filesystem data, UUID=8eecd08f-bae8-41ff-8497-8338f58af58a
35751         0x8BA7          mcrypt 2.2 encrypted data, algorithm: blowfish-448, mode: CBC, keymode: 8bit

$ mkdir haha

$ sudo mount ./haha.f38a74f55b4e193561d1b707211cf7eb ./haha

$ cd haha

$ ls
0    106  114  122  130  139  147  155  163  171  18   188  196  203  211  22   228  236  244  252  32  40  49  57  65  73  81  9   98
1    107  115  123  131  14   148  156  164  172  180  189  197  204  212  220  229  237  245  253  33  41  5   58  66  74  82  90  99
10   108  116  124  132  140  149  157  165  173  181  19   198  205  213  221  23   238  246  26   34  42  50  59  67  75  83  91  lost+found
100  109  117  125  133  141  15   158  166  174  182  190  199  206  214  222  230  239  247  27   35  43  51  6   68  76  84  92
101  11   118  126  134  142  150  159  167  175  183  191  2    207  215  223  231  24   248  28   36  44  52  60  69  77  85  93
102  110  119  127  135  143  151  16   168  176  184  192  20   208  216  224  232  240  249  29   37  45  53  61  7   78  86  94
103  111  12   128  136  144  152  160  169  177  185  193  200  209  217  225  233  241  25   3    38  46  54  62  70  79  87  95
104  112  120  129  137  145  153  161  17   178  186  194  201  21   218  226  234  242  250  30   39  47  55  63  71  8   88  96
105  113  121  13   138  146  154  162  170  179  187  195  202  210  219  227  235  243  251  31   4   48  56  64  72  80  89  97

$ cat {0..253}
Haha ext2 file system is easy, and I know you can easily decompress of it and find the content in it.But the content is spilted in pieces can you make the pieces together. Now this is the flag PCTF{P13c3_7oghter_i7}. The rest is up to you. Cheer up, boy.

$
```
