# -*- coding: utf-8 -*-
"""Sample controller with all its actions protected."""
from tg import expose, flash,request,predicates,app_globals,response
from tg.i18n import ugettext as _, lazy_ugettext as l_
from pythondispatchms.lib.base import BaseController
from pythondispatchms.lib.decorators import restErrorHandler
from tg import RestController

import requests

from tg import app_globals
__all__ = ['LoraController']



class LoraController(RestController):

    @expose('json')
    def get_all(self):
        return dict(name='Boony', breed='Dog')

    @expose('json')
    def post(self, name, breed,number):
        print("POST Name: {} Breed: {} number: {}".format(name, breed, number))
        return dict(name=name, breed=breed)

    @expose('json')
    def put(self, name, breed):
        print("PUT Name: {} Breed: {}".format(name, breed))
        return dict(name=name, breed=breed)

    @expose('json')
    def post_delete(self, name, breed,number):
        print(response.body)
        print(response.status)
        print("DELETE Name: {} Breed: {} Number:{}".format(name, breed, number))
        return dict(name=name, breed=breed)



