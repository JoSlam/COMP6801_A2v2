from django.conf.urls import url, include
from .views import views

app_name = 'KDC'

urlpatterns = [
    #/
    url(r'^$', views.index , name='index'),
    url(r'^login/$', views.login , name='login'),
    url(r'^register/$', views.register , name='register'),
]
