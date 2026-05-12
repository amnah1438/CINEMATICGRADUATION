from django.urls import path
from . import views

urlpatterns = [
    path('',        views.display,   name='display'),
    path('form/',   views.form_view, name='form'),
    path('success/', views.success,  name='success'),
]
