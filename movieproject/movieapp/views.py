from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import movie
from .forms import movieform
# Create your views here.
def index(request):
    movies=movie.objects.all()
    context={
        'movie_list':movies
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    film=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':film})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        discr=request.POST.get('discr',)
        year=request.POST.get('year',)
        image=request.FILES.get('image')
        Movie=movie(name=name,discr=discr,year=year,image=image)
        Movie.save()
        return redirect('/')
    return render (request,'add.html')
def update(request,id):
    Movie=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':Movie})
def delete(request,id):
    if request.method=='POST':
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')
