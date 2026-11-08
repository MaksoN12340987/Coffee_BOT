from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin
from django.urls import path

from TV.apps import TVConfig
from api.apps import ApiConfig
from cup_coffee.apps import CupCoffeeConfig
from users.apps import UsersConfig

urlpatterns = [
    path(
        f"",
        include(f"{CupCoffeeConfig.name}.urls", namespace=f"{CupCoffeeConfig.name}"),
    ),
    path('admin/', admin.site.urls),
    path(
        f"{UsersConfig.name}/",
        include(f"{UsersConfig.name}.urls", namespace=f"{UsersConfig.name}"),
    ),
    path(
        f"{ApiConfig.name}/",
        include(f"{ApiConfig.name}.urls", namespace=f"{ApiConfig.name}"),
    ),
    path(
        f"{TVConfig.name}/",
        include(f"{TVConfig.name}.urls", namespace=f"{TVConfig.name}"),
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
