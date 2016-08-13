# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-13 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_auto_20160813_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='T\xedtulo da foto')),
                ('description', models.TextField(blank=True, help_text='Este texto aparecer\xe1 embaixo do t\xedtulo na p\xe1gina inicial.', verbose_name='Descri\xe7\xe3o da foto')),
                ('pic', models.ImageField(help_text='Submeta aqui a foto para a p\xe1gina inicial.', upload_to='uploads/pictures/start_page/%Y/%m/%d/', verbose_name='Foto')),
            ],
        ),
        migrations.RemoveField(
            model_name='startpage',
            name='description1',
        ),
        migrations.RemoveField(
            model_name='startpage',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='startpage',
            name='description3',
        ),
        migrations.RemoveField(
            model_name='startpage',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='startpage',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='startpage',
            name='title3',
        ),
        migrations.AlterField(
            model_name='startpage',
            name='pic1',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pic1', to='administration.Picture'),
        ),
        migrations.AlterField(
            model_name='startpage',
            name='pic2',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pic2', to='administration.Picture'),
        ),
        migrations.AlterField(
            model_name='startpage',
            name='pic3',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pic3', to='administration.Picture'),
        ),
    ]
