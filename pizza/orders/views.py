from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'orders/login.html', {'message': None})

    context = {
        'user': request.user
    }
    return render(request, 'orders/index.html', context)


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'orders/login.html', {'message': "Bad username or password"})

def logout_view(request):

    context = {
        'user': request.user,
    }

    logout(request)
    return render(request, 'orders/logout.html', context, {'message': 'Logged out!'})
