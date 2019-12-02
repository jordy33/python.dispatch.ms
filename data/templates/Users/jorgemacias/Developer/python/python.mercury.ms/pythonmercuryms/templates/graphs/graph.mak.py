# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1526571108.14219
_enable_loop = True
_template_filename = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/graphs/graph.mak'
_template_uri = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/graphs/graph.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        graph_data = context.get('graph_data', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<div class="container" align="left">\n\t  <embed id="algo" type="image/svg+xml" src=')
        __M_writer(escape(graph_data))
        __M_writer(" style='height:500px'/>\n</div>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/graphs/graph.mak", "source_encoding": "utf-8", "uri": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/graphs/graph.mak", "line_map": {"24": 2, "17": 0, "31": 25, "25": 2, "23": 1}}
__M_END_METADATA
"""
