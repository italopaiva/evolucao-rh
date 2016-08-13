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
    answered = models.BooleanField(default=False)
    requester = models.CharField(
        "Nome do solicitante",
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

    def get_quantity(self):
        quantity = ""
        if self.quantity is 'None':
            quantity = "Nenhum"
        elif self.quantity is 11:
            quantity = "Mais de 10"
        else:
            quantity = self.quantity
        return quantity

    pretty_quantity = property(get_quantity)


class JoinUsRequest(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    answered = models.BooleanField(default=False)
    name = models.CharField(
        "Nome",
        max_length=50,
        validators=[
            validators.RegexValidator(
                r'^[a-zA-ZáéíóúàâêôãõüçÁÉÍÓÚÀÂÊÔÃÕÜÇ ]+$',
                "Ops, este não é um nome válido. Utilize somente caracteres alfabéticos."
            )
        ],
        blank=False
    )
    email = models.EmailField("E-mail", blank=False)
    phone = models.CharField(
        "Telefone",
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
    resume = models.FileField(
        "Currículo",
        help_text="Submeta aqui o seu currículo em '.PDF' ou '.DOC'.",
        upload_to='uploads/resumes/%Y/%m/%d/'
    )
