from rest_framework.urls import path

from . import views

urlpatterns = [
    path('get_categories', views.get_categories, name='get_categories'),
    path('get_items', views.get_items, name='get_items'),
]