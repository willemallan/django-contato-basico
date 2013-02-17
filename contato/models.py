# -*- coding: utf-8 -*-
from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(verbose_name=u'Email',max_length=255)
    assunto = models.CharField(max_length=255)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True,editable=False)
    
    class Meta:
        ordering = ('-data',)
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __unicode__(self):
        return self.nome

class Email(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(verbose_name=u'Email',max_length=255)
    
    class Meta:
        ordering = ('nome',)
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __unicode__(self):
        return self.nome