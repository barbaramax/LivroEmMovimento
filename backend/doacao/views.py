import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Doacao

@csrf_exempt 
def receber_doacao(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Doacao.objects.create(
            nome=data.get('nome', ''),
            email=data.get('email', ''),
            telefone=data.get('telefone', ''),
            quantidade_livros=data.get('quantidade_livros', 0),
        )
        return JsonResponse({'mensagem': 'Doação registrada!'}, status=201)
    return JsonResponse({'erro': 'Método não permitido'}, status=405)