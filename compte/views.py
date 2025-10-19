from django.forms import Form
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .forms import RegisterForm as UserRegistrationForm




User = get_user_model()

def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # pour activation ultérieure par email
            user.save()
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('login')
        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = UserRegistrationForm()  # formulaire vide pour GET

    return render(request, 'registration/register.html', {'register_form': form})


def user_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, "Connexion réussie.")
                return redirect('index')  # page d'accueil
            else:
                messages.error(request, "Votre compte n'est pas activé.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'restaurant/login.html')
