# CASH_FLOW
# Gestão Financeira Inspirada em Pai Rico, Pai Pobre

Este projeto é uma aplicação web Django que ajuda as pessoas a melhorar suas finanças pessoais, seguindo os conselhos e princípios do livro "Pai Rico, Pai Pobre" de Robert Kiyosaki.

## Instruções de Instalação

1. Clone o repositório para o seu ambiente local:

    git clone https://github.com/wemersonalvescccb/cash_flow.git

    python -m venv myenv

    source myenv/bin/activate  
    ### No Windows: myenv\Scripts\activate

    pip install -r requirements.txt

    python manage.py migrate

    python manage.py runserver

## Acesse o projeto em seu navegador em http://localhost:8000/.


# Instruções de Uso
## Cadastrar Renda e Despesas
Após iniciar o servidor de desenvolvimento (conforme as instruções de instalação), acesse o projeto em seu navegador.

No painel principal, você verá opções para cadastrar sua renda e despesas para um mês específico. Insira os valores correspondentes aos seus ganhos mensais e despesas, conforme as orientações do livro "Pai Rico, Pai Pobre".

Certifique-se de selecionar o mês específico para o qual deseja registrar as transações financeiras.

## Dashboard Financeiro
No painel de controle, você pode filtrar os dados pelo mês desejado, que exibirá um resumo financeiro. Neste resumo, você encontrará:

Total de Renda: O montante total de sua renda para o mês selecionado.
Total de Despesas: O montante total de suas despesas para o mês selecionado.
Saldo Final: Quanto dinheiro sobrará no dia do pagamento, considerando sua renda e despesas.
Gráfico Comparativo: Um gráfico que compara suas despesas com sua renda. O objetivo é sempre gastar menos do que ganha.

## Renda Passiva
Um gráfico para visualizar seu progresso em relação à renda passiva. O objetivo é alcançar 100% de renda passiva para sair da "corrida dos ratos", como sugerido no livro.

Você pode adicionar fontes de renda passiva e atualizar seu progresso regularmente para acompanhar seu objetivo.

## Gestão Mensal
Use o projeto regularmente para acompanhar suas finanças mensais, inserindo suas transações de renda e despesas a cada mês.
Lembre-se de que esse projeto é uma ferramenta poderosa para aplicar os princípios financeiros do livro "Pai Rico, Pai Pobre" em sua vida financeira. Acompanhar sua renda, despesas e progresso em direção à renda passiva o ajudará a tomar decisões financeiras mais conscientes e a trabalhar em direção à independência financeira.