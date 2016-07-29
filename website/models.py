# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import validators
from django.db import models

class Service(models.Model):
    name = models.CharField("Serviço", max_length=100)

    def __str__(self):
        return self.name

    SERVICES = [
        ('doorman', '1'),
        ('recepcionist', '2'),
        ('brigadist', '3'),
        ('cleaner', '4'),
        ('janitor', '5'),
        ('cupbearer', '6'),
        ('maid', '7'),
        ('gardener', '8'),
        ('pool_guy', '9'),
        ('driver', '10'),
        ('motoboy', '11'),
        ('parker', '12'),
    ]

class Budget(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    requester = models.CharField(
        "Solicitante",
        max_length=50,
        validators=[
            validators.RegexValidator(
                r'^[a-zA-ZáéíóúàâêôãõüçÁÉÍÓÚÀÂÊÔÃÕÜÇ ]+$',
                "Ops, este não é um nome válido. Utilize somente caracteres alfabéticos."
            )
        ],
        blank=False
    )
    requester_email = models.EmailField("E-mail do solicitante", blank=False)
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
        blank=False
    )
    requester_address = models.CharField(
        "Endereço do solicitante",
        max_length=100,
        help_text="Para quem ofereceremos esse serviço?!",
        blank=False
    )
    message = models.TextField("Mensagem/Detalhes", blank=True)

class BudgetService(models.Model):
    budget = models.ForeignKey(Budget)
    service = models.ForeignKey(Service)
    quantity = models.SmallIntegerField(validators=[validators.MaxValueValidator(11)])