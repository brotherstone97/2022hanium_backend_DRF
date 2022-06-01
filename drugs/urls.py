from django.urls import path
from .views import get_db

urlpatterns = [
    path('all', get_db)
]
