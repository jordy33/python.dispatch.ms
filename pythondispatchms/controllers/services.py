# -*- coding: utf-8 -*-
"""Sample controller with all its actions protected."""
from tg import expose, flash
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.predicates import has_permission
from tg import predicates,require

from pythondispatchms.lib.base import BaseController

__all__ = ['ServicesController']


class ServicesController(BaseController):
    """Sample controller-wide authorization"""

    @expose('json')
    def listjson(self, **kw):
        lista = []
        #https://dispatch.dudewhereismy.mx/test/graph?user=jorge&app_name=Deployment&internal_id=1&application_id=1


        lista.append({'id': 400,
                      'name': ('Desplegado de Smartphones'),
                      'rows':1,
                      'cols':1,
                      'observations': ('Administración Smartphones'),
                      'perm': 'Admin Smartphones',
                      'open': 'Menu',
                      'url': '',
                      'sons' :[{
                         'id': 401,
                         'name': 'Listado de dispositivos',
                         'url': '/api',
                         'perm': 'Administrar SmartPhones',
                         'observations': ('Smartphones admin'),
                         'open': 'openTab',
                         'sons': '',
                         'icon': '<span class="glyphicon glyphicon-file"></span>'
                      }
                      ]
                      })


        return dict(list=lista, error="ok", planet_name="dispatch")