from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout

def cadastro(request):
    """ Esta função cuida do LOGIN do usuário """
    if request.method == 'POST':
        usuario_digitado = request.POST.get('username')
        senha_digitada = request.POST.get('password')

        # Autentica o usuário
        user = authenticate(request, username=usuario_digitado, password=senha_digitada)

        if user is not None:
            login(request, user)
            return redirect('home') # Redireciona para a página inicial da loja
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
            return redirect('login') # Recarrega a página de login com erro
            
    return render(request, 'usuarios/login.html')

def registrar(request):
    """ Esta função cuida da criação de NOVAS CONTAS """
    if request.method == 'POST':
        usuario = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm_password')

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem!')
        elif User.objects.filter(username=usuario).exists():
            messages.error(request, 'Este usuário já existe!')
        else:
            # Cria o usuário no banco de dados
            User.objects.create_user(username=usuario, email=email, password=senha)
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('login')

    return render(request, 'usuarios/registrar.html')


def logout_view(request):
    logout(request)
    return redirect('home')

def login_recrutador(request):
    user = authenticate(request, username='recrutador', password='teste1234')
    
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, 'O acesso de recrutador não está configurado.')
        return redirect('login')