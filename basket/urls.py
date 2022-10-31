from django.urls import path
from . import views


urlpatterns = [
    path('', views.basket_sumary, name="basket_summary")
]

