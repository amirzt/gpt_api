from rest_framework.urls import path

from . import views

urlpatterns = [
    path('get_zarinpal_plan/', views.get_zarinpal_plan, name='get_zarinpal_plan'),
    path('get_googleplay_plan/', views.get_googleplay_plan, name='get_googleplay_plan'),
    path('get_appstore_plan/', views.get_appstore_plan, name='get_appstore_plan'),
    path('get_googleplay_code/', views.get_googleplay_code, name='get_googleplay_code'),
    path('get_appstore_code/', views.get_appstore_code, name='get_appstore_code'),
    path('get_zarinpal_url/', views.get_zarinpal_url, name='get_zarinpal_url'),
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify, name='verify'),
    path('get_admob/', views.get_admob, name='get_admob'),
    path('add_bazar_myket_order/', views.add_bazar_myket_order, name='add_bazar_myket_order'),

]
