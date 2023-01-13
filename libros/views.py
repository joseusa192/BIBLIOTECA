from django.shortcuts import render
from django.utils import timezone
from .models import Libro

def book_list(request):
    libro = Libro.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, './libros/book_list.html',{'libro':libro})
