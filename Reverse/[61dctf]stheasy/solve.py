#!/usr/bin/env python3

table1 = 'lk2j9Gh}AgfY4ds-a6QW1#k5ER_T[cvLbV7nOm3ZeX{CMt8SZo]U'
table2 = bytes.fromhex('485d8d248427999f54181e697e3315728d33246321540c78787878781b')

flag = []
for i in range(0, 29):
    flag.append(table1[table2[i] // 3 - 2])
print(''.join(flag))
