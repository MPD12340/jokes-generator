from django.urls import path
from .views import generate_story

urlpatterns = [
    path("generate/", generate_story),
]
