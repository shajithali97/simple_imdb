from django.http import  HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
# Create your views here.
def home(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'home.html',context)
def movie_detail(request,id):
    movie=Movie.objects.get(id=id)
    return render(request,'detail.html',{'movie':movie})

def add_movie(request):
    if request.method == "POST":
        m_name=request.POST.get('movie_name')
        m_desc=request.POST.get('desc')
        m_year=request.POST.get('year')
        m_img=request.FILES['img']
        movie=Movie(name=m_name,desc=m_desc,year=m_year,img=m_img)
        movie.save()
        return redirect('/')
    return render(request,'add.html')


def update_movie(request,id):
    movie=Movie.objects.get(id=id)

    form=MovieForm(request.POST or None,request.FILES,instance=movie)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST":
        movie.delete()
        return redirect('/')
    return render(request,'delete.html',{'movie':movie})