# -*- coding: utf-8 -*-
from django.db import models

class Subscriber(models.Model):

    first_name = models.CharField(max_length=50, verbose_name='Имя', db_index=True)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', db_index=True)
    email = models.CharField(max_length=100, verbose_name='Адрес почты', db_index=True)
    birthday = models.CharField(max_length=10, verbose_name='Дата рождения')

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class EmailTemplate(models.Model):

    subject = models.CharField(max_length=300, verbose_name='Тема письма', db_index=True)
    content = models.TextField(verbose_name='Текст письма')


class Message(models.Model):

    recipient = models.ForeignKey('Subscriber')
    text = models.TextField(blank=True)
    opened = models.BooleanField(default=False)
