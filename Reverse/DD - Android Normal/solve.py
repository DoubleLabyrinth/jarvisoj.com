#!/usr/bin/env python3

flag = bytearray.fromhex(
    '39636aa60031553da360e0916a66b36ba90b724228877c8fc1e27e4f44444354462d3339376139306133323637363431363538626263393735333236373030663462406469646963687578696e672e636f6d0096022655cab7569e0a29fb4a658c4b7a3d0c2d851267546a19e879d7f9577ab36d4dbce4eba060f9a31015bf0f026484727d95ad6c5efd42c66e5b10ddb3e773ad1e65350af2372532608b26fd'
)

flag += int(0x52EA7EE0AE6725FB).to_bytes(8, 'little')
flag += int(0xF657389C33AB7F7F).to_bytes(8, 'little')
flag += int(0x2509D1E6).to_bytes(4, 'little')
flag += int(0xC841).to_bytes(2, 'little')

print(flag[flag[0] // 2 : flag.find(b'\x00', flag[0] // 2)])

