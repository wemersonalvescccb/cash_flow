# Generated by Django 4.2.5 on 2023-09-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_despesas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fonte_despesas', models.CharField(max_length=255)),
                ('data', models.DateField()),
            ],
        ),
    ]
