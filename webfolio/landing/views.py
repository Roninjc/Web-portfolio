from django.shortcuts import render


def landpage(request):
    return render(request, 'landing/landpO.html')
