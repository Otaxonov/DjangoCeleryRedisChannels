from django.urls import path
from .views import JokesView

urlpatterns = [
    path('', JokesView, name='jokes')
]