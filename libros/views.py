from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Libro

def book_list(request):
    libro = Libro.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, './libros/book_list.html',{'libro':libro})

def libro_detail(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/detalle_libro.html', {'libro': libro})
