from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.all, name='what'),
    re_path(r'^(?P<num>[0-9]+)$', views.detail, name='details'),
]