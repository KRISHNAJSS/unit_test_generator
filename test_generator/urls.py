from django.urls import path
from .views import generate_test

app_name = 'test_generator'

urlpatterns = [
    path('generate/', generate_test, name='generate_test'),
]
