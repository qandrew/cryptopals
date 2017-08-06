# AES in ECB mode


from base64 import b64decode
# from base64 import b64encode
from Crypto.Cipher import AES

with open('7.txt', 'r') as f:
    data = f.read().decode('base64')

KEY = "YELLOW SUBMARINE"

a = AES.new(KEY,AES.MODE_ECB)
print a.decrypt(data)