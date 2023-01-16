from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Libro
from .forms import LibroForm

def book_list(request):
    libro = Libro.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, './libros/book_list.html',{'libro':libro})

def libro_detail(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/detalle_libro.html', {'libro': libro})

def form_book(request):
    form = LibroForm()
    return render(request, 'libros/book_edit.html',{'form':form})

def new_book(request): 
    if request.method=="POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.autor=request.user
            libro.published_date = timezone.now()
            libro.save()
            return redirect('libro_detail', pk=libro.pk)
    else: 
        form = LibroForm()
    return render(request, 'libros/book_edit.html', {'form':form})

def book_edit(request, pk): 
    libro = get_object_or_404(Libro, pk=pk)
    if request.method=="POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.autor=request.user
            libro.published_date = timezone.now()
            libro.save()
            return redirect('libro_detail', pk=libro.pk)
    else: 
        form = LibroForm(instance=libro)
    return render(request, 'libros/book_edit.html', {'form':form})
