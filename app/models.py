from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    localizacao = models.CharField(max_length=255, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Denuncia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    localizacao = models.CharField(max_length=255, blank=True)
    anonima = models.BooleanField(default=True)

    def __str__(self):
        return f'Denuncia {self.id} - {self.usuario.nome}'

class RedeApoio(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Alerta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensagem = models.CharField(max_length=255, default='Usuária acionou o alerta!')
    data = models.DateTimeField(auto_now_add=True)
    localizacao = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'Alerta {self.id} - {self.usuario.username}'

class AvaliacaoRisco(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    resposta_1 = models.BooleanField()
    resposta_2 = models.BooleanField()
    resposta_3 = models.BooleanField()
    resposta_4 = models.BooleanField()
    resposta_5 = models.BooleanField()
    data = models.DateTimeField(auto_now_add=True)

    def calcular_risco(self):
        respostas = [
            self.resposta_1, self.resposta_2,
            self.resposta_3, self.resposta_4, self.resposta_5
        ]
        risco = respostas.count(True)
        if risco >= 4:
            return "Alto Risco"
        elif risco >= 2:
            return "Médio Risco"
        else:
            return "Baixo Risco"

    def __str__(self):
        return f'Avaliação {self.id} - {self.usuario.username}'