from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.shortcuts import render
from .forms import Auth, Add
from .models import User
from django.template import loader
import jwt


def index(request):
    users = User.objects.all()
    template = loader.get_template('index.html')
    # return HttpResponse(template.render({'users': users}, request))
    return HttpResponse(users)


def auth(request):
    if request.method == 'POST':
        form = Auth(request.POST)
        if form.is_valid():
            print(request.POST)
            # process data & generate JWT
            # try:
            #    user = User.objects.get(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            # except User.DoesNotExist:
            #    raise Http404("Invalid username / password")

            if form.cleaned_data['username'] == "gibert" and form.cleaned_data['password'] == "coronavirus":
                payload = {
                    'id': 1,
                    'username': "gibert",
                }
                jwt_token = {'token': jwt.encode(payload, "SECRET_KEY_OF_THE_CORONAVIRUS")}

                # return HttpResponse(json.dump(jwt_token), status=200, content_type="application/json")
                response = HttpResponseRedirect('connected/')
                response.set_cookie('JWT', value=jwt_token['token'])
                return response

            else:
                return HttpResponseForbidden("Invalid username / password")

    form = Auth()
    return render(request, 'authentification.html', {'form': form})


def connected(request):
    jwt_token = request.COOKIES['JWT']
    payload = jwt.decode(jwt_token[2:-1], "SECRET_KEY_OF_THE_CORONAVIRUS")

    if payload['username'] != "gibert":
        return HttpResponseForbidden("Invalid username / password")

    html = "<html><head><head/><body>Liste des commentaires :<br>"
    for user in User.objects.all():
        html += "<li>" + str(user) + "</li>"
    html += "</body></html>"
    return HttpResponse(html)


def add(request):
    if request.method == 'POST':
        form = Add(request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'], password="", comment=form.cleaned_data['comment'])
            User.save(user)
    else:
        form = Add()

    return render(request, 'add.html', {'form': form})
