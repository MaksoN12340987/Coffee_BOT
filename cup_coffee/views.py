import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CoffeeCreateForm, CoffeeUpdateForm
from .models import CoffeeCup

logger_views = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_views.addHandler(file_handler)
logger_views.setLevel(logging.INFO)


class ListCup(ListView):
    model = CoffeeCup
    template_name = "coffee/home.html"
    context_object_name = "coffee"


class DetailCup(DetailView):
    model = CoffeeCup
    template_name = "coffee/cup.html"
    context_object_name = "coffee"


class CreateCup(CreateView):
    model = CoffeeCup
    template_name = "coffee/create.html"
    form_class = CoffeeCreateForm
    success_url = reverse_lazy("cup_coffee:home")


class UpdateCup(LoginRequiredMixin, UpdateView):
    model = CoffeeCup
    template_name = "coffee/update.html"
    form_class = CoffeeUpdateForm
    success_url = reverse_lazy("bcup_coffeelog:home")


class DeleteCup(LoginRequiredMixin, DeleteView):
    model = CoffeeCup
    template_name = "coffee/delete.html"
    success_url = reverse_lazy("cup_coffee:home")
