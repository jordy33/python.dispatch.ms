<!DOCTYPE html>
<html>
<head>
    ${self.meta()}
    <link rel="icon" type="image/x-icon" href="${tg.url('/img/admin.jpeg')}"/>
    <title>${self.title()}</title>
    <!-- CSS -->
    <link href="${tg.url('/css/bootstrap.min.css')}" rel="stylesheet">
    <link href="${tg.url('/css/teststyles3.css')}" rel="stylesheet">
    <!-- Fonts -->
    <link href="${tg.url('/fonts/font-awesome.min.css')}" rel="stylesheet" />
	<link href="${tg.url('/fonts/fonts.css')}" rel="stylesheet">
    <!-- jquery and alert -->
    <script src="${tg.url('/js/jquery-3.3.1.min.js')}"></script>
    <script src="${tg.url('/js/alert.js')}"></script>
	<!--[if lt IE 9]>
	<script src="${tg.url('/js/html5/html5shiv.js')}"></script>
	<script src="${tg.url('/js/html5/respond.min.js')}"></script>
	<![endif]-->
    <!-- jqgrid -->
    <script src="${tg.url('/js/jqgrid/jquery.jqgrid.min.js')}"></script>
    <script src="${tg.url('/js/jqgrid/i18n/grid.locale-es.js')}"></script>
    <link rel="stylesheet" href="${tg.url('/css/ui.jqgrid.css')}">
    <!-- Important: Bootstrap must be first to avoid over raid jquery-ui  -->
    <script src="${tg.url('/js/bootstrap.min.js')}"></script>
    <script src="${tg.url('/js/jquery-ui.js')}"></script>
    <script src="${tg.url('/js/jquery-validation-1.17.0/dist/jquery.validate.js')}"></script>

    <link rel="stylesheet" href="${tg.url('/css/jquery-ui1.css')}" type="text/css"/> <!-- Tema de grid-->
    <!-- end jqgrid -->
    <script src="${tg.url('/js/stomp/stomp.js')}"></script>
    <!-- notifications grid -->
    <!-- moment for UTC to local dates -->
    <script src="${tg.url('/js/moment/moment.js')}"></script>


<style>
.cygnus {

}
</style>
    <style type="text/css">

    div.dialog-hidden { display:none}
    html, body {
        margin: 0;
        padding: 0;
        font-size:100%;
    }
    .main-table{
        width:100%;
        border-style: solid;
        border-width: thin;
        border-collapse: separate;
        border-radius:5px;
        padding-top: 1px;
        padding-right: 1px;
        padding-bottom: 1px;
        padding-left: 1px;
    }
    .td-1{
        padding: 3px;
        alignment: left;
        text-align: left;
        width: 8px;
    }
    .td-last{
        padding: 3px;
        alignment: left;
        text-align: left;
    }

    .second-table{
        border-style: solid;
        border-width: thin;
        border-radius: 10px;
    }

    .ui-tabs {
        padding: 0;
    }
        .ui-tabs-panel {
        padding: 0;
    }
     .ui-tabs   .ui-tabs-panel {
        padding: 0;
    }
     .ui-tabs .ui-tabs-nav .ui-tabs-anchor {
    float: left;
    padding: .2em 1em;
    text-decoration: none;
}
.ui-state-active, .ui-widget-content .ui-state-active, .ui-widget-header .ui-state-active, a.ui-button:active, .ui-button:active, .ui-button.ui-state-active:hover{
color:#ffffff;
}
        .ui-state-default a, .ui-state-default a:link, .ui-state-default a:visited, a.ui-button, a:link.ui-button, a:visited.ui-button, .ui-button {
    color: #eb8f00;
    text-decoration: none;
            background: #fbc674;
}
        .ui-state-default, .ui-widget-content .ui-state-default, .ui-widget-header .ui-state-default, .ui-button, html .ui-button.ui-state-disabled:hover, html .ui-button.ui-state-disabled:active{
            background: #fbc674;
        }


