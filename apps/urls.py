from django.urls import path
from apps import views
urlpatterns=[
    path("",views.index),
    path("model/",views.process),
]