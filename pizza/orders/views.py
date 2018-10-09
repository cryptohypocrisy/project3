from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.utils import IntegrityError

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'orders/login.html', {'message': None})

    context = {
        'user': request.user
    }
    return render(request, 'orders/index.html', context)


def login_view(request):
    username = request.POST['login-username']
    password = request.POST['login-password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'orders/login.html', {'message': "Bad username or password"})

def logout_view(request):

    context = {
        'user': request.user, # need this to display a custom logout message to user
    }

    logout(request)
    return render(request, 'orders/logout.html', context, {'message': 'Logged out!'})


def signup_view(request):
    first_name = request.POST["signup-first_name"]
    last_name = request.POST["signup-last_name"]
    email = request.POST["signup-email"]
    password = request.POST["signup-password"]

    try:
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, email=email, password=password)
    except IntegrityError:
        return render(request, 'orders/login.html', {'message': 'Username already taken, pick another...'})

    return render(request, 'orders/newuser.html', {'message': 'Thanks for creating an account', 'user': first_name})
