# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1529001545.680694
_enable_loop = True
_template_filename = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/users.mak'
_template_uri = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/users.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<style type="text/css">\n</style>\n<script type="text/javascript">\n\n\n\n$(document).ready(function () {\nalternative()\nfunction alternative(){\n    $.jgrid.jqModal = $.jgrid.jqModal || {};\n\n    $.extend(true, $.jgrid.jqModal, {toTop: true});\n    var winWidth = 810;//Math.round(window.innerWidth * .50)\n    var winHeight = 400; //Math.round(window.innerHeight * .50)\n    var grid_name = \'#jgGrid\';\n    var pager_name = "#jqGridPager";\n    $.extend($.jgrid.nav,{alerttop:1});\n        var grid_name_html= grid_name.substr(1);\n        var pager_name_html=pager_name.substr(1);\n        if ($(grid_name).length){\n          $(grid_name).remove();\n          $(pager_name).remove();\n        }\n        var newDiv = $(document.createElement(\'div\'));\n        newDiv.html(\'<table id="\'+grid_name_html+\'"></table> <div id="\'+pager_name_html+\'"> </div>\');\n        //newDiv.html(\'<p>Hola</p>\');\n        var createUsersSticky = newDiv.dialog({\n            autoOpen: false,\n            height: winHeight - 20,\n            width: winWidth,\n            modal: true,\n            close: function () {\n                //form[ 0 ].reset();\n                //allFields.removeClass( "ui-state-error" );\n            }\n        });\n   $(document).ready(function () {\n\n        $(grid_name ).jqGrid({\n            url: \'test/data\',\n            mtype: "GET",\n            datatype: "json",\n            page: 1,\n            colModel: [\n                {label:"Order ID",sorttype: \'integer\',name: \'OrderID\',key: true,\twidth: 75,\tsearchrules : {\t"required": true,"number" : true,"minValue": 10200}},\n                {label:"Customer ID",name: \'CustomerID\',width: 150},\n                {label: "Order Date",name: \'OrderDate\',width: 150,sorttype:\'date\',\n                    searchoptions: {// dataInit is the client-side event that fires upon initializing the toolbar search field for a column\n                                    // use it to place a third party control to customize the toolbar\n                                    dataInit: function (element) {\n                            $(element).datepicker({\n                                id: \'orderDate_datePicker\',\n                                dateFormat: \'yy-mm-dd\',\n                                //minDate: new Date(2010, 0, 1),\n                                maxDate: new Date(2020, 0, 1),\n                                showOn: \'focus\'\n                            });\n                        }\n                    }\n                },\n                {label : "Ship Name",name: \'ShipName\',width: 150,searchoptions: {\n                        // dataInit is the client-side event that fires upon initializing the toolbar search field for a column\n                        // use it to place a third party control to customize the toolbar\n                        dataInit: function (element) {\n                            $(element).autocomplete({\n                                id: \'AutoComplete\',\n                                source: function(request, response){\n                                    this.xhr = $.ajax({\n                                        url: \'http://trirand.com/blog/phpjqgrid/examples/jsonp/autocompletep.php?callback=?&acelem=ShipName\',\n                                        data: request,\n                                        dataType: "jsonp",\n                                        success: function( data ) {\n                                            response( data );\n                                        },\n                                        error: function(model, response, options) {\n                                            response([]);\n                                        }\n                                    });\n                                },\n                                autoFocus: true\n                            });\n                        }\n                    }\n                },\n                {label: "Freight",sorttype: \'number\',name: \'Freight\', width: 150 }\n            ],\n            loadonce: true,\n            viewrecords: true,\n            width: 780,\n            height: 250,\n            rowNum: 10,\n            pager: "#jqGridPager"\n        });\n        // activate the build in search with multiple option\n        $(grid_name ).navGrid( pager_name, {\n            search: true, // show search button on the toolbar\n            add: false,\n            edit: false,\n            del: false,\n            refresh: true\n        },\n        {}, // edit options\n        {}, // add options\n        {}, // delete options\n        {\n            multipleSearch: true,\n\n\n        } // search options - define multiple search\n        );\n         createUsersSticky.dialog("open");\n    });\n\n\n}\n\n\n    });\n\n</script>\n\n\n  <!-- page end-->')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/users.mak", "filename": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/users.mak", "source_encoding": "utf-8"}
__M_END_METADATA
"""
