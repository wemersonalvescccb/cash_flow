from datetime import datetime

class DateFilterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifique se o filtro de datas está presente nos parâmetros GET
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if start_date and end_date:
            try:
                # Tente analisar as datas fornecidas
                datetime.strptime(start_date, '%Y-%m-%d')
                datetime.strptime(end_date, '%Y-%m-%d')

                # Se as datas forem válidas, armazene-as na sessão
                request.session['start_date'] = start_date
                request.session['end_date'] = end_date
            except ValueError:
                pass
        else:
            # Caso contrário, verifique se há um intervalo de anos especificado
            year = request.GET.get('year')
            if year:
                try:
                    # Tente analisar o ano fornecido
                    year = int(year)
                    # Defina as datas para o ano inteiro
                    request.session['start_date'] = f"{year}-01-01"
                    request.session['end_date'] = f"{year}-12-31"
                except ValueError:
                    pass

        response = self.get_response(request)
        return response
