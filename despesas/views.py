from django.shortcuts import render, redirect, get_object_or_404
from .models import Despesas
from .forms import DespesasForm
from django.db.models import Sum
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from datetime import date, datetime


@login_required(login_url='../usuario/login')
def despesas(request):
    start_date = request.session.get('start_date')
    end_date = request.session.get('end_date')

    if start_date and end_date:
        despesas = Despesas.objects.filter(user=request.user, data__range=(start_date, end_date))
        soma_despesas_total = despesas.aggregate(Sum('valor_despesas'))['valor_despesas__sum']
    else:
        despesas = Despesas.objects.filter(user=request.user)
        soma_despesas_total = despesas.aggregate(Sum('valor_despesas'))['valor_despesas__sum']

    soma_despesas_total_float = float(soma_despesas_total) if soma_despesas_total is not None else 0.0

    return render(request, 'despesas.html', {'despesas': despesas, 'soma_despesas_total': soma_despesas_total_float})



@login_required(login_url='../usuario/login')
def cadastrar_despesas(request):
    if request.method == 'POST':
        form = DespesasForm(request.POST)
        if form.is_valid():
            despesas = form.save(commit=False)
            despesas.user = request.user  # Associe o usuário logado ao campo 'user'
            despesas.save()
            # Redirecione para a página 'inicio' com os dados atualizados
            return redirect('despesas')
    else:
        form = DespesasForm()

    return render(request, 'despesas.html', {'form': form})

@login_required(login_url='../usuario/login')   
def excluir_despesas(request, despesas_id):
    despesas = get_object_or_404(Despesas, pk=despesas_id, user=request.user)
    
    if request.method == 'POST':
        despesas.delete()
        return redirect('despesas')
    
    return render(request, 'despesas.html', {'despesas': despesas})



def dash_despesa(request):
    # Obtém as datas de início e fim do intervalo a partir da sessão (se disponíveis)
    start_date = request.session.get('start_date')
    end_date = request.session.get('end_date')

    # Verifica se as datas não foram especificadas e define-as para o ano atual
    if not start_date and not end_date:
        current_year = date.today().year
        start_date = datetime(current_year, 1, 1)
        end_date = datetime(current_year, 12, 31)

    # Filtra as despesas com base nas datas
    despesas = Despesas.objects.filter(user=request.user, data__range=(start_date, end_date))

    # Calcula o valor total das despesas
    soma_despesas_total = despesas.aggregate(Sum('valor_despesas'))['valor_despesas__sum']

    # Calcula o valor total de despesas por fonte_despesas para o usuário logado
    data = despesas.values('fonte_despesas').annotate(total=Sum('valor_despesas')).order_by('-total')

    return render(request, 'dash_despesa.html', {'data': data, 'soma_despesas_total': soma_despesas_total})
