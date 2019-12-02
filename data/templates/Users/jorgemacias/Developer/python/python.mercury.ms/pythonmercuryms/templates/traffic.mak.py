# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525388544.422323
_enable_loop = True
_template_filename = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/traffic.mak'
_template_uri = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/traffic.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<p>TRAFFIC</p>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"17": 0, "28": 22, "22": 1}, "source_encoding": "utf-8", "filename": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/traffic.mak", "uri": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/traffic.mak"}
__M_END_METADATA
"""
