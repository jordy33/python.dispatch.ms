# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528997157.060791
_enable_loop = True
_template_filename = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/new.mak'
_template_uri = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/new.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n\n<html lang="en">\n\n<head>\n    <!-- The jQuery library is a prerequisite for all jqSuite products -->\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/new/jquery-1.11.0.js')))
        __M_writer('"></script>\n    <!-- We support more than 40 localizations -->\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/new/grid.locale-en.js')))
        __M_writer('"></script>\n    <!-- This is the Javascript file of jqGrid -->\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/new/jquery.jqgrid.src.js')))
        __M_writer('"></script>\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/new/jquery-ui.min.js')))
        __M_writer('"></script>\n    <!-- This is the localization file of the grid controlling messages, labels, etc.\n    <!-- A link to a jQuery UI ThemeRoller theme, more than 22 built-in and many more custom -->\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/new/jquery-ui.css')))
        __M_writer('" />\n    <!-- The link to the CSS that the grid needs -->\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/new/ui.jqgrid.css')))
        __M_writer('"  />\n        <link href="')
        __M_writer(escape(tg.url('/new/font-awesome.min.css')))
        __M_writer('" rel="stylesheet" />\n    <meta charset="utf-8" />\n    <title>jqGrid Loading Data - Million Rows from a REST service</title>\n</head>\n<body>\n\n<div id="Ecran">\n\t<table id="jqGrid"></table>\n\t<div id="jqGridPager"></div>\n</div>\n\n    <script type="text/javascript">\n        $(document).ready(function () {\n           $.jgrid.jqModal = $.jgrid.jqModal || {};\n$.extend(true, $.jgrid.jqModal, {toTop: true});\n\n$("#Ecran").dialog({\n    //dialogClass: \'Ecran\',\n    autoOpen: false,\n    width: 560,\n    height: 370,\n    modal: true,\n    open: function (event, ui) {\n        $("#jqGrid").jqGrid({\n            url: \'http://trirand.com/blog/phpjqgrid/examples/jsonp/getjsonp.php?callback=?&qwery=longorders\',\n            mtype: "GET",\n            datatype: "jsonp",\n            colModel: [\n                { label: \'OrderID\', name: \'OrderID\', key: true, width: 75 },\n                { label: \'Customer ID\', name: \'CustomerID\', width: 150 },\n                { label: \'Order Date\', name: \'OrderDate\', width: 150 },\n                { label: \'Freight\', name: \'Freight\', width: 150 },\n                { label:\'Ship Name\', name: \'ShipName\', width: 150 }\n            ],\n            cmTemplate: { width: 80, autoResizable: true },\n            autoResizing: { compact: true },\n            autoresizeOnLoad: true,\n            height: "auto",\n            viewrecords: true,\n            //width: 480,\n            height: "auto",\n            rowNum: 10,\n            pager: "#jqGridPager"\n        }).jqGrid("navGrid", { del: true, add: false, edit: false });\n    },\n    close:function () {}\n});\n$("#Ecran").dialog("open");\n\n        });\n\n   </script>\n\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"32": 15, "33": 15, "34": 17, "35": 17, "36": 18, "37": 18, "43": 37, "17": 0, "23": 1, "24": 7, "25": 7, "26": 9, "27": 9, "28": 11, "29": 11, "30": 12, "31": 12}, "uri": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/new.mak", "filename": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/new.mak", "source_encoding": "utf-8"}
__M_END_METADATA
"""
