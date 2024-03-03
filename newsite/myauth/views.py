from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpRequest

# Create your views here.


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/admin/')
        else:
            error = 'Invalid login or password!'
            return render(request, 'myauth/login.html', {'error': error})
    else:
        if request.user.is_authenticated:
            return redirect('/admin/')
        return render(request, 'myauth/login.html')

