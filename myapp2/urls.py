from django.urls import path
from . import views

urlpatterns = [
    path('coin/<int:amount_throws>', views.coin, name='coin'),
    path('dice/<int:amount_throws>', views.dice, name='dice'),
    path('hundred/<int:amount_throws>', views.hundred, name='hundred'),
    path('result/', views.result, name='hundred'),
]