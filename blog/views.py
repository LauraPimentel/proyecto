from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.forms import AlumnoForm
# from django.utils import timezone
# from .models import Post

def index(request):
    return render(request, 'registro/index.html')

def alumno_view(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('registro:index')
    else:
        form = AlumnoForm()
    return render(request, 'registro/alumno_form.html', {'form':form})

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})
