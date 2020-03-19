from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .forms import Auth


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def auth(request):
    if request.method == 'POST':
        form = Auth(request.POST)
        if form.is_valid():
            # process data & generate JWT
            if form.username == 'secureUser' and form.password == 'coronavirus':
                print("coucou")

            return HttpResponseRedirect('/connected')

    else:
        form = Auth()

    return render(request, 'authentification.html', {'form': form})
