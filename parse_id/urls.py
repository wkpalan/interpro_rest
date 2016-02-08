from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.db_list, name='db_list'),
]
