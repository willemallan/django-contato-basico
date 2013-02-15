# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto')
    search_fields = ('nome', 'email', 'assunto')
    list_filter = ['data',]
    readonly_fields = ['nome', 'email', 'assunto', 'mensagem']
    save_on_top = True
    list_per_page = 20
    
admin.site.register(Contato, ContatoAdmin)