from django.urls import path
from .views import home_

urlpatterns = [
    path('', home_, name='home'), 
]