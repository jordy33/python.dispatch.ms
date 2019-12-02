# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555372039.543328
_enable_loop = True
_template_filename = '/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/test/stepsExample.mak'
_template_uri = '/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/test/stepsExample.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        user = context.get('user', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<style type="text/css">\n</style>\n<script type="text/javascript">\n    function openWizardWindow(){\n                $.ajax({\n                          type: "GET",\n                          url: \'')
        __M_writer(escape(h.url()))
        __M_writer('/admin/loadWizard\',\n                          contentType: "application/json; charset=utf-8",\n                          data: { \'name\':\'pythondispatchms.templates.test.wizardLoadingSegment\',\'user\':\'')
        __M_writer(escape(user))
        __M_writer('\' },\n                          success: function(parameterdata) {\n                              //Insert HTML code\n                              //$( "#addAssignForm" ).html(parameterdata.expressionformtemplate);\n\n                              var winHeight = 750; //Math.round(window.innerHeight * .50)\n                              var winWidth = 1200;//Math.round(window.innerWidth * .50)\n\n                              if ($("#wizardForm").length){\n                                  $("#wizardForm").remove();\n                              }\n                              var newDiv = $(document.createElement(\'div\'));\n\n                              newDiv.html(parameterdata.dedwizardtemplate);\n                              var DedicatedWizardDialog = newDiv.dialog({\n                                  autoOpen: false,\n                                  title: "')
        __M_writer(escape(_('Wizard Example')))
        __M_writer('",\n                                  height: winHeight,\n                                  width: winWidth,\n                                  modal: true,\n                                  close: function() {\n                                      //$(\'#globalExpForm\')[0].reset();\n                                      //form[ 0 ].reset();\n                                      //allFields.removeClass( "ui-state-error" );\n                                  }\n                               });\n                              DedicatedWizardDialog.data(\'rowId\',1);\n                              DedicatedWizardDialog.dialog( "open" );\n                          },\n                          error: function() {\n                              alert("Error loaging Wizard")\n                          },\n                          complete: function() {\n                          }\n                     });\n            }\n</script>\n\n<input id="clickMe" type="button" value="clickme" onclick="openWizardWindow();" />\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "37": 31, "25": 1, "26": 7, "27": 7, "28": 9, "29": 9, "30": 25, "31": 25}, "uri": "/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/test/stepsExample.mak", "filename": "/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/test/stepsExample.mak"}
__M_END_METADATA
"""
