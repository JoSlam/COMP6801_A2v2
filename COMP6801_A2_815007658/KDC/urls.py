from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'KDC'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^app/', include('app.urls', namespace='app')),
    url(r'^login/$', views.UserLoginView.as_view(), name='login'),
    url(r'^register/$', views.UserRegistrationView.as_view(), name='register'),

]
