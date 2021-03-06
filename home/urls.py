from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/index.html'), name = 'home'),
    path('register/', views.register, name = 'register'),
]