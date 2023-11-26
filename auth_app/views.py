from django.shortcuts import render,redirect
from .form import AuthUser
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Utilisateur


#pour l'inscription 
# def inscription(request):
#     if request.method =="POST":
#         form = AuthUser(request.POST)
#         if form.is_valid():
#             user = form.save()
#             print(f"Utilisateur créé : nom: {user.username} password :{user.password} email: {user.email}")
#             return redirect ('connexion')
#     else:
#         form = AuthUser()
#     return render(request, 'auth_app/inscription.html', {'form':form})

def inscription(request):
    if request.method == 'POST':
        form = AuthUser(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.email = form.cleaned_data['email']
            user = form.save()
            print(f"Utilisateur créé : nom: {user.username} password :{user.password} email: {user.email}")
            return redirect ('connexion')
    else:
        form = AuthUser()
    return render(request, 'auth_app/inscription.html', {'form': form})
            
# pour la connexion
def connexion(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        
        else:
            messages.error(request, "nom ou mot de pass incorect")
    return render(request, 'auth_app/connexion.html')

#pour la deconnexion
def deconnexion(request):
    logout(request)
    return redirect('connexion')

@login_required
def profile(request):
    return render(request, 'auth_app/deconnexion.html')


def liste_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    print(utilisateurs)
    return render(request, 'auth_app/listes.html', {'utilisateurs': utilisateurs})
