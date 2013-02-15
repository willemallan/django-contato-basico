django-contato-basico
=====================

Formulário de contato básico pronto

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