from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('app.urls')),
    path('kdc/', include('KDC.urls')),
    path('tgs/', include('TGS.urls')),
    path('admin/', admin.site.urls),
]
