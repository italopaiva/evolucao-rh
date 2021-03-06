# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-13 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nome da Empresa')),
                ('owner', models.CharField(max_length=50, verbose_name='Dono da empresa')),
                ('address', models.TextField(help_text='Informe o endere\xe7o da empresa.', verbose_name='Endere\xe7o da Empresa')),
                ('phones', models.CharField(help_text='Informe os telefones da empresa. Pode utilizar barras, espa\xe7os e par\xeantesis, deixe o mais apresent\xe1vel poss\xedvel. Ex.: (48) 9 1234-5678 / (62) 9 9876-5432', max_length=100, verbose_name='Telefones da empresa')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail da empresa')),
                ('description', models.TextField(help_text="Este conte\xfado ir\xe1 aparecer na p\xe1gina 'Quem somos'.", verbose_name='Descri\xe7\xe3o da Empresa')),
                ('facebook_page', models.TextField(blank=True, help_text='Informe a URL da sua p\xe1gina da empresa no Facebook.', verbose_name='P\xe1gina do Facebook')),
                ('maps_url', models.TextField(blank=True, help_text='Informe a URL do mapa gerado pela API do Google Maps (apenas o campo src).', verbose_name='URL da localiza\xe7\xe3o da empresa (Google Maps)')),
            ],
        ),
    ]
