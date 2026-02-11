from django.http import HttpResponse

def teste_view(request):
    return HttpResponse("essa é a rota de teste")
