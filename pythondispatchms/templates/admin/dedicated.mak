

<script type="text/javascript">
    var lastsel2
$(document).ready(function () {
    function showCalendarInDedicated(rowId)
    {
        var winHeight = 400; //Math.round(window.innerHeight * .50)
                var winWidth = 810;//Math.round(window.innerWidth * .50)
                var grid_name_email = 'rowed5';
                var pager_name = "rowedPager";
                var user_fields_grid_pager=pager_name;
                var grid_name_email_by_id = '#'+grid_name_email;
                var pager_name_by_id = '#'+pager_name;
                if ($(grid_name_email_by_id).length){
                    $(grid_name_email_by_id).remove();
                    $(pager_name_by_id).remove();
                }
                if ($("#CalForm").length){
                    $("#CalForm").remove();
                }
                var user_fields_load_url='${h.url()}/admin/loadMonitorCalendars?id='+rowId;
                var newDiv = $(document.createElement('div'));
                var html='<div id="CalForm" title="Filter">'
                html=html+'<table id="'+grid_name_email+'"></table> <div id="'+pager_name+'"> </div>'
                html=html+'</div>'
                newDiv.html(html);

                var createUsersSticky = newDiv.dialog({
                    autoOpen: false,
                    title: "Doble click para seleccionar rol",
                    height: winHeight - 20,
                    width: winWidth,
                    modal: true,
                    close: function () {
                    }
                });
                var grid = new jQuery(grid_name_email_by_id);
                grid.jqGrid({
                    url: user_fields_load_url,
                    datatype: 'json',
                    mtype: 'GET',
                    colNames: ['id', ''  ,'00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19', '20','21','22','23'],
                    colModel: [
                        {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: false,edittype: 'text',editrules: {required: false}},
                        {name: 'day',index: 'day', width: 15, align: 'right', hidden: false, editable: false, edittype: 'text',editrules: {required: false}},
                        {name: 'h00', index: 'h00', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions:  {value:"Si:No"}},
                        {name: 'h01', index: 'h01', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h02', index: 'h02', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h03', index: 'h03', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h04', index: 'h04', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h05', index: 'h05', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h06', index: 'h06', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h07', index: 'h07', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h08', index: 'h08', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h09', index: 'h09', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h10', index: 'h10', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h11', index: 'h11', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h12', index: 'h12', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h13', index: 'h13', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h14', index: 'h14', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h15', index: 'h15', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h16', index: 'h16', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h17', index: 'h17', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h18', index: 'h18', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h19', index: 'h19', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h20', index: 'h20', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h21', index: 'h21', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h22', index: 'h22', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},
                        {name: 'h23', index: 'h23', width: 5,align: 'right',hidden: false, editable: true,edittype:"checkbox",editoptions: {value:"Si:No"}},


                    ],

                    pager: jQuery(user_fields_grid_pager),
                    rowNum: 10,
                    rowList: [10, 50, 100],
                    sortname: 'day',
                    sortorder: "asc",
                    viewrecords: true,
                    width: winWidth-40,
                    height: winHeight-145,
                    ondblClickRow: function(this_row) {
                                var rowData = jQuery("#jqGridDevices").getRowData(this_row);
                                //mapExpressions(rowId,rowData['id'],rowData['user_name'],listenerID,rowData['userlisteners_id']);
                                },
                    onSelectRow: function(id){
                        if(id && id!==lastsel2){
                            jQuery('#rowed5').jqGrid('restoreRow',lastsel2);
                            jQuery('#rowed5').jqGrid('editRow',id,true);
                            lastsel2=id;
                        }
                    },
                    editurl: '${h.url()}/admin/updateMonitorCalendars',
                    caption: "Input Types"

                });
                createUsersSticky.dialog("open");

    }
    function showDevicesInDedicated(rowId)
    {
        //var winHeight=Math.round(window.innerHeight*.50);
        //var winWidth=Math.round(window.innerWidth*.85);
        var winHeight=450;
        var winWidth=1000;
        // Event Routines
        var user_fields_grid_name = '#jqGridDevices';
        var grid_name_devices = 'jqGridDevices';
        var user_fields_grid_pager= '#DevicesTables';
        var pager_name = "DevicesTables";
        var user_fields_load_url='${h.url()}/admin/loadMonitorDevices?id='+rowId;
        var user_fields_update_url='${h.url()}/admin/updateMonitorDevices';
        var user_fields_addParams = {left: 0,width: window.innerWidth-700,top: 20,height: 190,url: user_fields_update_url,mtype: 'GET', closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
        var user_fields_editParams = {left: 0,width: window.innerWidth-500,top: 20,height: 250,url: user_fields_update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
            width: "500",
            editfunc: function (rowid) {
            alert('The "Edit" button was clicked with rowid=' + rowid);
            }
        };
        var user_fields_deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: user_fields_update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
        var user_fields_viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: user_fields_update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
        var user_fields_searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: user_fields_update_url,modal: true, };
        if ($("#DevForm").length){
                $("#DevForm").remove();
            }
            var newDiv = $(document.createElement('div'));
            var html='<div id="DevForm" title="Filter">'
            html=html+'<table id="'+grid_name_devices+'"></table> <div id="'+pager_name+'"> </div>'
            html=html+'</div>'
            newDiv.html(html);

            var createUsersSticky2 = newDiv.dialog({
                autoOpen: false,
                title: "${_('Unidades a monitorear')}",
                height: winHeight - 20,
                width: winWidth,
                modal: true,
                close: function () {
                }
            });

        var user_fields_grid = new jQuery(user_fields_grid_name);
        user_fields_grid.jqGrid({
            url: user_fields_load_url,
            datatype: 'json',
            mtype: 'GET',
            colNames: ['id', "${_('IMEI')}","${_('Unidad')}","${_('Conductor')}",'Password','Tel 1','Tel 2','Tel 3','Obs'],
            colModel: [
                {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: false,edittype: 'text',editrules: {required: false}},
                {name: 'imei',index: 'imei', width: 15, align: 'right', hidden: false, editable: false, edittype: 'text',editrules: {required: false}},
                {name: 'description', index: 'description', width: 35,align: 'right',hidden: false, editable: false,edittype: 'text', editrules: {required: false}},
                {name: 'driver_name', index: 'driver_name', width: 5,align: 'right',hidden: false, editable: true,edittype: 'text', editrules: {required: false}},
                {name: 'password', index: 'password', width: 5,align: 'right',hidden: false, editable: true,edittype: 'text', editrules: {required: false}},
                {name: 'phone1', index: 'phone1', width: 5,align: 'right',hidden: false, editable: true,edittype: 'text', editrules: {required: false}},
                {name: 'phone2', index: 'phone2', width: 5,align: 'right',hidden: false, editable: true,edittype: 'text', editrules: {required: false}},
                {name: 'phone3', index: 'phone3', width: 5,align: 'right',hidden: false, editable: true,edittype: 'text', editrules: {required: false}},
                {name: 'obs', index: 'obs', width: 5,align: 'right',hidden: false, editable: true,edittype: 'text', editrules: {required: false}},
                
            ],
            pager: jQuery(user_fields_grid_pager),
            rowNum: 10,
            rowList: [10, 50, 100],
            sortname: 'description',
            sortorder: "asc",
            viewrecords: true,
            width: winWidth-40,
            height: winHeight-145,

            ondblClickRow: function(this_row) {
                var rowData = jQuery("#jqGridDevices").getRowData(this_row);
                //mapExpressions(rowId,rowData['id'],rowData['user_name'],listenerID,rowData['userlisteners_id']);
                },
            });
            user_fields_grid.jqGrid('navGrid',user_fields_grid_pager,{edit:true,add:false,del:false, search:true},
                        user_fields_editParams,
                        user_fields_addParams,
                        user_fields_deleteParams,
                        user_fields_searchParams,
                        user_fields_viewParams)


        createUsersSticky2.dialog("open");

    }


    var bell = new Audio("${tg.url('/sounds/ding.mp3')}");
            function dateFmatter ( cellvalue, options, rowObject )
            {
                var utcDate=moment.utc(cellvalue,"YYYY-MM-DD h:mm:ss")
                var localDate=moment(utcDate).local();
                var formatdate = localDate.format("YYYY-MM-DD HH:mm:ss");
                return formatdate;
            }
            function stateFmatter ( cellvalue, options, rowObject ){
                html=cellvalue;
                if ( cellvalue=="0"){html = '<center><span class="glyphicon glyphicon-remove" style="color:red"></span></center>';}
                if ( cellvalue=="1"){html = '<center><span class="glyphicon glyphicon-ok" style="color:green"></span></center>';}
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
            var grid_name_dedicated = '#jgGridDedicated';
            var grid_pager_dedicated= '#listDedicatedEvents';
            var load_url='${h.url()}/admin/loadDedicatedMonitor/?user=${user}';
            var update_url='${h.url()}/admin/updateDedicatedMonitor/?user=${user}';
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
            var grid = jQuery(grid_name_dedicated);

            $(document).ready(function () {
                grid.jqGrid({
                url: load_url,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['${_('Hidden')}', '${_('Name')}', '${_('inicio')}', '${_('Fin')}', '${_('Interval')}', '${_('Application ID')}', '${_('App Nombre')}','${_('Rol')}','${_('Estado')}'],
                colModel: [
                    {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'name',index: 'name', width: 5, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'start',index: 'start',width: 10,align: 'right',editable: true,edittype: 'text',editrules: {required: true}},
                    {name: 'end', index: 'end', width: 5,align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true},search:false},
                    {name: 'interval', index: 'interval', width: 5,align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true},search:false},
                    {name: 'application_id', index: 'application_id', width: 15,align: 'right',hidden: true, editable: true, edittype: 'text', formatter:priorityFmatter, editrules: {required: true},search:false},
                    {name: 'application_name', index: 'application_name', width: 5,align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true},search:false},
                    {name: 'role', index: 'rolestate', width: 2,align: 'right',hidden: false, editable: false, edittype: 'text', formatter:stateFmatter, editrules: {required: true},search:false},
                    {name: 'state', index: 'state', width: 2,align: 'right',hidden: false, editable: false, edittype: 'text', formatter:stateFmatter, editrules: {required: true},search:false},
                ],
                pager: jQuery(grid_pager_dedicated),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'start',
                sortorder: "desc",
                viewrecords: true,
                autowidth: true,
                height: 250,
                ondblClickRow: function(rowId) {
                    var rowData = jQuery("#jgGridDedicated").getRowData(rowId);
                    showDevicesInDedicated(rowData['id'])
                },
                //capt
                //caption: header_container,
            });
            grid.jqGrid('navGrid',grid_pager_dedicated,{edit:false,add:false,del:true, search:false},
                            editParams,
                            addParams,
                            deleteParams,
                            searchParams,
                            viewParams);
            // add custom button

            grid.navButtonAdd(grid_pager_dedicated,
                {
                    buttonicon: "ui-icon-arrow-2-n-s",
                    title: "${_('State')}",
                    caption: "${_('State')}",
                    position: "first",
                    onClickButton: changeMonitorState
                });
            grid.navButtonAdd(grid_pager_dedicated,
                {
                    buttonicon: "ui-icon-plus",
                    title: "${_('Add')}",
                    caption: "${_('Add')}",
                    position: "first",
                    onClickButton: addUserWindow
                });

            grid.navButtonAdd(grid_pager_dedicated,
                {
                    buttonicon: "ui-icon-gear",
                    title: "${_('Unidades')}",
                    caption: "${_('Unidades')}",
                    position: "last",
                    onClickButton:  function(rowId) {
                         var rowKey = grid.getGridParam("selrow");
                         if (rowKey){
                             var rowData = grid.getRowData(rowKey);
                             //addUser(rowData['id']);
                             showDevicesInDedicated(rowData['id'])
                         }
                        else{
                            $.alert("No se ha seleccionado un renglón", { autoClose:false,type: 'danger',});
                            }

                        },
                }
            );

            grid.navButtonAdd(grid_pager_dedicated,
                {
                    buttonicon: "ui-icon-clock",
                    title: "${_('Calendario')}",
                    caption: "${_('Calendario')}",
                    position: "last",
                    onClickButton:  function(rowId) {
                         var rowKey = grid.getGridParam("selrow");
                         if (rowKey){
                             var rowData = grid.getRowData(rowKey);
                             //addUser(rowData['id']);
                             showCalendarInDedicated(rowData['id'])
                         }
                        else{
                            $.alert("No se ha seleccionado un renglón", { autoClose:false,type: 'danger',});
                            }

                        },
                }
            );


            });

            $.extend($.jgrid.nav,{alerttop:1});
            function changeMonitorState() {
                var grid = jQuery('#jgGridDedicated');
                var rowKey = grid.getGridParam("selrow");
                if (rowKey){
                    $.ajax({
                        type: "GET",
                        url: '${h.url()}/admin/updateMonitorState'+"?id="+rowKey+"&user=${user}",
                        contentType: "application/json; charset=utf-8",
                        data: { 'param':'gaugeParameters' },
                        success: function(data) {
                            // data.value is the success return json. json string contains key value
                            return true;
                        },
                        error: function() {
                            $.alert("Error accesing /admin/updateMonitorstate", { autoClose:false,type: 'danger',});
                            return true;
                        },
                        complete: function() {
                        }
                     });
                    }
                else
                    $.alert("No se ha seleccionado un renglón", { autoClose:false,type: 'danger',});

            }

            function addUserWindow(){
                $.ajax({
                          type: "GET",
                          url: '${h.url()}/admin/loadWizard',
                          contentType: "application/json; charset=utf-8",
                          data: { 'name':'pythondispatchms.templates.admin.wizard_dedicated' ,'user':'${user}'},
                          success: function(parameterdata) {
                              //Insert HTML code
                              //$( "#addAssignForm" ).html(parameterdata.expressionformtemplate);

                              var winHeight = 750; //Math.round(window.innerHeight * .50)
                              var winWidth = 1200;//Math.round(window.innerWidth * .50)

                              if ($("#addWizardForm").length){
                                  $("#addWizardForm").remove();
                              }
                              var newDiv = $(document.createElement('div'));

                              newDiv.html(parameterdata.dedwizardtemplate);
                              var DedicatedWizardDialog = newDiv.dialog({
                                  autoOpen: false,
                                  title: "${_('Creación de monitoreo dedicado')}",
                                  height: winHeight,
                                  width: winWidth,
                                  modal: true,
                                  close: function() {
                                      //$('#globalExpForm')[0].reset();
                                      //form[ 0 ].reset();
                                      //allFields.removeClass( "ui-state-error" );
                                  }
                               });
                              DedicatedWizardDialog.data('rowId',1);
                              DedicatedWizardDialog.dialog( "open" );
                          },
                          error: function() {
                              $.alert("Error accessing server /admin/loadTriggerFormTemplate", { autoClose:false,type: 'danger',});
                          },
                          complete: function() {
                          }
                     });
            }

// STOMP
            var dedicatedlistenerclient = Stomp.client('${h.stompServer()}');
            dedicatedlistenerclient.debug=null;
            var email_listener_connect_callback = function() {
                dedicatedlistenerclient.subscribe("/topic/dedicatedlistener", email_listener_subscribe_callback);
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
                            $("#jgGridDedicated").trigger( 'reloadGrid' );
                            break;
                        case 'NEW':
                            $("#jgGridDedicated").trigger( 'reloadGrid' );
                            $.alert("Nuevo monitoreo ", { autoClose:true,type: 'success',});
                            bell.play();
                            break;
                        case 'MSG':
                            $.alert(data, { autoClose:false,type: 'success',});
                            bell.play();
                            break;
                }
              };
            //dedicatedlistenerclient.connect('${h.whoami()}', '${h.password()}', listener_connect_callback, listener_error_callback, '/');
            var stompUser='${h.stompUser()}';
            var stompPass='${h.stompPassword()}';
            dedicatedlistenerclient.connect(stompUser, stompPass, email_listener_connect_callback, email_listener_error_callback, '/');            

});
</script>


    <table style="width:100%">
    <table id="jgGridDedicated" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listDedicatedEvents" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsDedicated" class="scroll" style="text-align:center;"></div>
    </table>
    <br>


</form>
