from django.conf.urls import url, include
from .views import views

app_name = 'app'

urlpatterns = [
    #/
    url(r'^$', views.index , name='index'),
    
]
