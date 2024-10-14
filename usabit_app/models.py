from django.db import models

# Create your models here.
class Transacao(models.Model):
    STATUS_TRANSACAO = [
        ('P', 'PENDENTE'),
        ('C', 'CONCLUIDO')
    ]
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_TRANSACAO, default='P')
    data_transacao = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) ->str:
        return self.nome

class ContaBancaria(models.Model):
    TIPO_CONTA = [
        ('CC', 'Conta Corrente'),
        ('CP', 'Conta Poupança')
    ]
    
    titular = models.CharField(max_length=100)
    numero_conta = models.CharField(max_length=20, unique=True)
    agencia = models.CharField(max_length=10)
    tipo_conta = models.CharField(max_length=2, choices=TIPO_CONTA)
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    data_abertura = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.titular} - {self.numero_conta}"
