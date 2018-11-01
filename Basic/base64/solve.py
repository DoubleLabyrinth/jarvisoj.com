#!/usr/bin/env python3
import base64
msg = base64.b32decode('GUYDIMZVGQ2DMN3CGRQTONJXGM3TINLGG42DGMZXGM3TINLGGY4DGNBXGYZTGNLGGY3DGNBWMU3WI===')
msg = bytes.fromhex(msg.decode())
msg = msg.decode()
print(msg)
