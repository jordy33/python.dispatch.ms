<script type="text/javascript">
$(document).ready(function () {
function showUsersInRol(rol_name){
                var winHeight = 400; //Math.round(window.innerHeight * .50)
                var winWidth = 810;//Math.round(window.innerWidth * .50)
                var grid_name_devices = 'jgGridRolUsers';
                var pager_name = "jqGridPagerRolUsers";
                var grid_name_users_by_id = '#'+grid_name_devices;
                var pager_name_by_id = '#'+pager_name;
                if ($(grid_name_users_by_id).length){
                    $(grid_name_users_by_id).remove();
                    $(pager_name_by_id).remove();
                }
                if ($("#RolForm").length){
                    $("#RolForm").remove();
                }
                var newDiv = $(document.createElement('div'));
                var html='<div id="RolForm" title="Filter">'
                html=html+'<table id="'+grid_name_devices+'"></table> <div id="'+pager_name+'"> </div>'
                html=html+'</div>'
                newDiv.html(html);

                var createUsersSticky2 = newDiv.dialog({
                    autoOpen: false,
                    title: "Usuarios del Rol",
                    height: winHeight - 20,
                    width: winWidth,
                    modal: true,
                    close: function () {
                    }
                });
                var grid = new jQuery(grid_name_users_by_id);
                grid.jqGrid({
                    url: '${h.url()}/admin/getUsersFromRole'+'?rolname='+rol_name,
                    mtype: "GET",
                    datatype: "json",
                    page: 1,
                    colModel: [
                        {label: "Usuario", name: 'user', key: true, width: 150},
                    ],
                    loadonce: true,
                    viewrecords: true,
                    width: 780,
                    height: 250,
                    rowNum: 10,
                    pager: pager_name_by_id,
                    ondblClickRow: function (rowId) {
                    },

                });
                grid.navGrid(pager_name_by_id, {
                    search: true,
                    add: false,
                    edit: false,
                    del: false,
                    refresh: true
                }, {}, {}, {}, {});

                createUsersSticky2.dialog("open");
}


    var cellsrenderer = function (row, column, value) {
        return '<div style="text-align: center; margin-top: 5px;">' + value + '</div>';
    }
    var columnsrenderer = function (value) {
        return '<div style="text-align: center; margin-top: 5px;">' + value + '</div>';
    }
    var bell = new Audio("${tg.url('/sounds/ding.mp3')}");
            var grid_name_email = '#jgGridRoles';
            var grid_pager_email= '#listRoles';
            var load_url='${h.url()}/admin/loadRoles/?user=${user}';
            var update_url='${h.url()}/admin/updateRoles/?user=${user}';
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
                colNames: ['${_('Hidden')}', '${_('Name')}'],
                colModel: [
                    {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'name',index: 'name', renderer: columnsrenderer, cellsrenderer: cellsrenderer, width: 5, align: 'center',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                ],
                pager: jQuery(grid_pager_email),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'name',
                sortorder: "desc",
                viewrecords: true,
                autowidth: true,
                height: 250,
                ondblClickRow: function(rowId) {
                    var rowData = jQuery("#jgGridRoles").getRowData(rowId);
                    showUsersInRol(rowData['name'])
                },
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
                $.ajax({
                          type: "GET",
                          url: '${h.url()}/admin/loadWizard',
                          contentType: "application/json; charset=utf-8",
                          data: { 'name':'pythondispatchms.templates.admin.wizard_roles','user':'${user}' },
                          success: function(parameterdata) {
                              var winHeight = 750; //Math.round(window.innerHeight * .50)
                              var winWidth = 1200;//Math.round(window.innerWidth * .50)

                              if ($("#addWizardForm").length){
                                  $("#addWizardForm").remove();
                              }
                              var newDiv = $(document.createElement('div'));

                              newDiv.html(parameterdata.dedwizardtemplate);
                              var DedicatedWizardDialog = newDiv.dialog({
                                  autoOpen: false,
                                  title: "${_('Creación de Rol')}",
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
                              alert("Error accessing wizard de Rol")
                          },
                          complete: function() {
                          }
                     });
            }

            // STOMP
            var adminlistenerclient = Stomp.client('${h.stompServer()}');
            adminlistenerclient.debug=null;
            var listener_connect_callback = function() {
                adminlistenerclient.subscribe("/topic/rolelistener", listener_subscribe_callback);
                // called back after the client is connected and authenticated to the STOMP server
              };
            var listener_error_callback = function(error) {
            };
            var listener_subscribe_callback = function(message) {

                var msg = message.body;
                var payload = msg.split('|');
                var command = payload[0];
                var data = payload[1];
                switch (command) {
                        case 'RELOAD':
                            $("#jgGridRoles").trigger( 'reloadGrid' );
                            $.alert("Reload", { autoClose:true,type: 'success',});
                            break;
                        case 'NEW':
                            $("#jgGridRoles").trigger( 'reloadGrid' );
                            $.alert("New Role", { autoClose:true,type: 'success',});
                            bell.play();
                            break;
                        case 'MSG':
                            $.alert(data, { autoClose:false,type: 'success',});
                            bell.play();
                            break;
                }
              };
            // adminlistenerclient.connect('${h.whoami()}', '${h.password()}', listener_connect_callback, listener_error_callback, '/');
            var stompUser='${h.stompUser()}';
            var stompPass='${h.stompPassword()}';
            adminlistenerclient.connect(stompUser, stompPass, listener_connect_callback, listener_error_callback, '/');

});
</script>


    <table style="width:100%">
    <table id="jgGridRoles" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listRoles" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsRoles" class="scroll" style="text-align:center;"></div>
    </table>
    <br>


</form>
