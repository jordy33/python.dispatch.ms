<!DOCTYPE html>
<html>
<head>
    ${self.meta()}
    <title>Application Wizard Bootstrap v3.x</title>
    		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script type="text/ecmascript" src="${tg.url('/lib/js/jquery-1.11.0.js')}"></script>
    <script src="${tg.url('/lib/js/bootstrap.min.js')}"></script>
    <script type="text/ecmascript" src="${tg.url('/lib/js/grid.locale-es.js')}"></script>
    <!-- This is the Javascript file of jqGrid -->
    <script type="text/ecmascript" src="${tg.url('/lib/js/jquery.jqgrid.src.js')}"></script>
    <script type="text/ecmascript" src="${tg.url('/lib/js/jquery-ui.min.js')}"></script>
    <!-- This is the localization file of the grid controlling messages, labels, etc.
    <!-- A link to a jQuery UI ThemeRoller theme, more than 22 built-in and many more custom -->
    <link rel="stylesheet" type="text/css" media="screen" href="${tg.url('/lib/css/jquery-ui.css')}" />
    <!-- The link to the CSS that the grid needs -->
    <link rel="stylesheet" type="text/css" media="screen" href="${tg.url('/lib/css/ui.jqgrid.css')}"  />
    <link href="${tg.url('/lib/fonts/font-awesome.min.css')}" rel="stylesheet" />
    <meta charset="utf-8" />
    <title>dispatch</title>

    <link href="${tg.url('/lib/css/bootstrap.min.css')}" rel="stylesheet">
    <script src="${tg.url('/lib/stomp/stomp.js')}"></script>
    <script src="${tg.url('/lib/moment/moment.js')}"></script>
    <script src="${tg.url('/lib/js/alert.js')}"></script>
    <script src="${tg.url('/lib/justgage/raphael-2.1.4.min.js')}"></script>
    <script src="${tg.url('/lib/justgage/justgage.js')}"></script>
    <script src="${tg.url('/lib/jqueryrotate/jQueryRotate.js')}"></script>
    <script src="${tg.url('/lib/jquery-validation-1.17.0/dist/jquery.validate.js')}"></script>

    <script src="${tg.url('/lib/timepicker/jquery-ui-timepicker-addon.js')}"></script>

    <style type="text/css">
        input { box-shadow: 0 0 3px #CC0000; margin: 10px }

        .dropdown {
          background: rgba(255, 255, 255, 0.1);
          float: left;
          margin: 10px 8px;
          padding: 0px;
          border-radius: 4px;
          list-style-type: none;}

        .dropdown a.dropdown-toggle {
          height: 40px;
          width: 40px;
          padding-top: 11px;
          padding-left: 9px; }

        .dropdown:hover {
          color: #fff;
          background: rgba(255, 255, 255, 0.2); }

        .dropdown .label {
          top: -4px;
          left: 22px;
          padding-top: 4px;
          padding-bottom: 4px;
          position: absolute;
          border-radius: 9999px; }

            .profile-sidebar {
          padding: 10px 0;
          border-bottom: 1px solid #e9ecf2; }
        .label-success {
          background-color: #8ad919; }
        .label-danger {
          background-color: #f9243f; }
        .profile-userpic img {
          float: left;
          margin: 10px 0px 0px 15px;
          width: 50px;
          height: 50px;
          border-radius: 9999px !important; }

        .profile-usertitle {
          float: left;
          text-align: left;
          margin: 10px 0 0 12px; }

        .profile-usertitle-name {
          font-size: 15px;
          margin-bottom: 0px; }

        .profile-usertitle-status {
          text-transform: uppercase;
          color: #AAA;
          font-size: 10px;
          font-weight: 600;
          margin-bottom: 15px; }
        .indicator {
          width: 10px;
          height: 10px;
          display: inline-block;
          border-radius: 9999px;
          margin-right: 5px; }

        .error { color: #F00; background-color: #f1f4f3; }
        div.dialog-hidden { display:none}
        html, body { margin: 0; padding: 0;}
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
        function logout() {
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

                //checkConnections();

                // called back after the client is connected and authenticated to the STOMP server
              };
            var error_callback = function(error) {
                $("#online").hide();
                $("#offline").show();
                 //logout();
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
                              <a class="navbar-brand" style="color:#a61a15" href="#"><span>${_('Administration')}</span> <br><div>System</div></a>
                          </div>
                      </td>
                  </tr>
                  <tr>
                      <td>
                          <table>
                              <td>
                                  <li class="dropdown">
                                     <a style="color:#a61a15" class="dropdown-toggle count-info" data-toggle="dropdown" href="#">
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
                  <li class=active><a href="#pl11" aria-expanded=&#34;true&#34;>dispatch</a></li>
                  <li><a href="#" onclick="logout()" style="color:#666"><em class="fa fa-power-off">&nbsp;</em>Logout</a></li>
              </ul>
              <div class="tab-content ui-tabs-panel ui-corner-bottom ui-widget-content">
                      <div class="tab-pane fade in active" id="pl11" style="height:70px;padding: 10px">
                          <!--
                         <button onclick="openTab('${_('Traffic')}','${h.url()}/traffic/index?groups=monitoristas')" title="home of dispatch">${_('Traffic')}</button>
                          <button onclick="openTab('${_('Listener Admin')}','${h.url()}/admin/adminListener/')" title="Listener">${_('Listener Admin')}</button>
                          <button onclick="openTab('${_('Ded Mon')}','${h.url()}/admin/dedicated/')" title="Listener">${_('Ded Mon')}</button>
                          <button onclick="openTab('${_('Roles')}','${h.url()}/admin/roles/')" title="Listener">${_('Roles')}</button>
                          <button onclick="openTab('${_('csv')}','${h.url()}/test/csv/')" title="CSV">${_('csv')}</button>
                          <button onclick="openTab('${_('pdf')}','${h.url()}/test/pdf/')" title="PDF">${_('pdf')}</button>
                          <button onclick="openTab('${_('twg')}','${h.url()}/test/twg/')" title="TWG">${_('Twg')}</button>
                          <button onclick="openTab('${_('Steps Example')}','${h.url()}/test/stepsExample/')" title="Listener">${_('Steps Example')}</button>
                          <button onclick="openTab('${_('Traffic Graphs')}','${h.url()}/traffic/monitorGraph')" title="Listener">${_('Traffic Graphs')}</button>
                          <button onclick="openTab('${_('Email Listener')}','${h.url()}/admin/emailListener/')" title="Listener">${_('Email Listener')}</button>
                          -->
                          <button onclick="openTab('Log','${h.url()}/log/')" title="home of dispatch">Log</button>
                          <!--
                          <button onclick="openTab('Graph','${h.url()}/test/graph')" title="home of earth">TeleGraph</button>
                          <button onclick="openTab('Graph2','${h.url()}/traffic/monitorGraph')" title="home of earth">Mon Graph</button>
                          <button onclick="openTab('QR Codes','${h.url()}/traffic/qrGraph')" title="home of earth">QR</button>
                          <button onclick="openTab('Images','${h.url()}/test/images')" title="Images">Base64</button>
                          <button onclick="openTab('Messages','${h.url()}/test/messages')" title="home of earth">Messages</button>
                          <button onclick="openTab('Position','${h.url()}/test/telefonica')" title="home of earth">Telefonica</button>
                          <button onclick="openTab('${_('Finalized Traffic')}','${h.url()}/traffic/finalizedtraffic')" title="home of dispatch">${_('Finalized Traffic')}</button>
                          -->
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