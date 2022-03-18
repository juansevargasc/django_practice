from django.urls import path
from . import views # imports from same root level

urlpatterns = [
    path('', views.index, name='index')
    
]