# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555371373.070755
_enable_loop = True
_template_filename = '/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/master.mak'
_template_uri = '/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/master.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['bottom_scripts', 'content_wrapper', 'head_content', 'main_menu', 'meta', 'body_class', 'title', 'footer']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n<head>\n    ')
        __M_writer(escape(self.meta()))
        __M_writer('\n    <title>Application Wizard Bootstrap v3.x</title>\n    \t\t<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/lib/js/jquery-1.11.0.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/js/bootstrap.min.js')))
        __M_writer('"></script>\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/lib/js/grid.locale-es.js')))
        __M_writer('"></script>\n    <!-- This is the Javascript file of jqGrid -->\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/lib/js/jquery.jqgrid.src.js')))
        __M_writer('"></script>\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/lib/js/jquery-ui.min.js')))
        __M_writer('"></script>\n    <!-- This is the localization file of the grid controlling messages, labels, etc.\n    <!-- A link to a jQuery UI ThemeRoller theme, more than 22 built-in and many more custom -->\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/lib/css/jquery-ui.css')))
        __M_writer('" />\n    <!-- The link to the CSS that the grid needs -->\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/lib/css/ui.jqgrid.css')))
        __M_writer('"  />\n    <link href="')
        __M_writer(escape(tg.url('/lib/fonts/font-awesome.min.css')))
        __M_writer('" rel="stylesheet" />\n    <meta charset="utf-8" />\n    <title>dispatch</title>\n\n    <link href="')
        __M_writer(escape(tg.url('/lib/css/bootstrap.min.css')))
        __M_writer('" rel="stylesheet">\n    <script src="')
        __M_writer(escape(tg.url('/lib/stomp/stomp.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/moment/moment.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/js/alert.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/justgage/raphael-2.1.4.min.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/justgage/justgage.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/jqueryrotate/jQueryRotate.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/jquery-validation-1.17.0/dist/jquery.validate.js')))
        __M_writer('"></script>\n\n    <script src="')
        __M_writer(escape(tg.url('/lib/timepicker/jquery-ui-timepicker-addon.js')))
        __M_writer('"></script>\n\n    <style type="text/css">\n        input { box-shadow: 0 0 3px #CC0000; margin: 10px }\n\n        .dropdown {\n          background: rgba(255, 255, 255, 0.1);\n          float: left;\n          margin: 10px 8px;\n          padding: 0px;\n          border-radius: 4px;\n          list-style-type: none;}\n\n        .dropdown a.dropdown-toggle {\n          height: 40px;\n          width: 40px;\n          padding-top: 11px;\n          padding-left: 9px; }\n\n        .dropdown:hover {\n          color: #fff;\n          background: rgba(255, 255, 255, 0.2); }\n\n        .dropdown .label {\n          top: -4px;\n          left: 22px;\n          padding-top: 4px;\n          padding-bottom: 4px;\n          position: absolute;\n          border-radius: 9999px; }\n\n            .profile-sidebar {\n          padding: 10px 0;\n          border-bottom: 1px solid #e9ecf2; }\n        .label-success {\n          background-color: #8ad919; }\n        .label-danger {\n          background-color: #f9243f; }\n        .profile-userpic img {\n          float: left;\n          margin: 10px 0px 0px 15px;\n          width: 50px;\n          height: 50px;\n          border-radius: 9999px !important; }\n\n        .profile-usertitle {\n          float: left;\n          text-align: left;\n          margin: 10px 0 0 12px; }\n\n        .profile-usertitle-name {\n          font-size: 15px;\n          margin-bottom: 0px; }\n\n        .profile-usertitle-status {\n          text-transform: uppercase;\n          color: #AAA;\n          font-size: 10px;\n          font-weight: 600;\n          margin-bottom: 15px; }\n        .indicator {\n          width: 10px;\n          height: 10px;\n          display: inline-block;\n          border-radius: 9999px;\n          margin-right: 5px; }\n\n        .error { color: #F00; background-color: #f1f4f3; }\n        div.dialog-hidden { display:none}\n        html, body { margin: 0; padding: 0;}\n</style>\n    <!-- Global JavaScript -->\n    <script type="text/javascript">\n        function changeStateMessage(recordNumber){\n                $.ajax({\n                type: "GET",\n                url: "')
        __M_writer(escape(tg.url('/notification/updateBadge')))
        __M_writer('"+"?record="+recordNumber,\n                contentType: "application/json; charset=utf-8",\n                data: { \'param\':\'badge\' },\n                success: function(data) {\n                    // data.value is the success return json. json string contains key value\n                    $("#numeric_badge").text(data.badge);\n                },\n                error: function() {\n                    //alert("#"+ckbid);\n                    alert("Error accessing server notification/badge")\n                    },\n                complete: function() {\n                    }\n                });\n                $(\'#jqGridNot\').trigger( \'reloadGrid\' );\n        }\n        function logout() {\n            var i = document.childNodes.length - 1;\n            while (i >= 0) {\n              console.log(document.childNodes[i]);\n              document.removeChild(document.childNodes[i--]);\n            }\n            jQuery.ajax({\n                    type: "GET",\n                    url: "/secc",\n                    username: "logmeout",\n                    password: "123456",\n                    headers: { "Authorization": "Basic xxx" }\n            })\n            .done(function(){\n                // If we don\'t get an error, we actually got an error as we expect an 401!\n            })\n            .fail(function(){\n                // We expect to get an 401 Unauthorized error! In this case we are successfully\n                    // logged out and we redirect the user.\n                window.location = "/";\n            });\n\n            return false;\n        }\n        var username = \'dispatch\';\n        var password = \'managepass\';\n\n        function make_base_auth(user, password) {\n            var tok = user + \':\' + password;\n            var hash = btoa(tok);\n            return "Basic " + hash;\n        }\n        function doAjax(pageName,id) {\n                $.ajax({\n                    url:pageName ,\n                    error: function () {\n                        alert("Error de credenciales con otro planeta");\n                    },\n                    beforeSend: function(xhr){\n                    xhr.setRequestHeader("Content-Type","application/json");\n                    xhr.setRequestHeader("Accept","application/json");\n                    xhr.setRequestHeader( "Authorization", make_base_auth(username,password));\n                    },\n                    dataType: \'html\',\n                    data: { user: "')
        __M_writer(escape(h.whoami()))
        __M_writer('", id:id } ,\n                    success: function (data, rq) {\n                        $("#loader"+id).html(\'\');\n                         $("#"+id).html(data);\n                    },\n                    error: function (data, rq) {\n                        $("#"+id).html("<p>Error</p>");\n                    },\n                    type: \'GET\'\n                });\n        }\n        function loadIframe(url) {\n         $.ajax({\n\n            url: url,\n            type: "GET",\n             crossDomain: true,\n             xhrFields: {\n            withCredentials: true\n        },\n        beforeSend: function(xhr){\n                xhr.setRequestHeader("Content-Type","application/json");\n                xhr.setRequestHeader("Accept","application/json");\n                xhr.setRequestHeader( "Authorization", make_base_auth(username,password));\n        },\n            data: "user=')
        __M_writer(escape(h.whoami()))
        __M_writer('",\n            success: function (response) {\n                $("#iframe").attr(\'src\',"data:text/html;charset=utf-8," + escape(response));\n\n            },\n            error: function(xhr,textStatus,err)\n            {\n                console.log("readyState: " + xhr.readyState);\n                console.log("responseText: "+ xhr.responseText);\n                console.log("status: " + xhr.status);\n                console.log("text status: " + textStatus);\n                console.log("error: " + err);\n            }\n        });\n    }\n\n        function openWindow(url,text,id){\n            doAjax(url,id);\n            var $dialog = $(\'<div></div>\')\n               .html(\'<div id="\'+id+\'" style="margin:10px"></div>\')\n               .dialog({\n                   autoOpen: false,\n                   modal: true,\n                   height:  580,\n                   width: 820,\n                   resizable: false,\n                   draggable: true,\n                   position : { my: "center", at: "top", of: window },\n                   title: text,\n                   buttons: {\n                       "Close": function ()\n                       {\n                           $(this).dialog(\'destroy\').remove();\n                       }\n                   }\n               });\n        $dialog.dialog(\'open\');\n        }\n        function openTab(text,url) {\n                var num_tabs = $("div#tabs ul.main1 li.main1").length + 1;\n                var mytext= text;\n                var id = "frame"+num_tabs;\n                doAjax(url,id);\n                $("div#tabs ul.main1").append(\n                    "<li class=\'main1\'><a href=\'#tab"+num_tabs+"\'>"+mytext+"</a><span class=\'ui-icon ui-icon-close\' role=\'presentation\'>Remove Tab</span></li>"\n                );\n                $("div#tabs").append(\n                    "<div id=\'tab"+num_tabs+"\'> <div class=\'row\'><div class=\'col-lg-12\'><div id=\'"+id+"\' style=\'margin:10px\'></div><div id=\'loader"+id+"\' class=\'cygnus\'><span style=\'float:left;width: 20%;\'><p>Cargando ...</p></span><span style=\'float:right;width: 80%;\'><img src=')
        __M_writer(escape(tg.url('/img/ajax-loader.gif')))
        __M_writer('></span></div></div></div></div>"\n                );\n                var $head = $("#"+id).contents().find("head");\n\n                var ur="')
        __M_writer(escape(tg.url('/css/theme/jquery-ui1.css')))
        __M_writer('";\n                $head.append($("<link/>",\n                        { rel: "stylesheet", href:ur, type: "text/css" }\n                      ));\n\n                $("div#tabs").tabs("refresh").tabs(\'option\', \'active\', num_tabs - 1);\n        }\n        function notificationFmatter (cellvalue, options, rowObject)\n        {\n            var array = cellvalue.split(\',\');\n            if (rowObject[5]==\'Y\') {\n                html = \'<div class="media">\'+\n                            \'<div class="media-body">\' +\n                                \'<strong class="notification-title">\' +\n                                    \'<i class="\'+array[6]+\'"></i>&nbsp&nbsp\'+\n                                    \'<a style="color:#337ab7;text-decoration: none;" href="#">\'+\n                                        array[0]+\' </a>\'+\n                                        array[1]+\' <a style="color:#337ab7;text-decoration: none;" href="#">\'+\n                                        array[2]+\'</a></strong> \' +\n                                    \'<p class="notification-desc"></p>\'+\n                                        array[3]+\'</i><br>\'+\n                                        array[4]+\n                                        \'<br><small style="color: #777777;" class="timestamp">\'+\n                                        rowObject[2]+\'</small></p>\' +\n                            \'</div>\' +\n                        \'</div>\';\n            }\n                else\n            {\n                html = \'<div class="media">\'+\n                            \'<div class="media-body">\' +\n                                \'<strong class="notification-title">\' +\n                                    \'<i class="\'+array[6]+\'"></i>&nbsp&nbsp\'+\n                                    \'<a style="color:#337ab7;text-decoration: none;" href="#">\'+\n                                        array[0]+\' </a>\'+\n                                        array[1]+\' <a style="color:#337ab7;text-decoration: none;" href="#">\'+\n                                        array[2]+\'</a></strong> \' +\n                                    \'<p class="notification-desc"></p>\'+\n                                        array[3]+\'</i><br>\'+\n                                        array[4]+\n                                        \'<br><small style="color: #777777;" class="timestamp">\'+\n                                        rowObject[2]+\'</small></p>\' +\n                                        \'<input type = "button", value = "Dismiss" onclick = "changeStateMessage(\'+rowObject[0]+\')">\' +\n                            \'</div>\' +\n                        \'</div>\';\n            }\n            return html\n        }\n\n        $(document).ready(function () {\n\n            var ding = new Audio("')
        __M_writer(escape(tg.url('/sounds/ding.mp3')))
        __M_writer('");\n            document.getElementById(\'iframe\').setAttribute(\'height\',window.innerHeight*.65);\n\n            $("div#tabs").tabs();\n\n            $( "#tabs" ).tabs().on( "click", "span.ui-icon-close", function() {\n              var num_tabs = $("div#tabs ul li").length + 1;\n              var panelId = $( this ).closest( "li" ).remove().attr( "aria-controls" );\n              $( "#" + panelId ).remove();\n              $("div#tabs").tabs("refresh").tabs(\'option\', \'active\', num_tabs - 1);\n            });\n            function checkConnections(){\n                $.ajax({\n                type: "GET",\n                url: "')
        __M_writer(escape(tg.url('/rabbit/countsessions')))
        __M_writer('",\n                contentType: "application/json; charset=utf-8",\n                data: { \'user\':\'')
        __M_writer(escape(h.whoami()))
        __M_writer('\' },\n                success: function(data) {\n                    // data.value is the success return json. json string contains key value\n                    var instances = Number(data.count)\n                    if (instances>0){\n                      alert("El usuario esta conectado en otra session")  ;\n                      logout();\n                    }\n                    else {\n                         $("#online").show();\n                         $("#offline").hide();\n                    }\n\n                },\n                error: function() {\n                    //alert("#"+ckbid);\n                    alert("Error in /rabbit/countsessions")\n                    },\n                complete: function() {\n                    }\n                });\n                $(\'#jqGridNot\').trigger( \'reloadGrid\' );\n            }\n\n            //STOMP SETUP\n\n            var client = Stomp.client(\'')
        __M_writer(escape(h.stompServer()))
        __M_writer('\');\n            client.debug=null;\n            var connect_callback = function() {\n                client.subscribe("/topic/')
        __M_writer(escape(h.whoami()))
        __M_writer('", subscribe_callback);\n\n                //checkConnections();\n\n                // called back after the client is connected and authenticated to the STOMP server\n              };\n            var error_callback = function(error) {\n                $("#online").hide();\n                $("#offline").show();\n                 //logout();\n            };\n            var subscribe_callback = function(message) {\n\n                var msg = message.body;\n                var payload = msg.split(\'|\');\n                var command = payload[0];\n                var data = payload[1];\n                switch (command) {\n                        case \'MSG\':\n                            $.alert(data, { autoClose:false});\n                            ding.play();\n                            break;\n                        case \'NOT\':\n                            $.alert("Mensaje nuevo", { autoClose:true});\n                            $("#numeric_badge").text(data);\n                            $(\'#jqGridNot\').trigger( \'reloadGrid\' );\n                            ding.play();\n                            break;\n                }\n              };\n            client.connect(\'')
        __M_writer(escape(h.whoami()))
        __M_writer("', '")
        __M_writer(escape(h.password()))
        __M_writer('\', connect_callback, error_callback, \'/\');\n            $("#jqGridNot").jqGrid({\n                    url: \'/notification/loadNotification/\',\n                    datatype: \'json\',\n                    mtype: \'GET\',\n                    colNames: [ \'id\',\'')
        __M_writer(escape(_('user')))
        __M_writer("','")
        __M_writer(escape(_('time_stamp')))
        __M_writer("','")
        __M_writer(escape(_('Message')))
        __M_writer("','")
        __M_writer(escape(_('state')))
        __M_writer("','")
        __M_writer(escape(_('Message')))
        __M_writer('\'],\n                    colModel :[\n                        {name:\'id\', hidden: true , width:0},\n                        {name:\'user_id\', hidden: true , width:0},\n                        {name:\'time_stamp\', hidden: true , width:0},\n                        {name:\'message\',formatter:notificationFmatter},\n                        {name:\'attended_time\', hidden: true , width:0},\n                        {name:\'attended_state\', hidden: true , width:0},\n\n                    ],\n\n                    sortname: \'time_stamp\',\n                    sortorder: "desc",\n                    viewrecords: true, // show the current page, data rang and total records on the toolbar\n                    caption: "')
        __M_writer(escape(_('Notifications')))
        __M_writer('",\n                    height: 150,\n                    width: 446\n                });\n            });\n\n\n\t</script>\n\n    ')
        __M_writer(escape(self.head_content()))
        __M_writer('\n\n</head>\n\n')
        if tg.auth_stack_enabled:
            if h.whoami()=="":
                __M_writer('       <meta http-equiv="refresh" content="0; url=')
                __M_writer(escape(tg.url('/main')))
                __M_writer('" />\n')
            else:
                __M_writer('        <body class="')
                __M_writer(escape(self.body_class()))
                __M_writer('">\n          ')
                __M_writer(escape(self.main_menu()))
                __M_writer('\n          ')
                __M_writer(escape(self.footer()))
                __M_writer('\n        <!-- Insert nice scrool -->\n          ')
                __M_writer(escape(self.bottom_scripts()))
                __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bottom_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n <script type="text/javascript">\n\n </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_wrapper(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        str = context.get('str', UNDEFINED)
        self = context.get('self', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  ')

        flash=tg.flash_obj.render('flash', use_js=False)
          
        
        __M_writer('\n')
        if flash:
            __M_writer('    <script>$.alert("')
            __M_writer(escape(str(tg.flash_obj.pop_payload()['message'])))
            __M_writer('" ,{autoclose:false,type:\'info\',title:false});</script>\n')
        __M_writer('  ')
        __M_writer(escape(self.body()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <!-- INSERT MAIN MENU -->\n<nav>\n      <table style="width: 100%"  class=" ui-tabs-panel ui-corner-bottom ui-widget-content">\n          <td style="width: 5%">\n              <table>\n                  <tr>\n                      <td colspan="2">\n                          <div align="center" >\n                              <a class="navbar-brand" style="color:#a61a15" href="#"><span>')
        __M_writer(escape(_('Administration')))
        __M_writer('</span> <br><div>System</div></a>\n                          </div>\n                      </td>\n                  </tr>\n                  <tr>\n                      <td>\n                          <table>\n                              <td>\n                                  <li class="dropdown">\n                                     <a style="color:#a61a15" class="dropdown-toggle count-info" data-toggle="dropdown" href="#">\n                                      <em class="fa fa-bell"></em><span class="label label-info" id="numeric_badge">')
        __M_writer(escape(h.badge()))
        __M_writer('</span>\n                                     </a>\n                                     <ul class="dropdown-menu dropdown-alerts">\n                                      <table id="jqGridNot" class="scroll" cellpadding="0" cellspacing="0"></table>\n                                      <div id="jqGridNot" class="scroll" style="text-align:center;"></div>\n                                     </ul>\n                                  </li>\n                              </td>\n                              <td>\n                                  <div class="profile-usertitle">\n                                      <div class="profile-usertitle-name">')
        __M_writer(escape(h.whoami()))
        __M_writer('</div>\n                                      <div id="online" class="dialog-hidden">\n                                          <div class="profile-usertitle-status"><span class="indicator label-success"></span>Online</div>\n                                      </div>\n                                      <div id="offline" class="dialog-hidden">\n                                          <div class="profile-usertitle-status"><span class="indicator label-danger"></span>Offline</div>\n                                      </div>\n                                  </div>\n                              </td>\n                          </table>\n                      </td>\n\n                  </tr>\n              </table>\n          </td>\n          <td>\n              <ul class="nav nav-tabs ui-widget-header">\n                  <li class=active><a href="#pl11" aria-expanded=&#34;true&#34;>dispatch</a></li>\n                  <li><a href="#" onclick="logout()" style="color:#666"><em class="fa fa-power-off">&nbsp;</em>Logout</a></li>\n              </ul>\n              <div class="tab-content ui-tabs-panel ui-corner-bottom ui-widget-content">\n                      <div class="tab-pane fade in active" id="pl11" style="height:70px;padding: 10px">\n                         <button onclick="openTab(\'')
        __M_writer(escape(_('Traffic')))
        __M_writer("','")
        __M_writer(escape(h.url()))
        __M_writer('/traffic/index?groups=monitoristas\')" title="home of dispatch">')
        __M_writer(escape(_('Traffic')))
        __M_writer('</button>\n                          <button onclick="openTab(\'')
        __M_writer(escape(_('Listener Admin')))
        __M_writer("','")
        __M_writer(escape(h.url()))
        __M_writer('/admin/adminListener/\')" title="Listener">')
        __M_writer(escape(_('Listener Admin')))
        __M_writer('</button>\n                          <button onclick="openTab(\'')
        __M_writer(escape(_('Ded Mon')))
        __M_writer("','")
        __M_writer(escape(h.url()))
        __M_writer('/admin/dedicated/\')" title="Listener">')
        __M_writer(escape(_('Ded Mon')))
        __M_writer('</button>\n                          <button onclick="openTab(\'')
        __M_writer(escape(_('Roles')))
        __M_writer("','")
        __M_writer(escape(h.url()))
        __M_writer('/admin/roles/\')" title="Listener">')
        __M_writer(escape(_('Roles')))
        __M_writer('</button>\n                          <button onclick="openTab(\'')
        __M_writer(escape(_('csv')))
        __M_writer("','")
        __M_writer(escape(h.url()))
        __M_writer('/test/csv/\')" title="CSV">')
        __M_writer(escape(_('csv')))
        __M_writer('</button>\n                          <button onclick="openTab(\'')
        __M_writer(escape(_('pdf')))
        __M_writer("','")
        __M_writer(escape(h.url()))
        __M_writer('/test/pdf/\')" title="PDF">')
        __M_writer(escape(_('pdf')))
        __M_writer('</button>\n                          <button onclick="openTab(\'')
        __M_writer(escape(_('twg')))
        __M_writer("','")
        __M_writer(escape(h.url()))
        __M_writer('/test/twg/\')" title="TWG">')
        __M_writer(escape(_('Twg')))
        __M_writer('</button>\n                          <button onclick="openTab(\'')
        __M_writer(escape(_('Steps Example')))
        __M_writer("','")
        __M_writer(escape(h.url()))
        __M_writer('/test/stepsExample/\')" title="Listener">')
        __M_writer(escape(_('Steps Example')))
        __M_writer('</button>\n                          <button onclick="openTab(\'')
        __M_writer(escape(_('Traffic Graphs')))
        __M_writer("','")
        __M_writer(escape(h.url()))
        __M_writer('/traffic/monitorGraph\')" title="Listener">')
        __M_writer(escape(_('Traffic Graphs')))
        __M_writer('</button>\n                          <button onclick="openTab(\'')
        __M_writer(escape(_('Email Listener')))
        __M_writer("','")
        __M_writer(escape(h.url()))
        __M_writer('/admin/emailListener/\')" title="Listener">')
        __M_writer(escape(_('Email Listener')))
        __M_writer('</button>\n                          <button onclick="openTab(\'Log\',\'')
        __M_writer(escape(h.url()))
        __M_writer('/log/\')" title="home of dispatch">Log</button>\n                          <button onclick="openTab(\'Graph\',\'')
        __M_writer(escape(h.url()))
        __M_writer('/test/graph\')" title="home of earth">TeleGraph</button>\n                          <button onclick="openTab(\'Graph2\',\'')
        __M_writer(escape(h.url()))
        __M_writer('/traffic/monitorGraph\')" title="home of earth">Mon Graph</button>\n                          <button onclick="openTab(\'QR Codes\',\'')
        __M_writer(escape(h.url()))
        __M_writer('/traffic/qrGraph\')" title="home of earth">QR</button>\n                          <button onclick="openTab(\'Images\',\'')
        __M_writer(escape(h.url()))
        __M_writer('/test/images\')" title="Images">Base64</button>\n                          <button onclick="openTab(\'Messages\',\'')
        __M_writer(escape(h.url()))
        __M_writer('/test/messages\')" title="home of earth">Messages</button>\n                          <button onclick="openTab(\'Position\',\'')
        __M_writer(escape(h.url()))
        __M_writer('/test/telefonica\')" title="home of earth">Telefonica</button>\n                          <button onclick="openTab(\'')
        __M_writer(escape(_('Finalized Traffic')))
        __M_writer("','")
        __M_writer(escape(h.url()))
        __M_writer('/traffic/finalizedtraffic\')" title="home of dispatch">')
        __M_writer(escape(_('Finalized Traffic')))
        __M_writer('</button>\n                      </div>\n              </div>\n          </td>\n      </table>\n</nav>\n      <div id="tabs">\n          <ul class="nav nav-tabs ui-widget-header main1">\n            <li class="main1"><a href="#tabs-1" >Inicio</a></li>\n          </ul>\n          <div id="tabs-1" align="right">\n            ')
        __M_writer(escape(self.content_wrapper()))
        __M_writer('\n          </div>\n      </div>\n    <!-- End MENU -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        response = context.get('response', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <meta charset="')
        __M_writer(escape(response.charset))
        __M_writer('" />\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="description" content="Bootstrap 3 App">\n    <meta name="author" content="Jorge Macias & Maria Lacayo">\n    <meta name="keyword" content="Sun">\n    <meta name="viewport" content="initial-scale=1.0">\n    <meta charset="utf-8">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_class(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n   <!-- INSERT FOOTER -->\n    <div class="text-right">\n        <div class="credits">\n              <p>Copyright &copy; Madd Systems ')
        __M_writer(escape(h.current_year()))
        __M_writer('&nbsp;</p>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "26": 1, "27": 4, "28": 4, "29": 8, "30": 8, "31": 9, "32": 9, "33": 10, "34": 10, "35": 12, "36": 12, "37": 13, "38": 13, "39": 16, "40": 16, "41": 18, "42": 18, "43": 19, "44": 19, "45": 23, "46": 23, "47": 24, "48": 24, "49": 25, "50": 25, "51": 26, "52": 26, "53": 27, "54": 27, "55": 28, "56": 28, "57": 29, "58": 29, "59": 30, "60": 30, "61": 32, "62": 32, "63": 108, "64": 108, "65": 168, "66": 168, "67": 193, "68": 193, "69": 240, "70": 240, "71": 244, "72": 244, "73": 295, "74": 295, "75": 309, "76": 309, "77": 311, "78": 311, "79": 337, "80": 337, "81": 340, "82": 340, "83": 370, "84": 370, "85": 370, "86": 370, "87": 375, "88": 375, "89": 375, "90": 375, "91": 375, "92": 375, "93": 375, "94": 375, "95": 375, "96": 375, "97": 389, "98": 389, "99": 398, "100": 398, "101": 402, "102": 403, "103": 404, "104": 404, "105": 404, "106": 405, "107": 406, "108": 406, "109": 406, "110": 407, "111": 407, "112": 408, "113": 408, "114": 410, "115": 410, "116": 413, "117": 423, "118": 425, "119": 427, "120": 429, "121": 514, "122": 524, "123": 533, "129": 535, "133": 535, "139": 516, "146": 516, "147": 517, "151": 519, "152": 520, "153": 521, "154": 521, "155": 521, "156": 523, "157": 523, "158": 523, "164": 427, "173": 431, "180": 431, "181": 440, "182": 440, "183": 450, "184": 450, "185": 460, "186": 460, "187": 482, "188": 482, "189": 482, "190": 482, "191": 482, "192": 482, "193": 483, "194": 483, "195": 483, "196": 483, "197": 483, "198": 483, "199": 484, "200": 484, "201": 484, "202": 484, "203": 484, "204": 484, "205": 485, "206": 485, "207": 485, "208": 485, "209": 485, "210": 485, "211": 486, "212": 486, "213": 486, "214": 486, "215": 486, "216": 486, "217": 487, "218": 487, "219": 487, "220": 487, "221": 487, "222": 487, "223": 488, "224": 488, "225": 488, "226": 488, "227": 488, "228": 488, "229": 489, "230": 489, "231": 489, "232": 489, "233": 489, "234": 489, "235": 490, "236": 490, "237": 490, "238": 490, "239": 490, "240": 490, "241": 491, "242": 491, "243": 491, "244": 491, "245": 491, "246": 491, "247": 492, "248": 492, "249": 493, "250": 493, "251": 494, "252": 494, "253": 495, "254": 495, "255": 496, "256": 496, "257": 497, "258": 497, "259": 498, "260": 498, "261": 499, "262": 499, "263": 499, "264": 499, "265": 499, "266": 499, "267": 510, "268": 510, "274": 415, "279": 415, "280": 416, "281": 416, "287": 429, "296": 425, "300": 425, "306": 526, "311": 526, "312": 530, "313": 530, "319": 313}, "filename": "/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/master.mak", "uri": "/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/master.mak"}
__M_END_METADATA
"""
