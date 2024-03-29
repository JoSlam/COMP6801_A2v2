from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'TGS'

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^create_application/$', views.ApplicationCreationView.as_view(), name="create"),
    path('add_app_to_user/<int:app_id>', views.add_app_to_user, name='add_app_to_user'),
    path('application/<int:app_id>', views.app_details, name="app_details"),
    path('application/edit/<int:app_id>', views.ApplicationEditView.as_view(), name="edit_app"),
]
