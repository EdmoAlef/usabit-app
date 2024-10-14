from django.core.management.base import BaseCommand
from usabit_app.models import Transacao
from usabit_app.cotacao import converter_moeda
import asyncio
import pandas as pd

class Command(BaseCommand):
    
    help = 'Importação em massa de transações'

    def handle(self, *args, **options):
        caminho_arquivo = 'transacoes.xlsx'
        df = pd.read_excel(caminho_arquivo)
        
        for _, row in df.iterrows():
            valor = row['valor']
            
            if row['moeda'] != 'BRL': 
                try:
                    cotacao = asyncio.run(converter_moeda(row['moeda'], 'BRL'))
                    valor = valor * float(cotacao)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Erro ao converter moeda: {e}"))
                    continue

            transacao = Transacao(
                nome=row['nome'],
                descricao=row['descricao'],
                status=row['status'],
                data_transacao=row['data'],
                valor=valor,
            )
            transacao.save()
            self.stdout.write(self.style.SUCCESS(f"Transação de {row['nome']} salva com sucesso."))