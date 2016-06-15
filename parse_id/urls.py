from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



urlpatterns = [
    url(r'^$', views.redirect_parse_id),
    url(r'^parse_id/$', views.base_view.as_view()),
    url(r'^parse_id/add/$', views.base_add.as_view()),
    url(r'^parse_id/(?P<db_name>[^/]+)/$', views.db_view.as_view()),
    url(r'^parse_id/(?P<db_name>[A-Za-z0-9]+)/(?P<db_id>[^/]+)[/$]', views.db_id_view.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
