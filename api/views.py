import logging
from rest_framework import generics, viewsets
from rest_framework.response import Response

from api.serializer import CoffeeCupSerializer
from cup_coffee.models import CoffeeCup
from users.models import BaseUser

logger_views = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_views.addHandler(file_handler)
logger_views.setLevel(logging.INFO)


class CupsLessonsAPI(generics.ListAPIView):
    serializer_class = CoffeeCupSerializer
    queryset = CoffeeCup.objects.all()


class CupAPI(generics.RetrieveAPIView):
    serializer_class = CoffeeCupSerializer
    queryset = CoffeeCup.objects.all()


class UserAPI(generics.RetrieveAPIView):
    serializer_class = CoffeeCupSerializer
    queryset = BaseUser.objects.all()
