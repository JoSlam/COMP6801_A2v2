import hashlib

#performs password hash using sha256 hashing algo
def hash_value(value):
    hash_instance = hashlib.sha256()
    hash_instance.update(value.encode("utf8"))
    return hash_instance.digest()