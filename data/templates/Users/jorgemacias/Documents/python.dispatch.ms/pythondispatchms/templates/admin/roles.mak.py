# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555371618.847684
_enable_loop = True
_template_filename = '/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/admin/roles.mak'
_template_uri = '/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/admin/roles.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        h = context.get('h', UNDEFINED)
        user = context.get('user', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<script type="text/javascript">\n$(document).ready(function () {\nfunction showUsersInRol(rol_name){\n                var winHeight = 400; //Math.round(window.innerHeight * .50)\n                var winWidth = 810;//Math.round(window.innerWidth * .50)\n                var grid_name_devices = \'jgGridRolUsers\';\n                var pager_name = "jqGridPagerRolUsers";\n                var grid_name_users_by_id = \'#\'+grid_name_devices;\n                var pager_name_by_id = \'#\'+pager_name;\n                if ($(grid_name_users_by_id).length){\n                    $(grid_name_users_by_id).remove();\n                    $(pager_name_by_id).remove();\n                }\n                if ($("#RolForm").length){\n                    $("#RolForm").remove();\n                }\n                var newDiv = $(document.createElement(\'div\'));\n                var html=\'<div id="RolForm" title="Filter">\'\n                html=html+\'<table id="\'+grid_name_devices+\'"></table> <div id="\'+pager_name+\'"> </div>\'\n                html=html+\'</div>\'\n                newDiv.html(html);\n\n                var createUsersSticky2 = newDiv.dialog({\n                    autoOpen: false,\n                    title: "Usuarios del Rol",\n                    height: winHeight - 20,\n                    width: winWidth,\n                    modal: true,\n                    close: function () {\n                    }\n                });\n                var grid = new jQuery(grid_name_users_by_id);\n                grid.jqGrid({\n                    url: \'')
        __M_writer(escape(h.url()))
        __M_writer('/admin/getUsersFromRole\'+\'?rolname=\'+rol_name,\n                    mtype: "GET",\n                    datatype: "json",\n                    page: 1,\n                    colModel: [\n                        {label: "Usuario", name: \'user\', key: true, width: 150},\n                    ],\n                    loadonce: true,\n                    viewrecords: true,\n                    width: 780,\n                    height: 250,\n                    rowNum: 10,\n                    pager: pager_name_by_id,\n                    ondblClickRow: function (rowId) {\n                    },\n\n                });\n                grid.navGrid(pager_name_by_id, {\n                    search: true,\n                    add: false,\n                    edit: false,\n                    del: false,\n                    refresh: true\n                }, {}, {}, {}, {});\n\n                createUsersSticky2.dialog("open");\n}\n\n\n    var cellsrenderer = function (row, column, value) {\n        return \'<div style="text-align: center; margin-top: 5px;">\' + value + \'</div>\';\n    }\n    var columnsrenderer = function (value) {\n        return \'<div style="text-align: center; margin-top: 5px;">\' + value + \'</div>\';\n    }\n    var bell = new Audio("')
        __M_writer(escape(tg.url('/sounds/ding.mp3')))
        __M_writer('");\n            var grid_name_email = \'#jgGridRoles\';\n            var grid_pager_email= \'#listRoles\';\n            var load_url=\'')
        __M_writer(escape(h.url()))
        __M_writer('/admin/loadRoles/?user=')
        __M_writer(escape(user))
        __M_writer("';\n            var update_url='")
        __M_writer(escape(h.url()))
        __M_writer('/admin/updateRoles/?user=')
        __M_writer(escape(user))
        __M_writer("';\n            //var header_container='")
        __M_writer(escape(_('Alerts')))
        __M_writer('\';\n            var addParams = {left: 0,width: window.innerWidth-700,top: 20,height: 255,url: update_url,mtype: \'GET\', closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var editParams = {left: 0,width: window.innerWidth-700,top: 20,height: 255,url: update_url,mtype: \'GET\',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,\n                    width: "500",\n                    editfunc: function (rowid) {\n                    }\n                };\n            var deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,mtype: \'GET\',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,mtype: \'GET\',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,mtype: \'GET\',closeAfterEdit: true,closeAfterSearch:true,url: update_url,modal: true, };\n            var grid = jQuery(grid_name_email);\n\n            $(document).ready(function () {\n                grid.jqGrid({\n                url: load_url,\n                datatype: \'json\',\n                mtype: \'GET\',\n                colNames: [\'')
        __M_writer(escape(_('Hidden')))
        __M_writer("', '")
        __M_writer(escape(_('Name')))
        __M_writer('\'],\n                colModel: [\n                    {name: \'id\',index: \'id\', width: 5,align: \'left\',key:true,hidden: true, editable: true,edittype: \'text\',editrules: {required: false}},\n                    {name: \'name\',index: \'name\', renderer: columnsrenderer, cellsrenderer: cellsrenderer, width: 5, align: \'center\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                ],\n                pager: jQuery(grid_pager_email),\n                rowNum: 10,\n                rowList: [10, 50, 100],\n                sortname: \'name\',\n                sortorder: "desc",\n                viewrecords: true,\n                autowidth: true,\n                height: 250,\n                ondblClickRow: function(rowId) {\n                    var rowData = jQuery("#jgGridRoles").getRowData(rowId);\n                    showUsersInRol(rowData[\'name\'])\n                },\n                //caption: header_container,\n            });\n            grid.jqGrid(\'navGrid\',grid_pager_email,{edit:false,add:false,del:true, search:false},\n                            editParams,\n                            addParams,\n                            deleteParams,\n                            searchParams,\n                            viewParams);\n            // add custom button\n            grid.navButtonAdd(grid_pager_email,\n                {\n                    buttonicon: "ui-icon-plus",\n                    title: "')
        __M_writer(escape(_('Add')))
        __M_writer('",\n                    caption: "')
        __M_writer(escape(_('Add')))
        __M_writer('",\n                    position: "first",\n                    onClickButton: addUserWindow\n                });\n            });\n            $.extend($.jgrid.nav,{alerttop:1});\n            function addUserWindow(){\n                $.ajax({\n                          type: "GET",\n                          url: \'')
        __M_writer(escape(h.url()))
        __M_writer('/admin/loadWizard\',\n                          contentType: "application/json; charset=utf-8",\n                          data: { \'name\':\'pythondispatchms.templates.admin.wizard_roles\',\'user\':\'')
        __M_writer(escape(user))
        __M_writer('\' },\n                          success: function(parameterdata) {\n                              var winHeight = 750; //Math.round(window.innerHeight * .50)\n                              var winWidth = 1200;//Math.round(window.innerWidth * .50)\n\n                              if ($("#addWizardForm").length){\n                                  $("#addWizardForm").remove();\n                              }\n                              var newDiv = $(document.createElement(\'div\'));\n\n                              newDiv.html(parameterdata.dedwizardtemplate);\n                              var DedicatedWizardDialog = newDiv.dialog({\n                                  autoOpen: false,\n                                  title: "')
        __M_writer(escape(_('Creación de Rol')))
        __M_writer('",\n                                  height: winHeight,\n                                  width: winWidth,\n                                  modal: true,\n                                  close: function() {\n                                      //$(\'#globalExpForm\')[0].reset();\n                                      //form[ 0 ].reset();\n                                      //allFields.removeClass( "ui-state-error" );\n                                  }\n                               });\n                              DedicatedWizardDialog.data(\'rowId\',1);\n                              DedicatedWizardDialog.dialog( "open" );\n                          },\n                          error: function() {\n                              alert("Error accessing wizard de Rol")\n                          },\n                          complete: function() {\n                          }\n                     });\n            }\n\n            // STOMP\n            var adminlistenerclient = Stomp.client(\'')
        __M_writer(escape(h.stompServer()))
        __M_writer('\');\n            adminlistenerclient.debug=null;\n            var listener_connect_callback = function() {\n                adminlistenerclient.subscribe("/topic/rolelistener", listener_subscribe_callback);\n                // called back after the client is connected and authenticated to the STOMP server\n              };\n            var listener_error_callback = function(error) {\n            };\n            var listener_subscribe_callback = function(message) {\n\n                var msg = message.body;\n                var payload = msg.split(\'|\');\n                var command = payload[0];\n                var data = payload[1];\n                switch (command) {\n                        case \'RELOAD\':\n                            $("#jgGridRoles").trigger( \'reloadGrid\' );\n                            $.alert("Reload", { autoClose:true,type: \'success\',});\n                            break;\n                        case \'NEW\':\n                            $("#jgGridRoles").trigger( \'reloadGrid\' );\n                            $.alert("New Role", { autoClose:true,type: \'success\',});\n                            bell.play();\n                            break;\n                        case \'MSG\':\n                            $.alert(data, { autoClose:false,type: \'success\',});\n                            bell.play();\n                            break;\n                }\n              };\n            // adminlistenerclient.connect(\'')
        __M_writer(escape(h.whoami()))
        __M_writer("', '")
        __M_writer(escape(h.password()))
        __M_writer("', listener_connect_callback, listener_error_callback, '/');\n            var stompUser='")
        __M_writer(escape(h.stompUser()))
        __M_writer("';\n            var stompPass='")
        __M_writer(escape(h.stompPassword()))
        __M_writer('\';\n            adminlistenerclient.connect(stompUser, stompPass, listener_connect_callback, listener_error_callback, \'/\');\n\n});\n</script>\n\n\n    <table style="width:100%">\n    <table id="jgGridRoles" class="scroll" cellpadding="0" cellspacing="0"></table>\n    <div id="listRoles" class="scroll" style="text-align:center;"></div>\n    <div id="listPsetcolsRoles" class="scroll" style="text-align:center;"></div>\n    </table>\n    <br>\n\n\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/admin/roles.mak", "line_map": {"64": 199, "70": 64, "17": 0, "26": 1, "27": 34, "28": 34, "29": 69, "30": 69, "31": 72, "32": 72, "33": 72, "34": 72, "35": 73, "36": 73, "37": 73, "38": 73, "39": 74, "40": 74, "41": 91, "42": 91, "43": 91, "44": 91, "45": 120, "46": 120, "47": 121, "48": 121, "49": 130, "50": 130, "51": 132, "52": 132, "53": 145, "54": 145, "55": 167, "56": 167, "57": 197, "58": 197, "59": 197, "60": 197, "61": 198, "62": 198, "63": 199}, "source_encoding": "utf-8", "filename": "/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/admin/roles.mak"}
__M_END_METADATA
"""
