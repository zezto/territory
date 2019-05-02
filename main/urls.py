from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.UserFormView.as_view(), name='login'),
    path('all', views.all, name='all'),
    path('create-account', views.UserCreateView.as_view(), name='create-acc'),
    path('dashboard', views.UserDashBoard.as_view(), name='dashboard'),
    path('stats', views.Stats.as_view(), name='stats'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.detail, name='details'),
    re_path(r'^(?P<pk>[0-9]+)/test$', views.test, name='test'),
    re_path(r'^(?P<pk>[0-9]+)/(?P<streetpk>[0-9]+)/create_post$',
            views.create_post, name='create-post'),
    re_path(r'^(?P<pk>[0-9]+)/add-street$',
            views.addstreet, name='add-street'),
    re_path(r'^(?P<pk>[0-9]+)/(?P<streetpk>[0-9]+)/add-number$',
            views.addnumber, name='add-number'),
    re_path(r'^(?P<pk>[0-9]+)/(?P<streetpk>[0-9]+)$',
            views.streetdeets, name='street-details'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
