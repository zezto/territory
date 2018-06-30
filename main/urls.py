from django.urls import path, re_path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.all, name='all'),
    re_path(r'^(?P<num>[0-9]+)$', views.detail, name='details'),
]