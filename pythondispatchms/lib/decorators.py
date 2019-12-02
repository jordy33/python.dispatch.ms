# -*- coding: utf-8 -*-
"""The base Controller API."""
from tg import expose
from tg import redirect

class restErrorHandler(object):
    def __init__(self, error_handler = None):
        self.error_handler = error_handler

    def __call__(self, func):
        def dict_wrap(*args, **kw):
            passvalue=dict(func(*args, **kw))
            for key,value in passvalue.items():
                if 'error' in value:
                    return redirect('/error/restError?error='+value['error']+'&descript='+value['descript'])
            return passvalue
        res = expose("json")(dict_wrap)
        return res