from rest_framework.urls import path

from support import views

urlpatterns = [
    path('get_instagram/', views.get_instagram, name='get_instagram'),
    path('get_email/', views.get_email, name='get_email'),
    path('get_telegram/', views.get_telegram, name='get_telegram'),
]
