from django.shortcuts import render

def book_list(request):
    return render(request, './libros/book_list.html',{})
