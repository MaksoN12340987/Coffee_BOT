from django.urls import path

from cup_coffee.apps import CupCoffeeConfig
from cup_coffee.views import CreateCup, DeleteCup, DetailCup, ListCup, UpdateCup



app_name = CupCoffeeConfig.name

urlpatterns = [
    path("", ListCup.as_view(), name="home"),
    path("create/", CreateCup.as_view(), name="create"),
    path("detaile/<int:pk>/", DetailCup.as_view(), name="detaile"),
    path("update/<int:pk>/", UpdateCup.as_view(), name="update"),
    path("delete/<int:pk>/", DeleteCup.as_view(), name="delete"),
]
