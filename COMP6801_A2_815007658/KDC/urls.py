from django.conf.urls import url, include
from . import views

app_name = 'KDC'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.UserLoginView.as_view(), name='login'),
    url(r'^register/$', views.UserRegistrationView.as_view(), name='register'),
    url(r'^register_success/$', views.register_success, name='register_success'),

]
