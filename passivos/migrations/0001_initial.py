# Generated by Django 4.2.5 on 2023-09-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_passivos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fonte_passivos', models.CharField(max_length=255)),
                ('data', models.DateField()),
            ],
        ),
    ]
