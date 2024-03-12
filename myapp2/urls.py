from django.urls import path
from . import views

urlpatterns = [
    path('coin/<int:amount_flips>', views.coin, name='coin'),
    path('dice/<int:amount_throws>', views.dice, name='dice'),
    path('hundred/', views.hundred, name='hundred'),
]