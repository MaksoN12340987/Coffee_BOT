import logging
from rest_framework import serializers
from django.core.cache import cache

from cup_coffee.models import CoffeeCup
from users.models import BaseUser

logger_serializers_materials = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_serializers_materials.addHandler(file_handler)
logger_serializers_materials.setLevel(logging.INFO)


class CoffeeCupSerializer(serializers.ModelSerializer):
    # cup = cache.get("CoffeeCupSerializer_queryset")
    # if not cup:
    #     cup = serializers.SerializerMethodField()
    #     cache.set("CoffeeCupSerializer_queryset", cup, 60 * 15)

    class Meta:
        model = CoffeeCup
        fields = "__all__"


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ["username", "first_name", "last_name", "is_active", "groups"]
