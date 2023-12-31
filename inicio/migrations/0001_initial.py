# Generated by Django 4.2.5 on 2023-09-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renda', models.DecimalField(decimal_places=2, default=0.0, help_text='Renda mensal', max_digits=10)),
                ('despesas', models.DecimalField(decimal_places=2, default=0.0, help_text='Despesas mensais', max_digits=10)),
                ('ativos', models.DecimalField(decimal_places=2, default=0.0, help_text='Ativos financeiros', max_digits=10)),
                ('passivos', models.DecimalField(decimal_places=2, default=0.0, help_text='Passivos financeiros', max_digits=10)),
            ],
        ),
    ]
