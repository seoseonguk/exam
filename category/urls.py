from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^category/(?P<pk>\d+)/$', category_detail, name='category_detail'),
    url(r'^category/(?P<pk>\d+)/edit/$', category_edit, name='category_edit'),

    url(r'^category/new/$', category_new, name='category_new'),
]
