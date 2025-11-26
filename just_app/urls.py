from just_app import views
from django.urls import path

urlpatterns = [
    path('', views.add_item)
]