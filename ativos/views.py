from django.shortcuts import render, redirect, get_object_or_404
from .models import Ativos
from .forms import AtivosForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required(login_url='../usuario/login')
def ativos(request):
    ativos = Ativos.objects.filter(user=request.user)
    soma_ativos_total = ativos.aggregate(Sum('valor_ativos'))['valor_ativos__sum']

    # O valor retornado será um objeto Decimal. Você pode convertê-lo em float se necessário.
    soma_ativos_total_float = float(soma_ativos_total) if soma_ativos_total is not None else 0.0
    return render(request, 'ativos.html', {'ativos': ativos, 'soma_ativos_total': soma_ativos_total_float})

@login_required(login_url='../usuario/login')    
def cadastrar_ativos(request):
    if request.method == 'POST':
        form = AtivosForm(request.POST)
        if form.is_valid():
            ativos = form.save(commit=False)
            ativos.user = request.user  # Associe o usuário logado ao campo 'user'
            ativos.save()
            # Redirecione para a página 'inicio' com os dados atualizados
            return redirect('ativos')
    else:
        form = AtivosForm()

    return render(request, 'ativos.html', {'form': form})

@login_required(login_url='../usuario/login')
def excluir_ativos(request, ativos_id):
    ativos = get_object_or_404(Ativos, pk=ativos_id, user=request.user)
    
    if request.method == 'POST':
        ativos.delete()
        return redirect('ativos')
    
    return render(request, 'ativos.html', {'ativos': ativos})
