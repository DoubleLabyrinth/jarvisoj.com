#!/usr/bin/env python3
import base64

base64_table = ['=','A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                'a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                '0', '1', '2', '3','4','5','6','7','8','9',
                '+', '/'][::-1]
base64_table = ''.join(base64_table)

tr = str.maketrans(
    base64_table[0:64],
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
)

s = 'mZOemISXmpOTkKCHkp6Rgv=='.translate(tr)
print(base64.b64decode(s))

