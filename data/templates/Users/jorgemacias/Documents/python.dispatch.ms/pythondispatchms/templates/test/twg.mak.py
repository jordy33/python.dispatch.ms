# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555372036.960173
_enable_loop = True
_template_filename = '/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/test/twg.mak'
_template_uri = '/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/test/twg.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<script type="text/javascript" src="')
        __M_writer(escape(tg.url('/lib/tw2/dynforms.js')))
        __M_writer('" ></script>\n<link rel="stylesheet" type="text/css" href="')
        __M_writer(escape(tg.url('/lib/tw2/forms.css')))
        __M_writer('" media="all">\n\n\n<style type="text/css">\n</style>\n<script type="text/javascript">\n</script>\n\n<body id="movieform:page"><h1>Movie Example for TW2</h1><form onsubmit="twd_blank_deleted()" action="https://dispatch.dudewhereismy.mx/test/movie_submit" method="post" enctype="multipart/form-data" id="movieform:form">\n     <span class="error"></span>\n    <table id="movieform">\n    <tr class="odd required"  id="movieform:title:container">\n        <th><label for="title">Title</label></th>\n        <td >\n            <input name="movieform:title" type="text" value="" id="movieform:title"/>\n\n            <span id="movieform:title:error"></span>\n        </td>\n    </tr>\n    <tr class="even"  id="movieform:director:container">\n        <th><label for="director">Director</label></th>\n        <td >\n            <input name="movieform:director" type="text" id="movieform:director"/>\n\n            <span id="movieform:director:error"></span>\n        </td>\n    </tr>\n    <tr class="odd"  id="movieform:genres:container">\n        <th><label for="genres">Genres</label></th>\n        <td >\n            <ul id="movieform:genres">\n        <li>\n            <input type="checkbox" name="movieform:genres" value="1" id="movieform:genres:0"/>\n            <label for="movieform:genres:0">Action</label>\n        </li>\n        <li>\n            <input type="checkbox" name="movieform:genres" value="2" id="movieform:genres:1"/>\n            <label for="movieform:genres:1">Comedy</label>\n        </li>\n        <li>\n            <input type="checkbox" name="movieform:genres" value="3" id="movieform:genres:2"/>\n            <label for="movieform:genres:2">Romance</label>\n        </li>\n        <li>\n            <input type="checkbox" name="movieform:genres" value="4" id="movieform:genres:3"/>\n            <label for="movieform:genres:3">Sci-fi</label>\n        </li>\n</ul>\n\n            <span id="movieform:genres:error"></span>\n        </td>\n    </tr>\n    <tr class="even"  id="movieform:cast:container">\n        <th><label for="cast">Cast</label></th>\n        <td >\n            <table id="movieform:cast">\n    <tr>\n        <th>Character</th><th>Actor</th><th></th>\n        <td><input style="display:none" type="image" id="movieform:cast:undo" src="')
        __M_writer(escape(tg.url('/img/undo.png')))
        __M_writer('" title="Undo" alt="Undo" onclick="twd_grow_undo(this); return false;" /></td>\n    </tr>\n    <tr style="display:none;" id="movieform:cast:0" class="odd">\n    <td id="movieform:cast:0:character:container">\n        <input name="movieform:cast:0:character" type="text" onchange="twd_grow_add(this);" id="movieform:cast:0:character"/>\n    </td>\n    <td id="movieform:cast:0:actor:container">\n        <input name="movieform:cast:0:actor" type="text" onchange="twd_grow_add(this);" id="movieform:cast:0:actor"/>\n    </td>\n    <td id="movieform:cast:0:del:container">\n        <input src="')
        __M_writer(escape(tg.url('/img/del.png')))
        __M_writer('" style="display:none;" name="movieform:cast:0:del" value="" id="movieform:cast:0:del" onclick="twd_grow_del(this); return false;" alt="Delete row" type="image"/>\n    </td>\n    <td>\n    </td>\n</tr>\n<tr id="movieform:cast:1" class="even">\n    <td id="movieform:cast:1:character:container">\n        <input name="movieform:cast:1:character" type="text" onchange="twd_grow_add(this);" id="movieform:cast:1:character"/>\n    </td>\n    <td id="movieform:cast:1:actor:container">\n        <input name="movieform:cast:1:actor" type="text" onchange="twd_grow_add(this);" id="movieform:cast:1:actor"/>\n    </td>\n    <td id="movieform:cast:1:del:container">\n        <input src="')
        __M_writer(escape(tg.url('/img/del.png')))
        __M_writer('" style="display:none;" name="movieform:cast:1:del" value="" id="movieform:cast:1:del" onclick="twd_grow_del(this); return false;" alt="Delete row" type="image"/>\n    </td>\n    <td>\n    </td>\n</tr>\n</table>\n\n            <span id="movieform:cast:error"></span>\n        </td>\n    </tr>\n    <tr class="error"><td colspan="2">\n        <input name="movieform:id" type="hidden" id="movieform:id"/>\n        <span id="movieform:error"></span>\n    </td></tr>\n</table>\n\n\t\t<input onclick="return twd_no_multi_submit(this);" type="submit" value="Save"/>\n</form>\n<script type="text/javascript">document.onkeypress = twd_suppress_enter;</script></body>\n</html>\n<script type="text/javascript">document.onkeypress = twd_suppress_enter;</script></body>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 83, "33": 83, "39": 33, "17": 0, "23": 1, "24": 1, "25": 1, "26": 2, "27": 2, "28": 60, "29": 60, "30": 70, "31": 70}, "uri": "/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/test/twg.mak", "filename": "/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/test/twg.mak"}
__M_END_METADATA
"""
