import hashlib
from django.contrib.auth import login,logout
from KDC.models.KDCUser import KDCUser

#performs password hash using sha256 hashing algo
def hash_value(value):
    hash_instance = hashlib.sha256()
    hash_instance.update(value.encode("utf8"))
    return hash_instance.digest()


def login_user(user_form):
    #login user using auth package
