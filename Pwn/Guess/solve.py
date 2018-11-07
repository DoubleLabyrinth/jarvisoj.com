#!/usr/bin/env python2
from pwn import *

possible_chars = 'PCTF{0123456789abcdef}'
flag = ''
offset = 64

conn = remote('pwn.jarvisoj.com', 9878)

def Guess(s):
    prefix_len = 50 - len(s)
    assert(prefix_len >= 0)
    conn.sendline(''.join([ '0' + pack(i - 64, 8) for i in range(prefix_len) ]) + s.encode('hex'))

sleep(1)
while len(flag) < 50:
    current_flag_len = len(flag)
    for c in possible_chars:
        conn.read()
        print('Try char: %c' % c)
        Guess(c + flag)
        recv = conn.readline()
        if recv.find('Yaaaay!') != -1:
            flag = c + flag
            log.info('update flag = %s' % flag)
            break
        elif recv.find('Nope.') != -1:
            continue
        else:
            raise ValueError('Unexpected recv = %s' % repr(recv))
    assert(len(flag) != current_flag_len)
