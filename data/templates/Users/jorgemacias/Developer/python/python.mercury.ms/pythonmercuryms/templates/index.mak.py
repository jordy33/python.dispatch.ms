# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528999578.159642
_enable_loop = True
_template_filename = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/index.mak'
_template_uri = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/index.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'local:templates.master', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n  <div class="row"><div class="col-md-8"><div id="iframe" style="margin:10px"><img src="')
        __M_writer(escape(tg.url('/img/freddie-dispatch-icon.png')))
        __M_writer('" style="width:50%;height:50%;" alt="Flowers in Chania"></div></div></div>\n <br>\n<br>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n  dispatch\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"34": 1, "35": 5, "36": 6, "37": 6, "43": 3, "28": 0, "53": 47, "47": 3}, "uri": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/index.mak", "filename": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/index.mak", "source_encoding": "utf-8"}
__M_END_METADATA
"""
