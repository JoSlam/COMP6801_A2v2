from django.urls import include, path
from django.conf.urls import url

from .views import views

app_name = 'app'

urlpatterns = [
    #/
    url(r'^$', views.index , name='index'),
    path('tgs/', include('TGS.urls'))
    
]
