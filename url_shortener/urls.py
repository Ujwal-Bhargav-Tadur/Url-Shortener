from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('stats/', views.stats, name='stats'),
    path('shorten/', views.add_link, name='add_link'),
    path('about/', views.about, name='about'),
    path('<str:short_url>/', views.redirect_to_url, name='redirect_to_url'),
]
