from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('create/',views.create,name='create'),
    path('edit/<uuid:pk>',views.edit,name='edit'),
    path('delete/<uuid:pk>',views.delete,name='delete'),
    path('list/',views.list,name='list'),
]