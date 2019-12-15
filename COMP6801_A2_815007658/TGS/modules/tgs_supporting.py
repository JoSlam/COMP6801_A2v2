import random
import Crypto
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

from base64 import b64decode
from base64 import b64encode

def generate_nonce(max):
    return random.randint(1, max)
     
def encrypt(message, key):
    cipher = DES.new(key=key.encode("utf8"), mode=DES.MODE_ECB)
    return b64encode(cipher.encrypt(pad(message.encode("utf8"), DES.block_size))).decode("utf8")

def decrypt(ciphertext, key):
    cipher = DES.new(key=key.encode("utf8"), mode=DES.MODE_ECB)
    return unpad(cipher.decrypt(b64decode(ciphertext.encode("utf8"))), DES.block_size).decode("utf8")