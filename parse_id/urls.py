from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.db_list, name='db_list'),
    url(r'db_list/', views.db_list, name='db_list'),
    url(r'add_data/', views.add_data, name='add_data'),
]
