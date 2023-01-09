from django.urls import path
from . import views

urlpatterns = [
    path('', views.issue, name='issue'),
    path('panel', views.panel, name='panel'),
    path('display', views.display, name='display'),
]
