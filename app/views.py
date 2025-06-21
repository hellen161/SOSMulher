from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CadastroForm, DenunciaForm
from .models import RedeApoio
from .models import Alerta, AvaliacaoRisco
from .forms import AvaliacaoRiscoForm
from django.core.mail import send_mail

def alerta_rapido(request):
    alerta = Alerta.objects.create(usuario=request.user, localizacao="Não informado")
    send_mail(
        '🚨 Alerta SOS Mulheres',
        f'A usuária {request.user.username} acionou o alerta em {alerta.data}. Verificar situação imediatamente.',
        'sosmulheres@app.com',
        ['redeapoio@gmail.com'],
        fail_silently=False,
    )
    return render(request, 'alerta.html', {'alerta': alerta})


def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def denuncia(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.usuario = request.user
            denuncia.save()
            return redirect('home')
    else:
        form = DenunciaForm()
    return render(request, 'denuncia.html', {'form': form})

@login_required
def rede_apoio(request):
    redes = RedeApoio.objects.all()
    return render(request, 'rede_apoio.html', {'redes': redes})
@login_required
def alerta_rapido(request):
    alerta = Alerta.objects.create(usuario=request.user, localizacao="Não informado")
    return render(request, 'alerta.html', {'alerta': alerta})

@login_required
def avaliacao_risco(request):
    if request.method == 'POST':
        form = AvaliacaoRiscoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.save()
            risco = avaliacao.calcular_risco()
            return render(request, 'resultado_risco.html', {'risco': risco})
    else:
        form = AvaliacaoRiscoForm()
    return render(request, 'avaliacao.html', {'form': form})