django-contato-basico
=====================

Formulário de contato básico pronto

Edit `settings.py`, example::

    # -------------------------------------------------------------
    # EMAIL 
    # -------------------------------------------------------------

    EMAIL_HOST="smtp.gmail.com"
    EMAIL_PORT="587"
    EMAIL_HOST_USER="contato@teste.com.br"
    EMAIL_HOST_PASSWORD="123456"
    EMAIL_USE_TLS=True

Add `contato` to your `INSTALLED_APPS`, example::

    INSTALLED_APPS = (
        'contato',
    )

Add line to your `urls.py`, example::

    url(r'^contato/$', 'contato.views.contato', name='contato'),

Before::

    python manage.py syncdb

or with south::

    python manage.py schemamigration contato --initial
    python manage.py migrate