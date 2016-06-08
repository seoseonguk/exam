from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^category/(?P<pk>\d+)/$', category_detail, name='category_detail'),
    url(r'^category/new/$', category_new, name='category_new'),
]
