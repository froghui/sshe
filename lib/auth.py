import base64
import time
import hmac
import hashlib
import struct
import sys

def GoogleAuthenticatorCode(secret):
    key = base64.b32decode(secret, True)
    message = struct.pack(">Q", time.time() / 30)
    hashcode = hmac.new(key, message, hashlib.sha1).digest()
    offset = ord(hashcode[19]) & 15
    return (struct.unpack(">I", hashcode[offset:offset+4])[0] & 0x7fffffff) % 1000000

def Main(token):
    code = str(GoogleAuthenticatorCode(token))
    if len(code) < 6:
        code = "0" * (6-len(code)) + code

    print code

Main(sys.argv[1])
