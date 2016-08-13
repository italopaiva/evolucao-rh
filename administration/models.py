# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class SingletonModel(models.Model):

    class Meta:
        abstract = True

    @classmethod
    def load(cls):
        return cls.objects.get()

class Company(SingletonModel):
    name = models.CharField(
        "Nome da Empresa",
        max_length=250,
        blank=False
    )
    owner = models.CharField(
        "Dono da empresa",
        max_length=50,
        blank=False
    )
    address = models.TextField(
        "Endereço da Empresa",
        help_text="Informe o endereço da empresa.",
        blank=False
    )
    phones = models.CharField(
        "Telefones da empresa",
        max_length=100,
        help_text="Informe os telefones da empresa. Pode utilizar barras, espaços e parêntesis, deixe o mais apresentável possível. Ex.: (48) 9 1234-5678 / (62) 9 9876-5432",
        blank=False
    )
    email = models.EmailField("E-mail da empresa", blank=False)
    description = models.TextField(
        "Descrição da Empresa",
        help_text="Este conteúdo irá aparecer na página 'Quem somos'. Este campo aceita código HTML. Por exemplo, utilize a tag &lt;br&gt; para quebrar linha (Texto &lt;br&gt; continuação do texto).",
        blank=False
    )
    facebook_page = models.TextField(
        "Página do Facebook",
        help_text="Informe a URL da sua página da empresa no Facebook.",
        blank=True
    )
    maps_url = models.TextField(
        "URL da localização da empresa (Google Maps)",
        help_text="Informe a URL do map a gerado pela API do Google Maps (apenas o campo src).",
        blank=True
    )

class StartPage(SingletonModel):
    title1 = models.CharField(
        "Título da foto",
        max_length=50,
        blank=False
    )
    description1 = models.TextField(
        "Descrição da foto",
        help_text="Este texto aparecerá embaixo do título na página inicial.",
        blank=False
    )
    pic1 = models.ImageField(
        "Foto 1",
        help_text="Submeta aqui a primeira foto para a página inicial.",
        upload_to='uploads/pictures/start_page/%Y/%m/%d/',
        blank=False
    )
    title2 = models.CharField(
        "Título da foto",
        max_length=50,
        blank=True
    )
    description2 = models.TextField(
        "Descrição da foto",
        help_text="Este texto aparecerá embaixo do título na página inicial.",
        blank=True
    )
    pic2 = models.ImageField(
        "Foto 2",
        help_text="Submeta aqui a segunda foto para a página inicial.",
        upload_to='uploads/pictures/start_page/%Y/%m/%d/',
        blank=True
    )
    title3 = models.CharField(
        "Título da foto",
        max_length=50,
        blank=True
    )
    description3 = models.TextField(
        "Descrição da foto",
        help_text="Este texto aparecerá embaixo do título na página inicial.",
        blank=True
    )
    pic3 = models.ImageField(
        "Foto 3",
        help_text="Submeta aqui a terceira foto para a página inicial.",
        upload_to='uploads/pictures/start_page/%Y/%m/%d/',
        blank=True
    )