from django.urls import path
from api.views import CupAPI, CupsLessonsAPI, UserAPI

from .apps import ApiConfig

app_name = ApiConfig.name

urlpatterns = [
    path("lessons/", CupsLessonsAPI.as_view(), name="lessons"),
    path("lesson/<int:pk>/", CupAPI.as_view(), name="lesson"),
    path("user/<int:pk>/", UserAPI.as_view(), name="update"),
]
