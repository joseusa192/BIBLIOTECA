from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='lista_libros'),
    path('libro/<int:pk>/', views.libro_detail, name='libro_detail'),
]