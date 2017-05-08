from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money/(?P<my_data>[A-Za-z]+)$', views.process_money),
    url(r'^reset$', views.reset),
]
