from django.urls import path
from .views import get_drug

urlpatterns = [
    path('all', get_drug)
]
