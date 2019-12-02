# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1529001359.434244
_enable_loop = True
_template_filename = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/master.mak'
_template_uri = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/master.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['content_wrapper', 'meta', 'bottom_scripts', 'title', 'body_class', 'footer', 'main_menu', 'head_content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n<head>\n    ')
        __M_writer(escape(self.meta()))
        __M_writer('\n    <link href="')
        __M_writer(escape(tg.url('/css/teststyles3.css')))
        __M_writer('" rel="stylesheet">\n    <!-- The jQuery library is a prerequisite for all jqSuite products -->\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/new/js/jquery-1.11.0.js')))
        __M_writer('"></script>\n    <!-- We support more than 40 localizations -->\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/new/js/grid.locale-es.js')))
        __M_writer('"></script>\n    <!-- This is the Javascript file of jqGrid -->\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/new/js/jquery.jqgrid.src.js')))
        __M_writer('"></script>\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/new/js/jquery-ui.min.js')))
        __M_writer('"></script>\n    <!-- This is the localization file of the grid controlling messages, labels, etc.\n    <!-- A link to a jQuery UI ThemeRoller theme, more than 22 built-in and many more custom -->\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/new/css/jquery-ui.css')))
        __M_writer('" />\n    <!-- The link to the CSS that the grid needs -->\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/new/css/ui.jqgrid.css')))
        __M_writer('"  />\n    <link href="')
        __M_writer(escape(tg.url('/new/fonts/font-awesome.min.css')))
        __M_writer('" rel="stylesheet" />\n    <meta charset="utf-8" />\n    <title>jqGrid Loading Data - Million Rows from a REST service</title>\n    <link href="')
        __M_writer(escape(tg.url('/new/css/bootstrap.min.css')))
        __M_writer('" rel="stylesheet">\n    <script src="')
        __M_writer(escape(tg.url('/new/stomp/stomp.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/new/moment/moment.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/new/js/alert.js')))
        __M_writer('"></script>\n\n<style>\n.cygnus {\n\n}\n</style>\n    <style type="text/css">\n\n    div.dialog-hidden { display:none}\n    html, body {\n        margin: 0;\n        padding: 0;\n        font-size:100%;\n    }\n    .main-table{\n        width:100%;\n        border-style: solid;\n        border-width: thin;\n        border-collapse: separate;\n        border-radius:5px;\n        padding-top: 1px;\n        padding-right: 1px;\n        padding-bottom: 1px;\n        padding-left: 1px;\n    }\n    .td-1{\n        padding: 3px;\n        alignment: left;\n        text-align: left;\n        width: 8px;\n    }\n    .td-last{\n        padding: 3px;\n        alignment: left;\n        text-align: left;\n    }\n\n    .second-table{\n        border-style: solid;\n        border-width: thin;\n        border-radius: 10px;\n    }\n\n    .ui-tabs {\n        padding: 0;\n    }\n        .ui-tabs-panel {\n        padding: 0;\n    }\n     .ui-tabs   .ui-tabs-panel {\n        padding: 0;\n    }\n     .ui-tabs .ui-tabs-nav .ui-tabs-anchor {\n    float: left;\n    padding: .2em 1em;\n    text-decoration: none;\n}\n.ui-state-active, .ui-widget-content .ui-state-active, .ui-widget-header .ui-state-active, a.ui-button:active, .ui-button:active, .ui-button.ui-state-active:hover{\ncolor:#ffffff;\n}\n\n\n\n/* DIEGO STYLE */\n\n        .btn{ font-size: 13px; /* Tamaño de la letra boton principal*/ }\n.dropdown-menu{\n    font-size: 13px; /* Tamaño de la los datos que se despliegan*/\n    min-width:10px; /* Largo minimo de los datos que se despliegan*/\n}\n\n.dropdown-menu> li> a\n{ display: inline;\n}\n\n.dropdown-submenu {\n    position: relative;\n}\n\n.dropdown-submenu .dropdown-menu {\n    top: 0;\n    left: 100%;\n    margin-top: -1px;\n}\n        .jqgrid-btn{\n        background: transparent;\n        border: none;\n        color: #333;\n    }\n    .myGridPager{\n        font-weight: normal;\n    }\n\n\n #map {\n        height: 400px;\n        width: 100%;\n       }\n\n\n\n/* DIEGO STYLE VENTANA EMERGENTE*/\n\n       .combo{\n\tfont-family: Tahoma, Verdana, Arial;\n\tfont-size: 11px;\n\tcolor: #707070;\n\tbackground-color: #FFFFFF;\n\tborder-width:0;\n}\n  .seccion {\n      width: 100%;\n      font-family: Georgia, "Times New Roman", Times, serif;\n      color: #ffffff;\n      background-color: #0a90b7eb }\n\n  .h1 {\n    font-family: Helvetica, Geneva, Arial, SunSans-Regular, sans-serif;\n\n\n  }\n\n       .bloque{\n           width: 28%;\n           background-color: lightgray;\n\n\n       }\n\n       .bloquelargo{\n           width: 25%;\n           background-color: lightgray;\n       }\n\n  #amap {\n        height: 400px;\n        width: 100%;\n       }\n\n  td.sombra{\n      background-color: #dddddd;\n\n  }\n\n  td.sombrafuerte{\n\n  background-color: #424242;\n  color: #ffffff;\n\n  }\n\n\n\n       .switch {\n\tposition: relative;\n\tdisplay: block;\n\tvertical-align: top;\n\twidth: 100px;\n\theight: 30px;\n\tpadding: 3px;\n\tmargin: 0 10px 10px 0;\n\tbackground: linear-gradient(to bottom, #eeeeee, #FFFFFF 25px);\n\tbackground-image: -webkit-linear-gradient(top, #eeeeee, #FFFFFF 25px);\n\tborder-radius: 18px;\n\tbox-shadow: inset 0 -1px white, inset 0 1px 1px rgba(0, 0, 0, 0.05);\n\tcursor: pointer;\n\tbox-sizing:content-box;\n}\n.switch-input {\n\tposition: absolute;\n\ttop: 0;\n\tleft: 0;\n\topacity: 0;\n\tbox-sizing:content-box;\n}\n.switch-label {\n\tposition: relative;\n\tdisplay: block;\n\theight: inherit;\n\tfont-size: 10px;\n\ttext-transform: uppercase;\n\tbackground: #eceeef;\n\tborder-radius: inherit;\n\tbox-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.12), inset 0 0 2px rgba(0, 0, 0, 0.15);\n\tbox-sizing:content-box;\n}\n.switch-label:before, .switch-label:after {\n\tposition: absolute;\n\ttop: 50%;\n\tmargin-top: -.5em;\n\tline-height: 1;\n\t-webkit-transition: inherit;\n\t-moz-transition: inherit;\n\t-o-transition: inherit;\n\ttransition: inherit;\n\tbox-sizing:content-box;\n}\n.switch-label:before {\n\tcontent: attr(data-off);\n\tright: 11px;\n\tcolor: #aaaaaa;\n\ttext-shadow: 0 1px rgba(255, 255, 255, 0.5);\n}\n.switch-label:after {\n\tcontent: attr(data-on);\n\tleft: 11px;\n\tcolor: #FFFFFF;\n\ttext-shadow: 0 1px rgba(0, 0, 0, 0.2);\n\topacity: 0;\n}\n.switch-input:checked ~ .switch-label {\n\tbackground: #E1B42B;\n\tbox-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.15), inset 0 0 3px rgba(0, 0, 0, 0.2);\n}\n.switch-input:checked ~ .switch-label:before {\n\topacity: 0;\n}\n.switch-input:checked ~ .switch-label:after {\n\topacity: 1;\n}\n.switch-handle {\n\tposition: absolute;\n\ttop: 4px;\n\tleft: 4px;\n\twidth: 28px;\n\theight: 28px;\n\tbackground: linear-gradient(to bottom, #FFFFFF 40%, #f0f0f0);\n\tbackground-image: -webkit-linear-gradient(top, #FFFFFF 40%, #f0f0f0);\n\tborder-radius: 100%;\n\tbox-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);\n}\n.switch-handle:before {\n\tcontent: "";\n\tposition: absolute;\n\ttop: 50%;\n\tleft: 50%;\n\tmargin: -6px 0 0 -6px;\n\twidth: 12px;\n\theight: 12px;\n\tbackground: linear-gradient(to bottom, #eeeeee, #FFFFFF);\n\tbackground-image: -webkit-linear-gradient(top, #eeeeee, #FFFFFF);\n\tborder-radius: 6px;\n\tbox-shadow: inset 0 1px rgba(0, 0, 0, 0.02);\n}\n.switch-input:checked ~ .switch-handle {\n\tleft: 74px;\n\tbox-shadow: -1px 1px 5px rgba(0, 0, 0, 0.2);\n}\n\n/* Transition\n========================== */\n.switch-label, .switch-handle {\n\ttransition: All 0.3s ease;\n\t-webkit-transition: All 0.3s ease;\n\t-moz-transition: All 0.3s ease;\n\t-o-transition: All 0.3s ease;\n}\n\n    </style>\n    <!-- Global JavaScript -->\n    <script type="text/javascript">\n        function changeStateMessage(recordNumber){\n                $.ajax({\n                type: "GET",\n                url: "')
        __M_writer(escape(tg.url('/notification/updateBadge')))
        __M_writer('"+"?record="+recordNumber,\n                contentType: "application/json; charset=utf-8",\n                data: { \'param\':\'badge\' },\n                success: function(data) {\n                    // data.value is the success return json. json string contains key value\n                    $("#numeric_badge").text(data.badge);\n                },\n                error: function() {\n                    //alert("#"+ckbid);\n                    alert("Error accessing server notification/badge")\n                    },\n                complete: function() {\n                    }\n                });\n                $(\'#jqGridNot\').trigger( \'reloadGrid\' );\n        }\n        function alogout() {\n            var i = document.childNodes.length - 1;\n            while (i >= 0) {\n              console.log(document.childNodes[i]);\n              document.removeChild(document.childNodes[i--]);\n            }\n            jQuery.ajax({\n                    type: "GET",\n                    url: "/secc",\n                    username: "logmeout",\n                    password: "123456",\n                    headers: { "Authorization": "Basic xxx" }\n            })\n            .done(function(){\n                // If we don\'t get an error, we actually got an error as we expect an 401!\n            })\n            .fail(function(){\n                // We expect to get an 401 Unauthorized error! In this case we are successfully\n                    // logged out and we redirect the user.\n                window.location = "/";\n            });\n\n            return false;\n        }\n        var username = \'dispatch\';\n        var password = \'managepass\';\n\n        function make_base_auth(user, password) {\n            var tok = user + \':\' + password;\n            var hash = btoa(tok);\n            return "Basic " + hash;\n        }\n        function doAjax(pageName,id) {\n                $.ajax({\n                    url:pageName ,\n                    error: function () {\n                        alert("Error de credenciales con otro planeta");\n                    },\n                    beforeSend: function(xhr){\n                    xhr.setRequestHeader("Content-Type","application/json");\n                    xhr.setRequestHeader("Accept","application/json");\n                    xhr.setRequestHeader( "Authorization", make_base_auth(username,password));\n                    },\n                    dataType: \'html\',\n                    data: { user: "')
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
        __M_writer('", subscribe_callback);\n\n                checkConnections();\n\n                // called back after the client is connected and authenticated to the STOMP server\n              };\n            var error_callback = function(error) {\n                $("#online").hide();\n                $("#offline").show();\n                 logout();\n            };\n            var subscribe_callback = function(message) {\n\n                var msg = message.body;\n                var payload = msg.split(\'|\');\n                var command = payload[0];\n                var data = payload[1];\n                switch (command) {\n                        case \'MSG\':\n                            $.alert(data, { autoClose:false});\n\n                            ding.play();\n                            break;\n                        case \'NOT\':\n                            $.alert("Mensaje nuevo", { autoClose:true});\n                            $("#numeric_badge").text(data);\n                            $(\'#jqGridNot\').trigger( \'reloadGrid\' );\n                            ding.play();\n                            break;\n                }\n              };\n            client.connect(\'')
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
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_wrapper(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        str = context.get('str', UNDEFINED)
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


def render_bottom_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n <script type="text/javascript">\n\n </script>\n')
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


def render_body_class(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
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


def render_main_menu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <!-- INSERT MAIN MENU -->\n<nav>\n      <table style="width: 100%"  class=" ui-tabs-panel ui-corner-bottom ui-widget-content">\n          <td style="width: 5%">\n              <table>\n                  <tr>\n                      <td colspan="2">\n                          <div align="center" >\n                              <a class="navbar-brand" style="color:#FDB813" href="#"><span>')
        __M_writer(escape(_('Administration')))
        __M_writer('</span> <br><div>System</div></a>\n                          </div>\n                      </td>\n                  </tr>\n                  <tr>\n                      <td>\n                          <table>\n                              <td>\n                                  <li class="dropdown">\n                                     <a style="color:#FDB813" class="dropdown-toggle count-info" data-toggle="dropdown" href="#">\n                                      <em class="fa fa-bell"></em><span class="label label-info" id="numeric_badge">')
        __M_writer(escape(h.badge()))
        __M_writer('</span>\n                                     </a>\n                                     <ul class="dropdown-menu dropdown-alerts">\n                                      <table id="jqGridNot" class="scroll" cellpadding="0" cellspacing="0"></table>\n                                      <div id="jqGridNot" class="scroll" style="text-align:center;"></div>\n                                     </ul>\n                                  </li>\n                              </td>\n                              <td>\n                                  <div class="profile-usertitle">\n                                      <div class="profile-usertitle-name">')
        __M_writer(escape(h.whoami()))
        __M_writer('</div>\n                                      <div id="online" class="dialog-hidden">\n                                          <div class="profile-usertitle-status"><span class="indicator label-success"></span>Online</div>\n                                      </div>\n                                      <div id="offline" class="dialog-hidden">\n                                          <div class="profile-usertitle-status"><span class="indicator label-danger"></span>Offline</div>\n                                      </div>\n\n                                  </div>\n                              </td>\n                          </table>\n                      </td>\n\n                  </tr>\n              </table>\n          </td>\n          <td>\n              <ul class="nav nav-tabs ui-widget-header">\n                  <li class=active><a href="#pl11" aria-expanded=&#34;true&#34;>Earth</a></li>\n                  <li><a href="#" onclick="logout()" style="color:#666"><em class="fa fa-power-off">&nbsp;</em>Logout</a></li>\n              </ul>\n              <div class="tab-content ui-tabs-panel ui-corner-bottom ui-widget-content">\n                      <div class="tab-pane fade in active" id="pl11" style="height:70px;padding: 10px">\n                         <button onclick="openTab(\'Traffic\',\'')
        __M_writer(escape(h.url()))
        __M_writer('/traffic/index\')" title="home of earth">Traffic</button>\n                          <button onclick="openTab(\'Listener Admin\',\'')
        __M_writer(escape(h.url()))
        __M_writer('/admin/listener/\')" title="Listener">Listener Admin</button>\n                         <button onclick="openTab(\'Graph\',\'')
        __M_writer(escape(h.url()))
        __M_writer('/test/graph\')" title="home of earth">Graph</button>\n                          <button onclick="openTab(\'Users\',\'')
        __M_writer(escape(h.url()))
        __M_writer('/test/users\')" title="home of earth">Users</button>\n                           <button onclick="openTab(\'Ecran\',\'')
        __M_writer(escape(h.url()))
        __M_writer('/test/ecran\')" title="home of earth">Ecran</button>\n                          <button onclick="openTab(\'Stomp\',\'')
        __M_writer(escape(h.url()))
        __M_writer('/test/websockets\')" title="home of earth">Stomp</button>\n                      </div>\n              </div>\n          </td>\n      </table>\n</nav>\n      <div id="tabs">\n          <ul class="nav nav-tabs ui-widget-header main1">\n            <li class="main1"><a href="#tabs-1" >Inicio</a></li>\n          </ul>\n          <div id="tabs-1" align="right">\n            ')
        __M_writer(escape(self.content_wrapper()))
        __M_writer('\n          </div>\n      </div>\n    <!-- End MENU -->\n\n\n')
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


"""
__M_BEGIN_METADATA
{"line_map": {"17": 0, "26": 1, "27": 4, "28": 4, "29": 5, "30": 5, "31": 7, "32": 7, "33": 9, "34": 9, "35": 11, "36": 11, "37": 12, "38": 12, "39": 15, "40": 15, "41": 17, "42": 17, "43": 18, "44": 18, "45": 21, "46": 21, "47": 22, "48": 22, "49": 23, "50": 23, "51": 24, "52": 24, "53": 289, "54": 289, "55": 349, "56": 349, "57": 374, "58": 374, "59": 421, "60": 421, "61": 425, "62": 425, "63": 476, "64": 476, "65": 490, "66": 490, "67": 492, "68": 492, "69": 518, "70": 518, "71": 521, "72": 521, "73": 552, "74": 552, "75": 552, "76": 552, "77": 557, "78": 557, "79": 557, "80": 557, "81": 557, "82": 557, "83": 557, "84": 557, "85": 557, "86": 557, "87": 571, "88": 571, "89": 580, "90": 580, "91": 584, "92": 585, "93": 586, "94": 586, "95": 586, "96": 587, "97": 588, "98": 588, "99": 588, "100": 589, "101": 589, "102": 590, "103": 590, "104": 592, "105": 592, "106": 595, "107": 605, "108": 607, "109": 609, "110": 611, "111": 687, "112": 698, "113": 707, "119": 690, "126": 690, "127": 691, "131": 693, "132": 694, "133": 695, "134": 695, "135": 695, "136": 697, "137": 697, "138": 697, "144": 597, "149": 597, "150": 598, "151": 598, "157": 709, "161": 709, "167": 607, "171": 607, "177": 611, "186": 700, "191": 700, "192": 704, "193": 704, "199": 613, "206": 613, "207": 622, "208": 622, "209": 632, "210": 632, "211": 642, "212": 642, "213": 665, "214": 665, "215": 666, "216": 666, "217": 667, "218": 667, "219": 668, "220": 668, "221": 669, "222": 669, "223": 670, "224": 670, "225": 681, "226": 681, "232": 609, "241": 232}, "uri": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/master.mak", "filename": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/master.mak", "source_encoding": "utf-8"}
__M_END_METADATA
"""
