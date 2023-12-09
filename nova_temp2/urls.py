from django.urls import path
from .views import home

urlpatterns = [
    # Diğer URL tanımları...
    path('', home, name='home'),
]
