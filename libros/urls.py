from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='lista_libros'),
    path('libro/<int:pk>/', views.libro_detail, name='libro_detail'),
    path('libro/new/', views.new_book, name='new_book'),
    path('libro/<int:pk>/edit', views.book_edit, name='book_edit'),
]