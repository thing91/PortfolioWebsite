from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^skills/', views.skills, name='skills'),
    url(r'^expv2/', views.expv2, name='expv'),
]
