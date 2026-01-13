from just_app import views
from django.urls import path

urlpatterns = [
    path('', views.for_product),
    path('product/<int:product_id>', views.for_size)
]