from django.urls import path

from . import views
urlpatterns = [
    path('',views.index),
    path('form',views.form_view),
    path('list',views.list_view),
    path('list/<str:_Id>/delete',views.delete_view),
]