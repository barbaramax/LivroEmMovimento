import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Voluntarios, AreaInteresse


@csrf_exempt
def cadastrar_voluntario(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        voluntario = Voluntarios.objects.create(
            nome=data.get('nome', ''),
            email=data.get('email', ''),
            telefone=data.get('telefone', ''),
        )

        areas = data.get('area_interesse', [])

        for area_nome in areas:

            area, created = AreaInteresse.objects.get_or_create(
                nome=area_nome
            )

            voluntario.area_interesse.add(area)

        return JsonResponse(
            {'mensagem': 'Voluntário cadastrado com sucesso!'},
            status=201
        )

    return JsonResponse(
        {'erro': 'Método não permitido'},
        status=405
    )