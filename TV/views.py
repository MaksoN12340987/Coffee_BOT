import logging

from django.views.generic import (
    ListView,
)

from cup_coffee.models import CoffeeCup

logger_views = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_views.addHandler(file_handler)
logger_views.setLevel(logging.INFO)



class Tv_1(ListView):
    model = CoffeeCup
    template_name = "TV/TV_1.html"
    context_object_name = "coffee"

    def get_queryset(self):
        # Показываем только те напитки, у которых стоит флаг "Видно всем"
        return CoffeeCup.objects.filter(publication_flag=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = context['object_list']
        
        grouped_menu = {
            'espresso': [],
            'black': [],
            'milk': [],
            'cold': [],
            'tea': [],
            'signature': [],
            'dobav': [],
            'halva': [],
            'syrup': [],
            'signature_2': [],
            'kids': [],
            'cocoa': [],
            'other': []
        }

        # Раскладываем напитки по категориям
        for drink in queryset:
            if drink.category in grouped_menu:
                grouped_menu[drink.category].append(drink)
            else:
                grouped_menu['other'].append(drink)
                
        # Передаем сгруппированный словарь в шаблон
        context['menu'] = grouped_menu
        logger_views.info(context['menu'], context)
        return context


class Tv_2(ListView):
    model = CoffeeCup
    template_name = "TV/TV_2.html"
    context_object_name = "coffee"

    def get_queryset(self):
        # Показываем только те напитки, у которых стоит флаг "Видно всем"
        return CoffeeCup.objects.filter(publication_flag=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = context['object_list']
        
        grouped_menu = {
            'espresso': [],
            'black': [],
            'milk': [],
            'cold': [],
            'tea': [],
            'signature': [],
            'dobav': [],
            'halva': [],
            'syrup': [],
            'signature_2': [],
            'kids': [],
            'cocoa': [],
            'other': []
        }

        # Раскладываем напитки по категориям
        for drink in queryset:
            if drink.category in grouped_menu:
                grouped_menu[drink.category].append(drink)
            else:
                grouped_menu['other'].append(drink)
                
        # Передаем сгруппированный словарь в шаблон
        context['menu'] = grouped_menu
        logger_views.info(context['menu'], context)
        return context


class Tv_3(ListView):
    model = CoffeeCup
    template_name = "TV/TV_3.html"
    context_object_name = "coffee"

    def get_queryset(self):
        # Показываем только те напитки, у которых стоит флаг "Видно всем"
        return CoffeeCup.objects.filter(publication_flag=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = context['object_list']
        
        grouped_menu = {
            'espresso': [],
            'black': [],
            'milk': [],
            'cold': [],
            'tea': [],
            'signature': [],
            'dobav': [],
            'halva': [],
            'syrup': [],
            'signature_2': [],
            'kids': [],
            'cocoa': [],
            'other': []
        }

        # Раскладываем напитки по категориям
        for drink in queryset:
            if drink.category in grouped_menu:
                grouped_menu[drink.category].append(drink)
            else:
                grouped_menu['other'].append(drink)
                
        # Передаем сгруппированный словарь в шаблон
        context['menu'] = grouped_menu
        logger_views.info(context['menu'], context)
        return context


class Tv_4(ListView):
    model = CoffeeCup
    template_name = "TV/TV_4.html"
    context_object_name = "coffee"

    def get_queryset(self):
        # Показываем только те напитки, у которых стоит флаг "Видно всем"
        return CoffeeCup.objects.filter(publication_flag=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = context['object_list']
        
        grouped_menu = {
            'espresso': [],
            'black': [],
            'milk': [],
            'cold': [],
            'tea': [],
            'signature': [],
            'dobav': [],
            'halva': [],
            'syrup': [],
            'signature_2': [],
            'cocoa': [],
            'kids': [],
            'other': []
        }

        # Раскладываем напитки по категориям
        for drink in queryset:
            if drink.category in grouped_menu:
                grouped_menu[drink.category].append(drink)
            else:
                grouped_menu['other'].append(drink)
                
        # Передаем сгруппированный словарь в шаблон
        context['menu'] = grouped_menu
        logger_views.info(context['menu'], context)
        return context


class Test(ListView):
    model = CoffeeCup
    template_name = "TV/TEST.html"
    context_object_name = "coffee"
