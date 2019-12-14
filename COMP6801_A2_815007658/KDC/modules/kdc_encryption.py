from django.contrib.auth import login,logout, authenticate
from KDC.models.User import User

def login_user(username, password):
    # login
    user = authenticate(username, password)
    if user:
        login(username, password)
    return user
