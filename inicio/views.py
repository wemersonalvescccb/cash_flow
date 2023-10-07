from django.shortcuts import render, redirect
from .forms import DateFilterForm  # Importe o formulário de filtro de data
from renda.models import Renda
from despesas.models import Despesas
from ativos.models import Ativos
from passivos.models import Passivos
from django.db.models import Sum
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
from django.contrib.auth.decorators import login_required

    

def base(args):
    return render(args, 'base.html')
    
@login_required(login_url='../usuario/login')
def inicio(request):
    form = DateFilterForm(request.GET)
    context = {}

    

    if form.is_valid():
        # Redireciona para a view 'dash'
        return redirect('inicio')

    context['form'] = form

    return render(request, 'inicio.html', context)

@login_required(login_url='../usuario/login')
def dash(request):
    start_date = request.session.get('start_date')
    end_date = request.session.get('end_date')
    
    if start_date is not None:
        data = datetime.strptime(start_date, "%Y-%m-%d")
        ano = data.strftime("%Y")  # Extrai o ano como string (por exemplo, "2023")
        mes = data.strftime("%B")
    else:
        # Lógica para lidar com start_date sendo None, se necessário
        ano = ""
        mes = ""
    
    renda_ativa = Renda.objects.filter(user=request.user, categoria_renda='ATIVA', data__range=(start_date, end_date))
    renda_passiva = Renda.objects.filter(user=request.user, categoria_renda='PASSIVA', data__range=(start_date, end_date))
    despesas = Despesas.objects.filter(user=request.user, data__range=(start_date, end_date))
    ativos = Ativos.objects.filter(user=request.user)
    passivos = Passivos.objects.filter(user=request.user)


    soma_renda_ativa = renda_ativa.aggregate(Sum('valor_renda'))['valor_renda__sum'] or Decimal('0.00')
    soma_renda_passiva = renda_passiva.aggregate(Sum('valor_renda'))['valor_renda__sum'] or Decimal('0.00')
    total_despesas = despesas.aggregate(Sum('valor_despesas'))['valor_despesas__sum'] or Decimal('0.00')
    total_ativos = ativos.aggregate(Sum('valor_ativos'))['valor_ativos__sum'] or Decimal('0.00')
    total_passivos = passivos.aggregate(Sum('valor_passivos'))['valor_passivos__sum'] or Decimal('0.00')

    soma_renda_total = Renda.objects.filter(user=request.user, data__range=(start_date, end_date)).aggregate(Sum('valor_renda'))['valor_renda__sum']
    soma_renda_total = soma_renda_total or Decimal('0.00')
    
    # Calcular dia de trabalho
    dia_trabalho = Decimal(soma_renda_total / 30)

    # Arredondar para duas casas decimais
    dia_trabalho = dia_trabalho.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    # Calcular hora de trabalho
    hora_trabalho = Decimal(dia_trabalho / 8)

    # Arredondar para duas casas decimais
    hora_trabalho = hora_trabalho.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    
    diferenca = soma_renda_total - total_despesas

    if total_despesas > 0 and soma_renda_total > 0:
        porcentagem_renda_passiva = (soma_renda_passiva / total_despesas) * 100
        porcentagem_renda = (total_despesas / soma_renda_total) * 100

        porcentagem_renda_passiva = Decimal(porcentagem_renda_passiva)
        porcentagem_renda = Decimal(porcentagem_renda)

        porcentagem_renda_passiva_int = int(porcentagem_renda_passiva)
        porcentagem_renda_int = int(porcentagem_renda)
    else:
        porcentagem_renda_passiva_int = 0
        porcentagem_renda_int = 0

    context = {
        'soma_renda_ativa': soma_renda_ativa,
        'soma_renda_passiva': soma_renda_passiva,
        'total_despesas': total_despesas,
        'porcentagem_renda_passiva_int': porcentagem_renda_passiva_int,
        'renda_total': soma_renda_total,
        'total_ativos': total_ativos,
        'total_passivos': total_passivos,
        'porcentagem_renda_int': porcentagem_renda_int,
        'start_date': start_date,
        'ano': ano,
        'mes': mes,
        'diferenca': diferenca,
        'dia_trabalho': dia_trabalho,
        'hora_trabalho': hora_trabalho,
    }

    form = DateFilterForm(request.GET)
    context['form'] = form

    return render(request, 'dash.html', context)