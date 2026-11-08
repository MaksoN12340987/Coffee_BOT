from django.urls import path

from TV.views import Tv_1, Tv_2, Tv_3, Tv_4, Test
from cup_coffee.apps import CupCoffeeConfig

app_name = CupCoffeeConfig.name

urlpatterns = [
    path("1/", Tv_1.as_view(), name="home"),
    path("2/", Tv_2.as_view(), name="create"),
    path("3/", Tv_3.as_view(), name="detaile"),
    path("4/", Tv_4.as_view(), name="update"),
    path("test/", Test.as_view(), name="home"),
]
