from django.contrib import admin
from .models import Usuario, Denuncia, RedeApoio

admin.site.register(Usuario)
admin.site.register(Denuncia)
admin.site.register(RedeApoio)

# 6. views.py (Exemplo de view simples)
from django.shortcuts import render, redirect
from .models import Denuncia, RedeApoio
from .forms import DenunciaForm

def home(request):
    return render(request, 'home.html')

def denuncia(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DenunciaForm()
    return render(request, 'denuncia.html', {'form': form})

def rede_apoio(request):
    redes = RedeApoio.objects.all()
    return render(request, 'rede_apoio.html', {'redes': redes})