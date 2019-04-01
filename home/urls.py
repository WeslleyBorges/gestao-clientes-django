from django.urls import path, include
from .views import home
from .views import my_logout

urlpatterns = [
    path('', home),
    path('logout/', my_logout, name='my_logout')
]
