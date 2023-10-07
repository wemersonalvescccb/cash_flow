from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.shortcuts import redirect
from django.urls import reverse

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Já existe um usuário')
        
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        
        url = reverse('login')
        return redirect(url)

def user_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        
        if user:
            login_django(request, user)
            url = reverse('base')
            return redirect(url)
        else:
            # Adicionar um trecho de código JavaScript para mostrar a modal de erro
            return render(request, 'login.html', {'show_error_modal': True})
        
def logout_view(request):
    logout(request)
    return redirect('base')