/* DIEGO STYLE */

        .btn{ font-size: 13px;  }
.dropdown-menu{
    font-size: 13px;
    min-width:10px;
}

.dropdown-menu> li> a
{ display: inline;
}

.dropdown-submenu {
    position: relative;
}

.dropdown-submenu .dropdown-menu {
    top: 0;
    left: 100%;
    margin-top: -1px;
}
        .jqgrid-btn{
        background: transparent;
        border: none;
        color: #333;
    }
    .myGridPager{
        font-weight: normal;
    }


 #map {
        height: 400px;
        width: 100%;
       }



/* DIEGO STYLE VENTANA EMERGENTE*/

       .combo{
	font-family: Tahoma, Verdana, Arial;
	font-size: 11px;
	color: #707070;
	background-color: #FFFFFF;
	border-width:0;
}
  .seccion {
      width: 100%;
      font-family: Georgia, "Times New Roman", Times, serif;
      color: #ffffff;
      background-color: #0a90b7eb }

  .h1 {
    font-family: Helvetica, Geneva, Arial, SunSans-Regular, sans-serif;


  }

       .bloque{
           width: 28%;
           background-color: lightgray;


       }

       .bloquelargo{
           width: 25%;
           background-color: lightgray;
       }

  #amap {
        height: 400px;
        width: 100%;
       }

  td.sombra{
      background-color: #dddddd;

  }

  td.sombrafuerte{

  background-color: #424242;
  color: #ffffff;

  }



       .switch {
	position: relative;
	display: block;
	vertical-align: top;
	width: 100px;
	height: 30px;
	padding: 3px;
	margin: 0 10px 10px 0;
	background: linear-gradient(to bottom, #eeeeee, #FFFFFF 25px);
	background-image: -webkit-linear-gradient(top, #eeeeee, #FFFFFF 25px);
	border-radius: 18px;
	box-shadow: inset 0 -1px white, inset 0 1px 1px rgba(0, 0, 0, 0.05);
	cursor: pointer;
	box-sizing:content-box;
}
.switch-input {
	position: absolute;
	top: 0;
	left: 0;
	opacity: 0;
	box-sizing:content-box;
}
.switch-label {
	position: relative;
	display: block;
	height: inherit;
	font-size: 10px;
	text-transform: uppercase;
	background: #eceeef;
	border-radius: inherit;
	box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.12), inset 0 0 2px rgba(0, 0, 0, 0.15);
	box-sizing:content-box;
}
.switch-label:before, .switch-label:after {
	position: absolute;
	top: 50%;
	margin-top: -.5em;
	line-height: 1;
	-webkit-transition: inherit;
	-moz-transition: inherit;
	-o-transition: inherit;
	transition: inherit;
	box-sizing:content-box;
}
.switch-label:before {
	content: attr(data-off);
	right: 11px;
	color: #aaaaaa;
	text-shadow: 0 1px rgba(255, 255, 255, 0.5);
}
.switch-label:after {
	content: attr(data-on);
	left: 11px;
	color: #FFFFFF;
	text-shadow: 0 1px rgba(0, 0, 0, 0.2);
	opacity: 0;
}
.switch-input:checked ~ .switch-label {
	background: #E1B42B;
	box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.15), inset 0 0 3px rgba(0, 0, 0, 0.2);
}
.switch-input:checked ~ .switch-label:before {
	opacity: 0;
}
.switch-input:checked ~ .switch-label:after {
	opacity: 1;
}
.switch-handle {
	position: absolute;
	top: 4px;
	left: 4px;
	width: 28px;
	height: 28px;
	background: linear-gradient(to bottom, #FFFFFF 40%, #f0f0f0);
	background-image: -webkit-linear-gradient(top, #FFFFFF 40%, #f0f0f0);
	border-radius: 100%;
	box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
}
.switch-handle:before {
	content: "";
	position: absolute;
	top: 50%;
	left: 50%;
	margin: -6px 0 0 -6px;
	width: 12px;
	height: 12px;
	background: linear-gradient(to bottom, #eeeeee, #FFFFFF);
	background-image: -webkit-linear-gradient(top, #eeeeee, #FFFFFF);
	border-radius: 6px;
	box-shadow: inset 0 1px rgba(0, 0, 0, 0.02);
}
.switch-input:checked ~ .switch-handle {
	left: 74px;
	box-shadow: -1px 1px 5px rgba(0, 0, 0, 0.2);
}

/* Transition
========================== */
.switch-label, .switch-handle {
	transition: All 0.3s ease;
	-webkit-transition: All 0.3s ease;
	-moz-transition: All 0.3s ease;
	-o-transition: All 0.3s ease;
}

    </style>
    <!-- Global JavaScript -->
    <script type="text/javascript">
        function changeStateMessage(recordNumber){
                $.ajax({
                type: "GET",
                url: "${tg.url('/notification/updateBadge')}"+"?record="+recordNumber,
                contentType: "application/json; charset=utf-8",
                data: { 'param':'badge' },
                success: function(data) {
                    // data.value is the success return json. json string contains key value
                    $("#numeric_badge").text(data.badge);
                },
                error: function() {
                    //alert("#"+ckbid);
                    alert("Error accessing server notification/badge")
                    },
                complete: function() {
                    }
                });
                $('#jqGridNot').trigger( 'reloadGrid' );
        }
        function alogout() {
            var i = document.childNodes.length - 1;
            while (i >= 0) {
              console.log(document.childNodes[i]);
              document.removeChild(document.childNodes[i--]);
            }
            jQuery.ajax({
                    type: "GET",
                    url: "/secc",
                    username: "logmeout",
                    password: "123456",
                    headers: { "Authorization": "Basic xxx" }
            })
            .done(function(){
                // If we don't get an error, we actually got an error as we expect an 401!
            })
            .fail(function(){
                // We expect to get an 401 Unauthorized error! In this case we are successfully
                    // logged out and we redirect the user.
                window.location = "/";
            });

            return false;
        }
        var username = 'dispatch';
        var password = 'managepass';

        function make_base_auth(user, password) {
            var tok = user + ':' + password;
            var hash = btoa(tok);
            return "Basic " + hash;
        }
        function doAjax(pageName,id) {
                $.ajax({
                    url:pageName ,
                    error: function () {
                        alert("Error de credenciales con otro planeta");
                    },
                    beforeSend: function(xhr){
                    xhr.setRequestHeader("Content-Type","application/json");
                    xhr.setRequestHeader("Accept","application/json");
                    xhr.setRequestHeader( "Authorization", make_base_auth(username,password));
                    },
                    dataType: 'html',
                    data: { user: "${h.whoami()}", id:id } ,
                    success: function (data, rq) {
                        $("#loader"+id).html('');
                         $("#"+id).html(data);
                    },
                    error: function (data, rq) {
                        $("#"+id).html("<p>Error</p>");
                    },
                    type: 'GET'
                });
        }
        function loadIframe(url) {
         $.ajax({

            url: url,
            type: "GET",
             crossDomain: true,
             xhrFields: {
            withCredentials: true
        },
        beforeSend: function(xhr){
                xhr.setRequestHeader("Content-Type","application/json");
                xhr.setRequestHeader("Accept","application/json");
                xhr.setRequestHeader( "Authorization", make_base_auth(username,password));
        },
            data: "user=${h.whoami()}",
            success: function (response) {
                $("#iframe").attr('src',"data:text/html;charset=utf-8," + escape(response));

            },
            error: function(xhr,textStatus,err)
            {
                console.log("readyState: " + xhr.readyState);
                console.log("responseText: "+ xhr.responseText);
                console.log("status: " + xhr.status);
                console.log("text status: " + textStatus);
                console.log("error: " + err);
            }
        });
    }

        function openWindow(url,text,id){
            doAjax(url,id);
            var $dialog = $('<div></div>')
               .html('<div id="'+id+'" style="margin:10px"></div>')
               .dialog({
                   autoOpen: false,
                   modal: true,
                   height:  580,
                   width: 820,
                   resizable: false,
                   draggable: true,
                   position : { my: "center", at: "top", of: window },
                   title: text,
                   buttons: {
                       "Close": function ()
                       {
                           $(this).dialog('destroy').remove();
                       }
                   }
               });
        $dialog.dialog('open');
        }
        function openTab(text,url) {
                var num_tabs = $("div#tabs ul.main1 li.main1").length + 1;
                var mytext= text;
                var id = "frame"+num_tabs;
                doAjax(url,id);
                $("div#tabs ul.main1").append(
                    "<li class='main1'><a href='#tab"+num_tabs+"'>"+mytext+"</a><span class='ui-icon ui-icon-close' role='presentation'>Remove Tab</span></li>"
                );
                $("div#tabs").append(
                    "<div id='tab"+num_tabs+"'> <div class='row'><div class='col-lg-12'><div id='"+id+"' style='margin:10px'></div><div id='loader"+id+"' class='cygnus'><span style='float:left;width: 20%;'><p>Cargando ...</p></span><span style='float:right;width: 80%;'><img src=${tg.url('/img/ajax-loader.gif')}></span></div></div></div></div>"
                );
                var $head = $("#"+id).contents().find("head");

                var ur="${tg.url('/css/theme/jquery-ui1.css')}";
                $head.append($("<link/>",
                        { rel: "stylesheet", href:ur, type: "text/css" }
                      ));

                $("div#tabs").tabs("refresh").tabs('option', 'active', num_tabs - 1);
        }
        function notificationFmatter (cellvalue, options, rowObject)
        {
            var array = cellvalue.split(',');
            if (rowObject[5]=='Y') {
                html = '<div class="media">'+
                            '<div class="media-body">' +
                                '<strong class="notification-title">' +
                                    '<i class="'+array[6]+'"></i>&nbsp&nbsp'+
                                    '<a style="color:#337ab7;text-decoration: none;" href="#">'+
                                        array[0]+' </a>'+
                                        array[1]+' <a style="color:#337ab7;text-decoration: none;" href="#">'+
                                        array[2]+'</a></strong> ' +
                                    '<p class="notification-desc"></p>'+
                                        array[3]+'</i><br>'+
                                        array[4]+
                                        '<br><small style="color: #777777;" class="timestamp">'+
                                        rowObject[2]+'</small></p>' +
                            '</div>' +
                        '</div>';
            }
                else
            {
                html = '<div class="media">'+
                            '<div class="media-body">' +
                                '<strong class="notification-title">' +
                                    '<i class="'+array[6]+'"></i>&nbsp&nbsp'+
                                    '<a style="color:#337ab7;text-decoration: none;" href="#">'+
                                        array[0]+' </a>'+
                                        array[1]+' <a style="color:#337ab7;text-decoration: none;" href="#">'+
                                        array[2]+'</a></strong> ' +
                                    '<p class="notification-desc"></p>'+
                                        array[3]+'</i><br>'+
                                        array[4]+
                                        '<br><small style="color: #777777;" class="timestamp">'+
                                        rowObject[2]+'</small></p>' +
                                        '<input type = "button", value = "Dismiss" onclick = "changeStateMessage('+rowObject[0]+')">' +
                            '</div>' +
                        '</div>';
            }
            return html
        }

        $(document).ready(function () {

            var ding = new Audio("${tg.url('/sounds/ding.mp3')}");
            document.getElementById('iframe').setAttribute('height',window.innerHeight*.65);

            $("div#tabs").tabs();

            $( "#tabs" ).tabs().on( "click", "span.ui-icon-close", function() {
              var num_tabs = $("div#tabs ul li").length + 1;
              var panelId = $( this ).closest( "li" ).remove().attr( "aria-controls" );
              $( "#" + panelId ).remove();
              $("div#tabs").tabs("refresh").tabs('option', 'active', num_tabs - 1);
            });
            function checkConnections(){
                $.ajax({
                type: "GET",
                url: "${tg.url('/rabbit/countsessions')}",
                contentType: "application/json; charset=utf-8",
                data: { 'user':'${h.whoami()}' },
                success: function(data) {
                    // data.value is the success return json. json string contains key value
                    var instances = Number(data.count)
                    if (instances>0){
                      alert("El usuario esta conectado en otra session")  ;
                      logout();
                    }
                    else {
                         $("#online").show();
                         $("#offline").hide();
                    }

                },
                error: function() {
                    //alert("#"+ckbid);
                    alert("Error in /rabbit/countsessions")
                    },
                complete: function() {
                    }
                });
                $('#jqGridNot').trigger( 'reloadGrid' );
            }

            //STOMP SETUP

            var client = Stomp.client('${h.stompServer()}');
            client.debug=null;
            var connect_callback = function() {
                client.subscribe("/topic/${h.whoami()}", subscribe_callback);

                checkConnections();

                // called back after the client is connected and authenticated to the STOMP server
              };
            var error_callback = function(error) {
                $("#online").hide();
                $("#offline").show();
                 logout();
            };
            var subscribe_callback = function(message) {

                var msg = message.body;
                var payload = msg.split('|');
                var command = payload[0];
                var data = payload[1];
                switch (command) {
                        case 'MSG':
                            $.alert(data, { autoClose:false});

                            ding.play();
                            break;
                        case 'NOT':
                            $.alert("Mensaje nuevo", { autoClose:true});
                            $("#numeric_badge").text(data);
                            $('#jqGridNot').trigger( 'reloadGrid' );
                            ding.play();
                            break;
                }
              };
            client.connect('${h.whoami()}', '${h.password()}', connect_callback, error_callback, '/');
            $("#jqGridNot").jqGrid({
                    url: '/notification/loadNotification/',
                    datatype: 'json',
                    mtype: 'GET',
                    colNames: [ 'id','${_('user')}','${_('time_stamp')}','${_('Message')}','${_('state')}','${_('Message')}'],
                    colModel :[
                        {name:'id', hidden: true , width:0},
                        {name:'user_id', hidden: true , width:0},
                        {name:'time_stamp', hidden: true , width:0},
                        {name:'message',formatter:notificationFmatter},
                        {name:'attended_time', hidden: true , width:0},
                        {name:'attended_state', hidden: true , width:0},

                    ],

                    sortname: 'time_stamp',
                    sortorder: "desc",
                    viewrecords: true, // show the current page, data rang and total records on the toolbar
                    caption: "${_('Notifications')}",
                    height: 150,
                    width: 446
                });
            });


	</script>

    ${self.head_content()}

</head>

% if tg.auth_stack_enabled:
  % if h.whoami()=="":
       <meta http-equiv="refresh" content="0; url=${tg.url('/main')}" />
  % else:
        <body class="${self.body_class()}">
          ${self.main_menu()}
          ${self.footer()}
        <!-- Insert nice scrool -->
          ${self.bottom_scripts()}
  % endif
% endif


<%def name="meta()">
    <meta charset="${response.charset}" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Bootstrap 3 App">
    <meta name="author" content="Jorge Macias & Maria Lacayo">
    <meta name="keyword" content="Sun">
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
</%def>

<%def name="title()">  </%def>

<%def name="head_content()"></%def>

<%def name="body_class()"></%def>

<%def name="main_menu()">
  <!-- INSERT MAIN MENU -->
<nav>
      <table style="width: 100%"  class=" ui-tabs-panel ui-corner-bottom ui-widget-content">
          <td style="width: 5%">
              <table>
                  <tr>
                      <td colspan="2">
                          <div align="center" >
                              <a class="navbar-brand" style="color:#FDB813" href="#"><span>${_('Administration')}</span> <br><div>System</div></a>
                          </div>
                      </td>
                  </tr>
                  <tr>
                      <td>
                          <table>
                              <td>
                                  <li class="dropdown">
                                     <a style="color:#FDB813" class="dropdown-toggle count-info" data-toggle="dropdown" href="#">
                                      <em class="fa fa-bell"></em><span class="label label-info" id="numeric_badge">${h.badge()}</span>
                                     </a>
                                     <ul class="dropdown-menu dropdown-alerts">
                                      <table id="jqGridNot" class="scroll" cellpadding="0" cellspacing="0"></table>
                                      <div id="jqGridNot" class="scroll" style="text-align:center;"></div>
                                     </ul>
                                  </li>
                              </td>
                              <td>
                                  <div class="profile-usertitle">
                                      <div class="profile-usertitle-name">${h.whoami()}</div>
                                      <div id="online" class="dialog-hidden">
                                          <div class="profile-usertitle-status"><span class="indicator label-success"></span>Online</div>
                                      </div>
                                      <div id="offline" class="dialog-hidden">
                                          <div class="profile-usertitle-status"><span class="indicator label-danger"></span>Offline</div>
                                      </div>

                                  </div>
                              </td>
                          </table>
                      </td>

                  </tr>
              </table>
          </td>
          <td>
              <ul class="nav nav-tabs ui-widget-header">
                  <li class=active><a href="#pl11" aria-expanded=&#34;true&#34;>Earth</a></li>
                  <li><a href="#" onclick="logout()" style="color:#666"><em class="fa fa-power-off">&nbsp;</em>Logout</a></li>
              </ul>
              <div class="tab-content ui-tabs-panel ui-corner-bottom ui-widget-content">
                      <div class="tab-pane fade in active" id="pl11" style="height:70px;padding: 10px">
                         <button onclick="openTab('Traffic','${h.url()}/traffic/index')" title="home of earth">Traffic</button>
                          <button onclick="openTab('Listener Admin','${h.url()}/admin/listener/')" title="Listener">Listener Admin</button>
                         <button onclick="openTab('Graph','${h.url()}/test/graph')" title="home of earth">Graph</button>
                          <button onclick="openTab('Users','${h.url()}/test/users')" title="home of earth">Users</button>
                           <button onclick="openTab('Users','${h.url()}/test/ecran')" title="home of earth">Ecran</button>
                          <button onclick="openTab('Stomp','${h.url()}/test/websockets')" title="home of earth">Stomp</button>
                      </div>
              </div>
          </td>
      </table>
</nav>
      <div id="tabs">
          <ul class="nav nav-tabs ui-widget-header main1">
            <li class="main1"><a href="#tabs-1" >Inicio</a></li>
          </ul>
          <div id="tabs-1" align="right">
            ${self.content_wrapper()}
          </div>
      </div>
    <!-- End MENU -->


</%def>


<%def name="content_wrapper()">
  <%
    flash=tg.flash_obj.render('flash', use_js=False)
  %>
  % if flash:
    <script>$.alert("${str(tg.flash_obj.pop_payload()['message'])}" ,{autoclose:false,type:'info',title:false});</script>
  % endif
  ${self.body()}
</%def>

<%def name="footer()">
   <!-- INSERT FOOTER -->
    <div class="text-right">
        <div class="credits">
              <p>Copyright &copy; Madd Systems ${h.current_year()}&nbsp;</p>
        </div>
    </div>
</%def>

<%def name="bottom_scripts()">
 <script type="text/javascript">

 </script>
</%def>