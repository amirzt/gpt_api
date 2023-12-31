from rest_framework.urls import path

from . import views

urlpatterns = [
    path('create_conversation/', views.create_conversation, name='create_conversation'),
    path('get_conversation/', views.get_conversation, name='get_conversation'),
    path('update_conversation/', views.update_conversation, name='update_conversation'),
    path('delete_conversation/', views.delete_conversation, name='delete_conversation'),
    path('add_message/', views.add_message, name='add_message'),
    path('get_message/', views.get_message, name='get_message'),
    path('update_message/', views.update_message, name='update_message'),
    path('send_message_to_gpt/', views.send_message_to_gpt, name='send_message_to_gpt'),

]
