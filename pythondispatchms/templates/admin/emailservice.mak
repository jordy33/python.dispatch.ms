<style type="text/css">
</style>
<script>

            function dateFmatter ( cellvalue, options, rowObject )
            {
                var utcDate=moment.utc(cellvalue,"YYYY-MM-DD h:mm:ss")
                var localDate=moment(utcDate).local();
                var formatdate = localDate.format("YYYY-MM-DD HH:mm:ss");
                return formatdate;
            }
            function statusFmatter ( cellvalue, options, rowObject ){
                html=cellvalue;
                switch (cellvalue){
                    case cellvalue="A":
                        html = '<center><span class="glyphicon glyphicon-search" style="color:blue"></span></center>';
                        break;
                    case cellvalue="N":
                        html = '<center><span class="glyphicon glyphicon-remove" style="color:red"></span></center>';
                        break;
                    case cellvalue="C":
                        html = '<center><span class="glyphicon glyphicon-ok" style="color:green"></span></center>';
                        break;
                    case cellvalue="P":
                        html = '<center><span class="glyphicon glyphicon-time" style="color:sandybrown"></span></center>';
                        break;
                }
                return html;
            }
            function priorityFmatter ( cellvalue, options, rowObject )
            {
                html=cellvalue;

                switch (cellvalue){

                    case cellvalue=1:
                        html='<center><div class="redsquare" style="text-align:center"> <img/> </div></center>';
                        break;
                    case cellvalue=2:
                        html='<center><div class="orangesquare"> <img/> </div></center>';
                        break;
                    case cellvalue=3:
                        html='<center><div class="yellowsquare"> <img/> </div></center>';
                        break;
                    case cellvalue=4:
                        html='<center><div class="greensquare"> <img/> </div></center>'
                        break;
                    case cellvalue=5:
                        html='<center><div class="bluesquare"> <img/> </div></center>';
                        break;
                }
                return html;
            }
            var c5Plates=''
            var grid_name_email = '#jgGridEmail';
            var grid_pager_email= '#listEmailListeners';
            var load_url='${h.url()}/admin/loadEmailListener/?user=${user}';
            var update_url='${h.url()}/admin/updateEmailListener/?user=${user}';
            //var header_container='${_('Alerts')}';
            var addParams = {left: 0,width: window.innerWidth-700,top: 20,height: 255,url: update_url,mtype: 'GET', closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var editParams = {left: 0,width: window.innerWidth-700,top: 20,height: 255,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                    width: "500",
                    editfunc: function (rowid) {
                    }
                };
            var deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,mtype: 'GET',closeAfterEdit: true,closeAfterSearch:true,url: update_url,modal: true, };
            var grid = jQuery(grid_name_email);

            $(document).ready(function () {
                grid.jqGrid({
                url: load_url,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['${_('Hidden')}', '${_('Event ID')}', '${_('Event Desc')}', '${_('Client-Id')}', '${_('Name')}', '${_('IMEI')}', '${_('Email')}', '${_('Password')}', '${_('SMTP Server')}','${_('Port')}','${_('Latitude')}','${_('Longitude')}'],
                colModel: [
                    {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'event_id',index: 'event_id', width: 5, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'event_desc',index: 'event_desc',width: 10,align: 'right',editable: true,edittype: 'text',editrules: {required: true}},
                    {name: 'client_id', index: 'client_id', width: 5,align: 'right',hidden: false, editable: true, edittype: 'text', formatter:statusFmatter, editrules: {required: true},search:false},
                    {name: 'client_name', index: 'client_name', width: 10,align: 'right',hidden: false, editable: true, edittype: 'text', formatter:statusFmatter, editrules: {required: true},search:false},
                    {name: 'imei', index: 'imei', width: 5,align: 'right',hidden: false, editable: true, edittype: 'text', formatter:priorityFmatter, editrules: {required: true},search:false},
                    {name: 'email',index: 'email',width: 10,align: 'right',hidden: false,editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'password',index: 'password',width: 5,align: 'right',hidden: false,editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'smtp_server',index: 'smtp_server', width: 10, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'port',index: 'port',width: 5,align: 'right',editable: true,edittype: 'text',editrules: {required: true}},
                    {name: 'latitude',index: 'latitude',width: 5,align: 'right',editable: true,edittype: 'text',editrules: {required: true}},
                    {name: 'longitude',index: 'longitude',width: 5,align: 'right',editable: true,edittype: 'text',editrules: {required: true}},
                ],
                pager: jQuery(grid_pager_email),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'email',
                sortorder: "desc",
                viewrecords: true,
                autowidth: true,
                height: 250,
                //caption: header_container,
            });
            grid.jqGrid('navGrid',grid_pager_email,{edit:false,add:false,del:true, search:false},
                            editParams,
                            addParams,
                            deleteParams,
                            searchParams,
                            viewParams);
            // add custom button
            grid.navButtonAdd(grid_pager_email,
                {
                    buttonicon: "ui-icon-plus",
                    title: "${_('Add')}",
                    caption: "${_('Add')}",
                    position: "first",
                    onClickButton: addUserWindow
                });
            });
            $.extend($.jgrid.nav,{alerttop:1});
            function addUserWindow(){
                var winHeight = 400; //Math.round(window.innerHeight * .50)
                var winWidth = 810;//Math.round(window.innerWidth * .50)
                var grid_name_email = 'jgGridEmai4Usersl';
                var pager_name = "jqGridPagerEmail4Users";
                var grid_name_email_by_id = '#'+grid_name_email;
                var pager_name_by_id = '#'+pager_name;
                if ($(grid_name_email_by_id).length){
                    $(grid_name_email_by_id).remove();
                    $(pager_name_by_id).remove();
                }
                if ($("#AppForm").length){
                    $("#AppForm").remove();
                }
                var newDiv = $(document.createElement('div'));
                var html='<div id="AppForm" title="Filter">'
                html=html+'<table id="'+grid_name_email+'"></table> <div id="'+pager_name+'"> </div>'
                html=html+'</div>'
                newDiv.html(html);

                var createUsersSticky = newDiv.dialog({
                    autoOpen: false,
                    title: "Double click to select",
                    height: winHeight - 20,
                    width: winWidth,
                    modal: true,
                    close: function () {
                    }
                });
                var grid = new jQuery(grid_name_email_by_id);
                grid.jqGrid({
                    url: '${h.url()}/admin/getClients4Email',
                    mtype: "GET",
                    datatype: "json",
                    page: 1,
                    colModel: [
                        {label: "User Name", name: 'username', key: true, width: 150},
                        {label: "Address", name: 'address', width: 150},
                        {label: "application_id", name: 'application_id', width: 150,hidden:true},
                        {label: "folio_sinube", name: 'folio_sinube', width: 150,hidden:true},
                        {label: "internal_id", name: 'internal_id', width: 150,hidden:true}
                    ],
                    loadonce: true,
                    viewrecords: true,
                    width: 780,
                    height: 250,
                    rowNum: 10,
                    pager: pager_name_by_id,
                    ondblClickRow: function (rowId) {
                        var rowData = jQuery(grid_name_email_by_id).getRowData(rowId);
                        createUsersSticky.dialog("close");
                        AddEmailService(rowData['application_id'],rowData['folio_sinube'],rowData['internal_id'],rowData['username']);
                    },

                });
                grid.navGrid(pager_name_by_id, {
                    search: true,
                    add: false,
                    edit: false,
                    del: false,
                    refresh: true
                }, {}, {}, {}, {});

                createUsersSticky.dialog("open");
            }

            function AddEmailService(client_id,imei,internal_id,application_name) {
                var winHeight = 700; //Math.round(window.innerHeight * .50)
                var winWidth = 800
                if ($("#addEmailForm").length){
                    $("#addEmailForm").remove();
                }
                var addEmailExpButtons = {
                                    "${_('Add')}": function() {
                                        var expressionemail= encodeURIComponent($('#expressionemail').val());
                                        var expressionepasswd= encodeURIComponent($('#expressionpasswd').val());
                                        var expressionsmtp= encodeURIComponent($('#expressionsmtp').val());
                                        var expressionport= encodeURIComponent($('#expressionport').val());
                                        var expressioneventid= encodeURIComponent($('#expressioneventid').val());
                                        var expressioneventdesc= encodeURIComponent($('#expressioneventdesc').val());
                                        $.ajax({
                                                type: "GET",
                                                url:  '${h.url()}/admin/addEmaillistener'+"?email="+expressionemail+"&password="+expressionepasswd+"&smtp="+expressionsmtp+"&port="+expressionport+"&client_id="+client_id+"&imei="+imei+"&internal_id="+internal_id+"&event_id="+expressioneventid+"&event_desc="+expressioneventdesc+"&client_name="+application_name,
                                                contentType: "application/json; charset=utf-8",
                                                data: { 'param':'gaugeParameters' },
                                                success: function(data) {
                                                    // data.value is the success return json. json string contains key value
                                                     $('#jgGridEmail').trigger( 'reloadGrid' );
                                                },
                                                error: function() {
                                                     $.alert("Error accessing /admin/addGlobalExp", { autoClose:false,});
                                                    return true;
                                                },
                                                complete: function() {
                                                }
                                                });
                                            $('#emailListenerForm')[0].reset();
                                            addUserTriggerDialog.dialog( "close" );


                                    },
                                    "${_('Close')}": function() {
                                        $('#emailListenerForm')[0].reset();
                                        addUserTriggerDialog.dialog( "close" );
                                    }
                            };
                var newDiv = $(document.createElement('div'));
                var info='<style type="text/css"> .container { width: 500px; clear: both; }.container input { width: 100%; clear: both; } </style>'
                info=info+'<div class="container" id="addEmailForm" title="Filter"><form id="emailListenerForm">'
                info=info+'<br>Event ID:</label> <input id="expressioneventid" name="expressioneventid" type="number"></textarea>'
                info=info+'<br>Event Desc:</label> <input id="expressioneventdesc" name="expressioneventdesc" type="text"></textarea>'
                info=info+'<br>Email:<input type="text" id="expressionemail" name="expressionemail"></textarea>'
                info=info+'<br>Password:<input type="text" id="expressionpasswd" name="expressionpasswd"></textarea>'
                info=info+'<br>SMTP Server:<input type="text" id="expressionsmtp" name="expressionsmtp" value="imap.gmail.com"></textarea>'
                info=info+'<br>SMTP Port:</label> <input id="expressionport" name="expressionport" value="993" type="number"></textarea>'
                info=info+'<br/></form></div>'
                newDiv.html(info);
                var addUserTriggerDialog = newDiv.dialog({
                    autoOpen: false,
                    title:'Add email listener parameters',
                    height: winHeight-100,
                    width: winWidth-200,
                    modal: true,
                    buttons: addEmailExpButtons,
                    close: function() {
                        //$('#emailListenerForm')[0].reset();
                        //form[ 0 ].reset();
                        //allFields.removeClass( "ui-state-error" );
                    }
                 });
                addUserTriggerDialog.data('rowId',1);
                addUserTriggerDialog.dialog( "open" );
            }
            // STOMP
            var emaillistenerclient = Stomp.client('${h.stompServer()}');
            emaillistenerclient.debug=null;
            var email_listener_connect_callback = function() {
                emaillistenerclient.subscribe("/topic/emaillistener", email_listener_subscribe_callback);
                // called back after the client is connected and authenticated to the STOMP server
              };
            var email_listener_error_callback = function(error) {
            };
            var email_listener_subscribe_callback = function(message) {

                var msg = message.body;
                var payload = msg.split('|');
                var command = payload[0];
                var data = payload[1];
                switch (command) {
                        case 'RELOAD':
                            $("#jgGridListeners").trigger( 'reloadGrid' );
                            break;
                        case 'NEW':
                            $("#jgGridListeners").trigger( 'reloadGrid' );
                            $.alert("Listener has been trigger, now you can assign data", { autoClose:true,type: 'success',});
                            bell.play();
                            break;
                        case 'MSG':
                            $.alert(data, { autoClose:false,type: 'success',});
                            bell.play();
                            break;
                }
              };
            //emaillistenerclient.connect('${h.whoami()}', '${h.password()}', listener_connect_callback, listener_error_callback, '/');
            var stompUser='${h.stompUser()}';
            var stompPass='${h.stompPassword()}';
            emaillistenerclient.connect(stompUser, stompPass, email_listener_connect_callback, email_listener_error_callback, '/');
            </script>
</div>
    <!-- page start-->
    <!-- Hidden POP UP Start-->

    <!-- Hidden POP UP End-->
<div id="noteContent" title="${_('Basic dialog')}">
</div>
    <!-- JQGRID table start-->
    <table style="width:100%">
    <table id="jgGridEmail" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listEmailListeners" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsListener+e" class="scroll" style="text-align:center;"></div>
    </table>
    <br>

  <!-- page end-->