from django.shortcuts import render, redirect, get_object_or_404
from .models import Renda
from .forms import RendaForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


@login_required(login_url='../usuario/login')
def renda(request):
    start_date = request.session.get('start_date')
    end_date = request.session.get('end_date')

    # Verifica se as datas estão presentes na sessão
    if start_date and end_date:
        # Filtra os dados de renda do usuário logado no intervalo de datas
        renda_data = Renda.objects.filter(user=request.user, data__range=(start_date, end_date))
        soma_renda_total = renda_data.aggregate(Sum('valor_renda'))['valor_renda__sum']
        # O valor retornado será um objeto Decimal. Você pode convertê-lo em float se necessário.
        soma_renda_total_float = float(soma_renda_total) if soma_renda_total is not None else 0.0
    else:
        # Se as datas não estiverem definidas na sessão, exiba todos os dados de renda do usuário logado
        renda_data = Renda.objects.filter(user=request.user)
        soma_renda_total = renda_data.aggregate(Sum('valor_renda'))['valor_renda__sum']
        soma_renda_total_float = float(soma_renda_total) if soma_renda_total is not None else 0.0

    return render(request, 'renda.html', {'renda': renda_data, 'soma_renda_total': soma_renda_total_float})

 
@login_required(login_url='../usuario/login')    
def cadastrar_renda(request):
    if request.method == 'POST':
        form = RendaForm(request.POST)
        if form.is_valid():
            # Crie uma instância do objeto de renda associada ao usuário logado
            renda = form.save(commit=False)
            renda.user = request.user  # Associe o usuário logado ao campo 'user'
            renda.save()
            # Redirecione para a página 'inicio' com os dados atualizados
            return redirect('renda')
    else:
        form = RendaForm()

    return render(request, 'renda.html', {'form': form})

@login_required(login_url='../usuario/login')
def excluir_renda(request, renda_id):
    renda = get_object_or_404(Renda, pk=renda_id, user=request.user)
    
    if request.method == 'POST':
        renda.delete()
        return redirect('renda')
    
    return render(request, 'renda.html', {'renda': renda})