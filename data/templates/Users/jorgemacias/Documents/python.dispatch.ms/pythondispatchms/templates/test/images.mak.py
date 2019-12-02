# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555371641.961587
_enable_loop = True
_template_filename = '/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/test/images.mak'
_template_uri = '/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/test/images.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        list = context.get('list', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<style>\n    .container {\n        width: 500px;\n    }\n\n    .container img {\n        display: block;\n        width: 100%;\n        height: auto;\n    }\n</style>\n\n<ul>\n')
        for item in list:
            __M_writer('    <div class="container">\n  <li><img src="data:image/bmp;base64,')
            __M_writer(escape(item))
            __M_writer('" /></li>\n    </div>\n')
        __M_writer('</ul>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/test/images.mak", "line_map": {"17": 0, "34": 28, "23": 1, "24": 14, "25": 15, "26": 16, "27": 16, "28": 19}, "source_encoding": "utf-8", "filename": "/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/test/images.mak"}
__M_END_METADATA
"""
