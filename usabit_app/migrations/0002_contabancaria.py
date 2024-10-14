# Generated by Django 5.1.2 on 2024-10-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usabit_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContaBancaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.CharField(max_length=100)),
                ('numero_conta', models.CharField(max_length=20, unique=True)),
                ('agencia', models.CharField(max_length=10)),
                ('tipo_conta', models.CharField(choices=[('CC', 'Conta Corrente'), ('CP', 'Conta Poupança')], max_length=2)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('data_abertura', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
