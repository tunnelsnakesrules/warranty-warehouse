from django.urls import path
from . import views

urlpatterns = [
    path('', views.parts_list, name='parts_list'),
    path('parts/', views.parts_list, name='parts_list'),
    path('add/', views.add_part, name='add_part'),  # новый маршрут
]
