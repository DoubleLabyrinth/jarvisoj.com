#!/usr/bin/env python2
from pwn import *
context(arch = 'i386')

shellcode = asm('xchg eax, esp')
shellcode += asm('ret')
shellcode += asm('mov ecx, [eax]')
shellcode += asm('mov [edx], ecx')
shellcode += asm('pop ebx')
shellcode += asm('ret')

print 'PCTF{%s}' % shellcode.encode('hex').upper()
