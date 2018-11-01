#!/usr/bin/env python3
import morse_talk as mtalk

msg1 = 'XYYY YXXX XYXX XXY XYY X XYY YX YYXX'.replace('X', '.').replace('Y', '-')
msg1 = mtalk.decode(msg1)

def CaesarDecode(msg, shift):
    UpperTable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LowerTable = 'abcdefghijklmnopqrstuvwxyz'
    m = []
    for i in range(len(msg)):
        if msg[i].isalpha():
            if msg[i].islower():
                index = ord(msg[i]) - ord('a')
                m.append(LowerTable[(index - shift) % 26])
            else:
                index = ord(msg[i]) - ord('A')
                m.append(UpperTable[(index - shift) % 26])
        else:
            m.append(msg[i])
    return ''.join(m)

print('PCTF{%s}' % CaesarDecode(msg1, 20))
