from django.urls import path
from . import views

urlpatterns = [
    path('',          views.display,             name='display'),
    path('form/',     views.form_view,            name='form'),
    path('success/',  views.success,              name='success'),

    # لوحة الإدارة الجديدة
    path('panel/',    views.panel_view,           name='panel'),
    path('panel/logout/', views.panel_logout,     name='panel_logout'),

    # API
    path('api/settings/',              views.api_settings,          name='api_settings'),
    path('api/password/',              views.api_change_password,   name='api_password'),
    path('api/messages/',              views.api_messages,          name='api_messages'),
    path('api/messages/delete-all/',   views.api_message_delete_all,name='api_msg_del_all'),
    path('api/messages/<int:msg_id>/toggle/', views.api_message_toggle, name='api_msg_toggle'),
    path('api/messages/<int:msg_id>/delete/', views.api_message_delete, name='api_msg_delete'),
    path('api/upload/',                       views.api_upload,         name='api_upload'),
]
