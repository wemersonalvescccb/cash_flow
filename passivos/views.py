from django.shortcuts import render, redirect, get_object_or_404
from .models import Passivos
from .forms import PassivosForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required(login_url='../usuario/login')
def passivos(request):
    passivos = Passivos.objects.filter(user=request.user)
    soma_passivos_total = passivos.aggregate(Sum('valor_passivos'))['valor_passivos__sum']

    # O valor retornado será um objeto Decimal. Você pode convertê-lo em float se necessário.
    soma_passivos_total_float = float(soma_passivos_total) if soma_passivos_total is not None else 0.0
    return render(request, 'passivos.html', {'passivos': passivos, 'soma_passivos_total': soma_passivos_total_float})

@login_required(login_url='../usuario/login')  
def cadastrar_passivos(request):
    if request.method == 'POST':
        form = PassivosForm(request.POST)
        if form.is_valid():
            passivos = form.save(commit=False)
            passivos.user = request.user  # Associe o usuário logado ao campo 'user'
            passivos.save()
            # Redirecione para a página 'inicio' com os dados atualizados
            return redirect('dash')
    else:
        form = PassivosForm()

    return render(request, 'passivos.html', {'form': form})

@login_required(login_url='../usuario/login')
def excluir_passivos(request, passivos_id):
    passivos = get_object_or_404(Passivos, pk=passivos_id, user=request.user)
    
    if request.method == 'POST':
        passivos.delete()
        return redirect('passivos')
    
    return render(request, 'passivos.html', {'passivos': passivos})
