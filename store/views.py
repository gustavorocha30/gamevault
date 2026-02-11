import json
import datetime
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout
from decouple import config

def home(request):
    # --- LÓGICA DE PAGAMENTO
    if request.GET.get('status') == 'success' and request.user.is_authenticated:
        # Pega o pedido ABERTO
        pedido = Pedido.objects.filter(cliente=request.user, completo=False).first()
        if pedido:
            pedido.completo = True 
            pedido.save()
        

    # Lógica de Busca
    query = request.GET.get('q') 
    if query:
        produtos = Produto.objects.filter(nome__icontains=query)
    else:
        produtos = Produto.objects.all()

    # Lógica do Carrinho
    carrinho_items = 0
    if request.user.is_authenticated:
        # Tenta pegar um pedido aberto, se não achar, cria um novo vazio
        pedido, created = Pedido.objects.get_or_create(cliente=request.user, completo=False)
        carrinho_items = pedido.get_cart_items 

    context = {'produtos': produtos, 'carrinho_items': carrinho_items}
    return render(request, 'home.html', context)

def cart(request):
    if request.user.is_authenticated:
        pedido, created = Pedido.objects.get_or_create(cliente=request.user, completo=False)
        itens = pedido.itempedido_set.all()
    else:
        itens = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'itens': itens, 'pedido': pedido}
    return render(request, 'cart.html', context)

def updateItem(request):
    data = json.loads(request.body)
    produtoId = data['produtoId']
    action = data['action']

    cliente = request.user
    produto = Produto.objects.get(id=produtoId)
    
    pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
    itemPedido, created = ItemPedido.objects.get_or_create(pedido=pedido, produto=produto)

    if action == 'add':
        itemPedido.quantidade = (itemPedido.quantidade + 1)
    elif action == 'remove':
        itemPedido.quantidade = (itemPedido.quantidade - 1)

    itemPedido.save()

    if itemPedido.quantidade <= 0:
        itemPedido.delete()

    return JsonResponse('Item atualizado com sucesso!', safe=False)

def processOrder(request):
    stripe.api_key = config('STRIPE_SECRET_KEY')

    if request.user.is_authenticated:
        cliente = request.user
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        items_carrinho = pedido.itempedido_set.all()

        line_items_stripe = []
        for item in items_carrinho:
            line_items_stripe.append({
                'price_data': {
                    'currency': 'brl', 
                    'product_data': {
                        'name': item.produto.nome,
                    },
                    'unit_amount': int(item.produto.preco * 100), 
                },
                'quantity': item.quantidade,
            })

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'], 
                line_items=line_items_stripe,
                mode='payment',
                success_url='http://127.0.0.1:8000/?status=success',
                cancel_url='http://127.0.0.1:8000/carrinho/?status=cancel',
            )
            return JsonResponse(checkout_session.url, safe=False)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse('Erro ao processar', safe=False)

def library(request):
    items_comprados = []
    
    if request.user.is_authenticated:
        # 1. Busca todos os pedidos FECHADOS do usuário
        pedidos_fechados = Pedido.objects.filter(cliente=request.user, completo=True)
        
        # 2. Percorre cada pedido e pega os itens dentro dele
        for pedido in pedidos_fechados:
            items = pedido.itempedido_set.all()
            for item in items:
                items_comprados.append(item)
    
    context = {'items': items_comprados}
    return render(request, 'library.html', context)

def signout(request):
    logout(request) # Encerra a sessão do usuário
    return redirect('home')