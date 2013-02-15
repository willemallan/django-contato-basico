# -*- coding: utf-8 -*-
import datetime
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from contato.forms import ContatoForm

def contato(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContatoForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            
            # valores
            site = 'SITE CONTATO'
            destino = ['teste@teste.com.br',]

            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            
            context = {
                'site': site,
                'nome': nome,
                'email': email,
                'assunto': assunto,
                'mensagem': mensagem,
                'data': datetime.datetime.today,
            }

            email_message = render_to_string('contato.txt', context)
            from_email = "{0} <{1}>".format(site, settings.EMAIL_HOST_USER)
    
            # try:
            send_mail(u'{0} - {1}'.format(site, assunto), email_message, from_email, destino, fail_silently=False)
            form.save()            
            return render_to_response('sucesso.html', RequestContext(request))
    else:
        form = ContatoForm() # An unbound form

    return render(request, 'contato.html', {
        'form': form,
    })