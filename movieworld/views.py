from django.shortcuts import render, redirect
from .models import Movie


def view_list(request):
    bases = {'movies':Movie.objects.all()}
    return render(request, 'index.html', context=bases)

def add_movie(request):
    if request.method == "POST":
        post = request.POST.get
        file = request.FILES.get

        sarlavha = post("title")
        batafsil = post('description')
        rasm = file('poster')
        janri = post('genre')
        yil = post('year')

        Movie.objects.create(
            title = sarlavha,
            desc = batafsil,
            photo = rasm,
            janr = janri,
            year = yil
        )

        return redirect('home')
    return render(request, 'create.html')

def view_detail(request, pk):
    base = {'movie':Movie.objects.get(id=pk)}

    return render(request, 'detail.html', context=base)

def edit_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    base = {'movie':movie}

    if request.method == "POST":
        post = request.POST.get
        file = request.FILES.get

        sarlavha = post("title")
        batafsil = post('description')
        rasm = file('poster', movie.photo)
        janri = post('genre')
        yil = post('year')

        movie.title = sarlavha
        movie.desc = batafsil
        movie.photo = rasm
        movie.janr = janri
        movie.year = yil

        movie.save()
        return redirect('home')
    
    return render(request, 'update.html', context=base)


def remove_movie(request, pk):
    post = Movie.objects.get(id=pk)
    base = {'movie':post}

    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'delete.html', context=base)

    



        