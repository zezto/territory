from django.urls import path, re_path

from . import views

app_name= 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('all', views.all, name='all'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.detail, name='details'),
    re_path(r'^terr/(?P<pk>[0-9]+)/$', views.TerrUpdate.as_view(), name='ter-update'),
    re_path(r'^terr/(?P<pk>[0-9]+)/delete/$', views.TerrDelete.as_view(), name='ter-delete'),
    re_path(r'^terr/add/$', views.create_terr, name='ter-add'),
    re_path(r'^(?P<pk>[0-9]+)/test$', views.test, name='test'),
    re_path(r'^(?P<pk>[0-9]+)/create_post$', views.create_post, name='create-post'),
    re_path(r'^(?P<pk>[0-9]+)/add-street$', views.addstreet, name='add-street'),
        re_path(r'^(?P<pk>[0-9]+)/add-number$', views.addnumber, name='add-number'),

]