from django.contrib.auth import login, logout, authenticate
from KDC.models.User import User

def login_user(request, username, password):
    # login
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request=request, user=user)
    return user if user else None
