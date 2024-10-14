# Importação de transações

Projeto para importar um arquivo de transações utilizando python com django

 # Instalação do Projeto

     git clone https://github.com/EdmoAlef/usabit-app
     
     cd usabit-app

     python3 manage.py migrate

     python3 manage.py runserver
     
Criando comando em python para importação de uma planilha de transações(xls)
> A Importação ler uma planilha de transações com valores, de acordo com a origem da moeda ele executa uma requisição de uma api externa para converter o valor da moeda para real

    python3 manage.py importa_planilha
