# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525365335.213355
_enable_loop = True
_template_filename = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/login.mak'
_template_uri = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/login.mak'
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
        login = context.get('login', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        came_from = context.get('came_from', UNDEFINED)
        login_counter = context.get('login_counter', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n  <h1>Login</h1>\n\n  <div class="row">\n    <div class="col-md-8 col-md-offset-1">\n      <form action="')
        __M_writer(escape(tg.url('/login_handler', params=dict(came_from=came_from, __logins=login_counter))))
        __M_writer('"\n            method="post" accept-charset="UTF-8" class="form-horizontal">\n        <div class="form-group">\n          <label class="col-sm-2 control-label">Username:</label>\n          <div class="col-sm-10">\n            <input class="form-control" type="text" name="login" value="')
        __M_writer(escape(login))
        __M_writer('"/>\n          </div>\n        </div>\n        <div class="form-group">\n          <label class="col-sm-2 control-label">Password:</label>\n          <div class="col-sm-10">\n            <input class="form-control" type="password" name="password"/>\n          </div>\n        </div>\n        <div class="form-group">\n          <div class="col-sm-10 col-sm-offset-2">\n            <div class="checkbox">\n              <label>\n                <input type="checkbox" name="remember" value="2252000" /> remember me\n              </label>\n            </div>\n          </div>\n        </div>\n        <div class="form-group">\n          <div class="col-sm-10 col-sm-offset-2">\n            <button type="submit" class="btn btn-default">Login</button>\n          </div>\n        </div>\n      </form>\n    </div>\n  </div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('Login Form')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/login.mak", "line_map": {"49": 2, "59": 53, "53": 2, "38": 1, "39": 2, "40": 7, "41": 7, "42": 12, "43": 12, "28": 0}, "source_encoding": "utf-8", "filename": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/login.mak"}
__M_END_METADATA
"""
