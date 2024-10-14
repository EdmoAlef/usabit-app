from django.contrib import admin
from .models import Transacao, ContaBancaria
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_transacao', 'status', 'valor')
    list_filter = ('status', )

@admin.register(ContaBancaria)
class ContaBancariaAdmin(admin.ModelAdmin):
    list_display = ('titular', 'numero_conta', 'agencia', 'tipo_conta', 'saldo', 'data_abertura')
    list_filter = ('tipo_conta', )
    list_editable = ('numero_conta', 'agencia', 'saldo', 'tipo_conta')
    search_fields = ('titular', 'numero_conta', 'agencia')

    help_texts = {
        'titular': 'Nome do titular da conta.',
        'numero_conta': 'Número único da conta.',
        'agencia': 'Número da agência bancária.',
        'tipo_conta': 'Tipo de conta (Corrente, Poupança, etc.).',
        'saldo': 'Saldo atual da conta.',
        'data_abertura': 'Data em que a conta foi aberta.',
    }