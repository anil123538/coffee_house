from django.urls import path
from . import views

#create urls
urlpatterns = [
    path('',views.home),
]

