from django.shortcuts import render,redirect
from .form import AuthUser
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
def inscription(request):
    if request.method =="POST":
        form = AuthUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('connexion')
    else:
        form = AuthUser()
    return render(request, 'auth_app/inscription.html', {'form':form})

def connexion(request):
    if request.method == 'POST':
        name = request.POST["name"]
        password = request.POST["password"]
        user= authenticate(request, name=name, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('accueil')
        else:
            messages.error(request, "nom ou mot de pass incorect")
    return render(request, 'auth_app/connexion.html')


@login_required
def deconnexion(request):
    logout(request)
    return redirect('connexion')