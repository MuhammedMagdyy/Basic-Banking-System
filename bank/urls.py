from django.urls import path, include
from bank.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('index/', index_view, name="index"),
    path('list/', list_view, name='list'),
    path('form/<id>', update_view, name="update"),
]
