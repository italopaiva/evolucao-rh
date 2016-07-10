#coding=utf-8
from __future__ import unicode_literals

from django.core import validators
from django.db import models

class Service(models.Model):
    name = models.CharField("Serviço", max_length=100)

    def __str__(self):
        return self.name

class Budget(models.Model):
    requester = models.CharField(
        "Solicitante",
        max_length=50,
        validators=[
            validators.RegexValidator(
                r'^[a-zA-Z0-9\s+]+$',
                "Ops, este não é um nome válido. Utilize somente caracteres alfabéticos."
            )
        ]
    )
    requester_email = models.EmailField("E-mail do solicitante")
    requester_phone = models.CharField(
        "Telefone do solicitante",
        max_length=15,
        help_text="Use somente números.",
        validators=[
            validators.RegexValidator(
                r'^[0-9\s+]+$',
                "Ops, este não é um número válido. Utilize somente números."
            )
        ],
    )
    requester_address = models.CharField(
        "Endereço do solicitante",
        max_length=100,
        help_text="Para quem ofereceremos esse serviço?!",
        validators=[
            validators.RegexValidator(
                r'^[0-9\s+]+$',
                "Ops, este não é um número válido. Utilize somente números."
            )
        ],
    )
    message = models.TextField("Mensagem/Detalhes")