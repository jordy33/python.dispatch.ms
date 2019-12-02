# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528997459.87289
_enable_loop = True
_template_filename = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/ecran.mak'
_template_uri = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/ecran.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<div id="Ecran">\n\t<table id="jqGrid"></table>\n\t<div id="jqGridPager"></div>\n</div>\n\n    <script type="text/javascript">\n        $(document).ready(function () {\n           $.jgrid.jqModal = $.jgrid.jqModal || {};\n$.extend(true, $.jgrid.jqModal, {toTop: true});\n\n$("#Ecran").dialog({\n    //dialogClass: \'Ecran\',\n    autoOpen: false,\n    width: 560,\n    height: 370,\n    modal: true,\n    open: function (event, ui) {\n        $("#jqGrid").jqGrid({\n            url: \'http://trirand.com/blog/phpjqgrid/examples/jsonp/getjsonp.php?callback=?&qwery=longorders\',\n            mtype: "GET",\n            datatype: "jsonp",\n            colModel: [\n                { label: \'OrderID\', name: \'OrderID\', key: true, width: 75 },\n                { label: \'Customer ID\', name: \'CustomerID\', width: 150 },\n                { label: \'Order Date\', name: \'OrderDate\', width: 150 },\n                { label: \'Freight\', name: \'Freight\', width: 150 },\n                { label:\'Ship Name\', name: \'ShipName\', width: 150 }\n            ],\n            cmTemplate: { width: 80, autoResizable: true },\n            autoResizing: { compact: true },\n            autoresizeOnLoad: true,\n            height: "auto",\n            viewrecords: true,\n            //width: 480,\n            height: "auto",\n            rowNum: 10,\n            pager: "#jqGridPager"\n        }).jqGrid("navGrid", { del: true, add: false, edit: false });\n    },\n    close:function () {}\n});\n$("#Ecran").dialog("open");\n\n        });\n\n   </script>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/ecran.mak", "filename": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/ecran.mak", "source_encoding": "utf-8"}
__M_END_METADATA
"""
