from django.urls import path

from TV.views import Sale, Tv_1, Tv_2, Tv_3, Tv_4, Test
from cup_coffee.apps import CupCoffeeConfig

app_name = CupCoffeeConfig.name

urlpatterns = [
    path("1/", Tv_1.as_view(), name="Tv_1"),
    path("2/", Tv_2.as_view(), name="Tv_2"),
    path("3/", Tv_3.as_view(), name="Tv_3"),
    path("4/", Tv_4.as_view(), name="Tv_4"),
    path("sale/", Sale.as_view(), name="Sale"),
    path("test/", Test.as_view(), name="home"),
]
