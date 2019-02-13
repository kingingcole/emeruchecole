from django.shortcuts import render
from .models import Contact


# Create your views here.
def index(request):
    if request.method == 'POST':
        c = Contact()
        c.first_name = request.POST.get('name')
        c.last_name = request.POST.get('surname')
        c.email = request.POST.get('email')
        c.message = request.POST.get('message')
        c.save()
        context = {
            'data': 'data'
        }
        return render(request, 'main_site/index.html', context)
    else:
        return render(request, 'main_site/index.html')


def blermo(request):
    return render(request, 'main_site/blermo-work.html')

def movie_app(request):
    return render(request, 'main_site/movie-work.html')


def handler404(request):
    return render(request, 'main_site/404.html', status=404)


def handler500(request):
    return render(request, 'main_site/500.html', status=500)
