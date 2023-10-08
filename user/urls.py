from rest_framework.urls import path

from user import views

urlpatterns = [
    path('get_user_info/', views.get_user_info, name='get_user_info'),
    path('splash/', views.splash, name='splash'),
    path('login/', views.login, name='login'),

]
