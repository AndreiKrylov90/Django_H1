from django.urls import path

from . import views
from .views import user_products

urlpatterns = [
    path('user/<int:user_id>/<int:days>', user_products, name='user_products'),
    path('authors', views.authors),
    path('post/<int:post_id>', views.post, name='post'),
    path('user/<int:user_id>/posts', views.user_posts, name='user_posts'),
]