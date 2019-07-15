#!/usr/bin/env python3

c = '8842101220480224404014224202480122'
c = c.split('0')
for i in range(len(c)):
    c[i] = chr(ord('A') + sum([ int(c[i][j]) for j in range(len(c[i])) ]) - 1)
print(''.join(c))
