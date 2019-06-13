from django.urls import path
from .views import background_view

urlpatterns = [
    path('',background_view,name='background_view'),
]
