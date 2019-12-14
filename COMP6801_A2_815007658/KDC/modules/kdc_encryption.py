import hashlib
from django.contrib.auth import login,logout
from KDC.models.User import User

#performs password hash using sha256 hashing algo
def hash_value(value):
    hash_instance = hashlib.sha256()
    hash_instance.update(value.encode("utf8"))
    return hash_instance.digest()


def login_user(user_form):
    return
    #login user using auth package
