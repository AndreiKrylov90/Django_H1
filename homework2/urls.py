from django.urls import path
from .views import user_products

urlpatterns = [
    path('user/<int:user_id>/<int:days>', user_products, name='user_products'),
]