from django.conf.urls import url
from . import views

urlpatterns = [ # Lista de las urls
    url(r'^login/$', views.authentication, name='authentication'),
    url(r'^', views.hello, name='hello')
]
