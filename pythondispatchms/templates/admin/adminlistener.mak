<style type="text/css">
</style>
<script>
            var bell = new Audio("${tg.url('/sounds/ding.mp3')}");
            function dateFmatter ( cellvalue, options, rowObject )
            {
                var utcDate=moment.utc(cellvalue,"YYYY-MM-DD h:mm:ss")
                var localDate=moment(utcDate).local();
                var formatdate = localDate.format("YYYY-MM-DD HH:mm:ss");
                return formatdate;
            }
            function statusFmatter ( cellvalue, options, rowObject ){
                html=cellvalue;
                if ( cellvalue=="0"){html = '<center><span class="glyphicon glyphicon-remove" style="color:red"></span></center>';}
                if ( cellvalue=="1"){html = '<center><span class="glyphicon glyphicon-ok" style="color:green"></span></center>';}
                return html;
            }
                var username = 'dispatch';
                var password = 'managepass';

                function make_base_auth(user, password) {
                    var tok = user + ':' + password;
                    var hash = btoa(tok);
                    return "Basic " + hash;
                }
                $.ajaxSetup({
                    beforeSend: function (xhr)
                    {
                    xhr.setRequestHeader("Content-Type","application/json");
                    xhr.setRequestHeader("Accept","application/json");
                    xhr.setRequestHeader( "Authorization", make_base_auth(username,password));
                    }
                });
            var grid_name = '#jgGridListeners';
            var grid_pager= '#listPagerListeners';
            var load_url='${h.url()}/admin/loadListenerAdmin?user=${user}';
            var update_url='${h.url()}/admin/updateListenerAdmin?user=${user}';
            //var header_container='${_('Alerts')}';
            var addParams = {left: 0,width: window.innerWidth-700,top: 20,height: 190,url: update_url,mtype: 'GET', closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var editParams = {left: 0,width: window.innerWidth-700,top: 20,height: 200,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                    width: "500",
                    editfunc: function (rowid) {
                    }
                };
            var deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url,modal: true, };
            var listenergrid = jQuery(grid_name);

            $(document).ready(function () {
                listenergrid.jqGrid({
                url: load_url,
                datatype: 'json',
                mtype: 'GET',
                colNames: ["${_('Hidden')}", "${_('Listener ID')}", "${_('Description')}", "${_('Time Stamp')}","${_('State')}","${_('Log State')}"],
                colModel: [
                    {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: true}},
                    {name: 'listener_id',index: 'listener_id',width: 25,align: 'right',hidden: false,editable: false,edittype: 'text',editrules: {required: false}},
                    {name: 'name',index: 'name', width: 25, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'time_stamp',index: 'time_stamp', width: 14, align: 'right',hidden: false,editable: false, edittype: 'text', formatter:dateFmatter,editrules: {required: false}},
                    {name: 'state', index: 'state', width: 8,align: 'right',hidden: false, editable: false, edittype: 'text', formatter:statusFmatter, editrules: {required: true},search:false},
                    {name: 'logstate', index: 'logstate', width: 8,align: 'right',hidden: false, editable: false, edittype: 'text', formatter:statusFmatter, editrules: {required: true},search:false},
                ],
                pager: jQuery(grid_pager),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'time_stamp',
                sortorder: "desc",
                viewrecords: true,
                autowidth: true,
                height: 250,
                ondblClickRow: function(rowId) {
                    listenerFieldsMapper(rowId)
                },
                //caption: header_container,
            });
            listenergrid.jqGrid('navGrid',grid_pager,{edit:true,add:false,del:true, search:true},
                            editParams,
                            addParams,
                            deleteParams,
                            searchParams,
                            viewParams);
            // add custom button
            listenergrid.navButtonAdd(grid_pager,
                {
                    buttonicon: "ui-icon-arrow-2-n-s",
                    title: "${_('Log State')}",
                    caption: "${_('Log State')}",
                    position: "first",
                    onClickButton: changeLogListenerState
                }
            );
            listenergrid.navButtonAdd(grid_pager,
                {
                    buttonicon: "ui-icon-arrow-2-n-s",
                    title: "${_('State')}",
                    caption: "${_('State')}",
                    position: "first",
                    onClickButton: changeListenerState
                }
            );

            listenergrid.navButtonAdd(grid_pager,
                {
                    buttonicon: "ui-icon-person",
                    title: "${_('Grupos')}",
                    caption: "${_('Grupos')}",
                    position: "last",
                    onClickButton:  function(rowId) {
                         var rowKey = listenergrid.getGridParam("selrow");
                         if (rowKey){
                             var rowData = listenergrid.getRowData(rowKey);
                             addUser(rowData['id'],rowData['listener_id']);
                         }
                        else{
                            alert("No rows are selected");
                            }

                        },
                }
            );

            listenergrid.navButtonAdd(grid_pager,
                {
                    buttonicon: "ui-icon-flag",
                    title: "${_('Eventos')}",
                    caption: "${_('Eventos')}",
                    position: "last",
                    onClickButton:  function(rowId) {
                         var rowKey = listenergrid.getGridParam("selrow");
                         if (rowKey){
                             var rowData = listenergrid.getRowData(rowKey);
                             addEvents(rowData['id'],rowData['listener_id']);
                         }
                        else{
                            alert("No rows are selected");
                            }

                        },
                }
            );

            }            );

            $.extend($.jgrid.nav,{alerttop:1});
            function addEvents(rowId,listenerID){
                var lid=listenerID;
                var winHeight = 400; //Math.round(window.innerHeight * .50)
                var winWidth = 810;//Math.round(window.innerWidth * .50)
                var grid_name = 'jgGrid4Events';
                var pager_name = "jqGridPager4Events";
                var grid_name_by_id = '#'+grid_name;
                var pager_name_by_id = '#'+pager_name;
                if ($(grid_name_by_id).length){
                    $(grid_name_by_id).remove();
                    $(pager_name_by_id).remove();
                }

                var newDiv = $(document.createElement('div'));
                newDiv.html('<table id="'+grid_name+'"></table> <div id="'+pager_name+'"> </div>');

                var createUsersSticky = newDiv.dialog({
                    autoOpen: false,
                    title: "Agregar Eventos",
                    height: winHeight ,
                    width: winWidth ,
                    modal: true,
                    close: function () {
                    }
                });


                var load_url='${h.url()}/admin/loadEvents?listener_id='+listenerID;
                var update_url='${h.url()}/admin/updateEvents?listener_id='+listenerID;

                var header_container='Eventos';
                var addParams = {left: 0,width: window.innerWidth-700,top: 20,height: 190,url: update_url,mtype: 'GET', closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
                var editParams = {left: 0,width: window.innerWidth-700,top: 20,height: 200,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                    width: "500",
                    editfunc: function (rowid) {
                    alert('The "Edit" button was clicked with rowid=' + rowid);
                    }
                };
                var deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
                var viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
                var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url,modal: true, };
                var grid = jQuery(grid_name_by_id);
                grid.jqGrid({
                    url: load_url,
                    datatype: 'json',
                    mtype: 'GET',
                    colNames: ['id','Id Evento', 'Descripción'],
                    colModel: [
                        {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                        {name: 'event_id', index: 'event_id', width:5,align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                        {name: 'event_desc', index: 'event_desc', width:34,align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                    ],
                    pager: jQuery(pager_name_by_id),
                    rowNum: 10,
                    rowList: [10, 50, 100],
                    sortname: 'event_id',
                    sortorder: "asc",
                    viewrecords: true,
                    height: winHeight-140 ,
                    width: winWidth-60 ,
                    caption: header_container,

                });
                grid.jqGrid('navGrid',pager_name_by_id,{edit:true,add:true,del:true, search:true},
                                editParams,
                                addParams,
                                deleteParams,
                                searchParams,
                                viewParams);

                    createUsersSticky.dialog("open");

            }

            function addUser(rowId,listenerID){
                //var winHeight=Math.round(window.innerHeight*.50);
                //var winWidth=Math.round(window.innerWidth*.85);
                var winHeight=450;
                var winWidth=1000;
                // Event Routines
                var user_fields_grid_name = '#jqGridUser';
                var user_fields_grid_pager= '#UserTables';

                var user_fields_load_url='${h.url()}/admin/loadListenerUsers?id='+rowId;
                var user_fields_update_url='${h.url()}/admin/updateListenerUsers';
                var user_fields_addParams = {left: 0,width: window.innerWidth-700,top: 20,height: 190,url: user_fields_update_url,mtype: 'GET', closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
                var user_fields_editParams = {left: 0,width: window.innerWidth-700,top: 20,height: 200,url: user_fields_update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                    width: "500",
                    editfunc: function (rowid) {
                    alert('The "Edit" button was clicked with rowid=' + rowid);
                    }
                };
                var user_fields_deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: user_fields_update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
                var user_fields_viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: user_fields_update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
                var user_fields_searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: user_fields_update_url,modal: true, };
                var user_fields_grid = jQuery(user_fields_grid_name);
                user_fields_grid.jqGrid({
                    url: user_fields_load_url,
                    datatype: 'json',
                    mtype: 'GET',
                    colNames: ['id', "${_('User Name')}","${_('State')}","${_('Finalize Traffic')}",'hidden'],
                    colModel: [
                        {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                        {name: 'user_name',index: 'user_name', width: 25, align: 'right', hidden: false, editable: true, edittype: 'text',editrules: {required: false}},
                        {name: 'state', index: 'state', width: 5,align: 'right',hidden: false, editable: true, formatter:statusFmatter,edittype: 'text', editrules: {required: false}},
                        {name: 'finalize', index: 'finalize', width: 5,align: 'right',hidden: false, editable: true, formatter:statusFmatter,edittype: 'text', editrules: {required: false}},
                        {name: 'userlisteners_id', index: 'userlisteners_id', width: 5,align: 'right',hidden: true},
                    ],
                    pager: jQuery(user_fields_grid_pager),
                    rowNum: 10,
                    rowList: [10, 50, 100],
                    sortname: 'user_name',
                    sortorder: "asc",
                    viewrecords: true,
                    width: winWidth-40,
                    height: winHeight-145,

                    ondblClickRow: function(this_row) {
                        var rowData = jQuery("#jqGridUser").getRowData(this_row);
                        mapExpressions(rowId,rowData['id'],rowData['user_name'],listenerID,rowData['userlisteners_id']);
                        },
                    });
                    user_fields_grid.jqGrid('navGrid',user_fields_grid_pager,{edit:false,add:false,del:true, search:true},
                                user_fields_editParams,
                                user_fields_addParams,
                                user_fields_deleteParams,
                                user_fields_searchParams,
                                user_fields_viewParams)
                    user_fields_grid.navButtonAdd(user_fields_grid_pager,
                        {
                            buttonicon: "ui-icon-plus",
                            title: "${_('Add Groups')}",
                            caption: "${_('Add Groups')}",
                            position: "last",
                            onClickButton:function() {
                               addUserWindow(rowId,user_fields_grid_name)
                        }
                    });
                    user_fields_grid.navButtonAdd(user_fields_grid_pager,
                        {
                            buttonicon: "ui-icon-arrow-2-n-s",
                            title: "${_('State')}",
                            caption: "${_('State')}",
                            position: "last",
                            onClickButton:function() {
                               var rowKey = user_fields_grid.getGridParam("selrow");
                               if (rowKey){
                                   var rowData = user_fields_grid.getRowData(rowKey);
//                                   addUser(rowData['id'],rowData['listener_id']);
                                   changeListenerUserState(rowData['id']);
                               }
                               else{
                                   alert("No rows are selected");
                               }
                        }
                    });
                $("#UserGrid").show();
                var editFieldsDialog = $( "#UserGrid" ).dialog({
                    autoOpen: false,
                    height: winHeight,
                    width: winWidth,
                    title: "${_('Users for listener ')}"+listenerID,
                    modal: true,
                    close: function() {
                        user_fields_grid.jqGrid('GridUnload');
                    }
                });
                $("#UserGrid").trigger( 'reloadGrid', { fromServer: true, page: 1 } );
                editFieldsDialog.data('rowId',1);
                editFieldsDialog.dialog( "open" );

            }

            function addUserWindow(listener,topgrid){
                var winHeight = 400; //Math.round(window.innerHeight * .50)
                var winWidth = 810;//Math.round(window.innerWidth * .50)
                var grid_name = 'jgGrid4Users';
                var pager_name = "jqGridPager4Users";
                var grid_name_by_id = '#'+grid_name;
                var pager_name_by_id = '#'+pager_name;
                if ($(grid_name_by_id).length){
                    $(grid_name_by_id).remove();
                    $(pager_name_by_id).remove();
                }

                var newDiv = $(document.createElement('div'));
                newDiv.html('<table id="'+grid_name+'"></table> <div id="'+pager_name+'"> </div>');

                var createUsersSticky = newDiv.dialog({
                    autoOpen: false,
                    title: "Double click to add a user",
                    height: winHeight - 20,
                    width: winWidth,
                    modal: true,
                    close: function () {
                    }
                });
                var grid = new jQuery(grid_name_by_id);
                grid.jqGrid({
                    url: '${h.url()}/admin/getGroups',
                    mtype: "GET",
                    datatype: "json",
                    page: 1,
                    colModel: [
                        {label: "User Name", name: 'username', key: true, width: 150},
                    ],
                    loadonce: true,
                    viewrecords: true,
                    width: 780,
                    height: 250,
                    rowNum: 10,
                    pager: pager_name_by_id,
                    ondblClickRow: function (rowId) {
                        doDoubleClick(rowId)
                    },

                });
                grid.navGrid(pager_name_by_id, {
                    search: true,
                    add: false,
                    edit: false,
                    del: false,
                    refresh: true
                }, {}, {}, {}, {});

                function doDoubleClick(rowId) {

                    var rowData = jQuery(grid_name_by_id).getRowData(rowId);
                    $.ajax({
                        type: "GET",
                        url: '${h.url()}/admin/addUsersToListener?id='+listener+"&username="+rowData['username'],
                        contentType: "application/json; charset=utf-8",
                        data: { 'param':'gaugeParameters' },
                        success: function(data) {
                            $.alert("Success adding user ", { autoClose:true,type: 'success'});
                            $("#jqGridUser").trigger( 'reloadGrid', { fromServer: true, page: 1 } );
                        },
                        error: function() {
                        $.alert("Error accessing traffic/addPending", { autoClose:false,});
                        return true;
                        },
                        complete: function() {

                        }
                    });
                    createUsersSticky.dialog("close");
                }
                createUsersSticky.dialog("open");
            }

            function mapExpressions(listener_id,user_id,user_name,listener_name,userlisteners_id){
                function priorityFmatter ( cellvalue, options, rowObject )
                {
                    html=cellvalue;
                    if ( cellvalue==1){html = '<center><div style="background-color:red"><div style="color:white">1</div></div></center>';}
                    if ( cellvalue==2){html = '<center><div style="background-color:orange" style="text-align:center">2</div></center>';}
                    if ( cellvalue==3){html = '<center><div style="background-color:yellow" style="text-align:center">3</div></center>';}
                    if ( cellvalue==4){html = '<center><div style="background-color:green"><div style="color:white">4</div></div></center>';}
                    if ( cellvalue==5){html = '<center><div style="background-color:blue"><div style="color:white">5</div></div></center>';}
                    return html;
                }
                var winHeight = 690; // Math.round(window.innerHeight * .78)
                var winWidth = 650;// Math.round(window.innerWidth * .40)

                var global_exp_load_url='${h.url()}/admin/loadGlobalExp?userlisteners_id='+userlisteners_id;

                var grid_name_1 = 'jgGridGlobalExp';
                var pager_name_1 = "jqGridPageGlobalExp";
                var grid_name_by_id_1 = '#'+grid_name_1;
                var pager_name_by_id_1 = '#'+pager_name_1;
                if ($(grid_name_by_id_1).length){
                    $(grid_name_by_id_1).remove();
                    $(pager_name_by_id_1).remove();
                }

                var trigger_user_load_url='${h.url()}/admin/loadTriggerByUser?user_id='+user_id;
                var grid_name_2 = 'jgGridTrigger';
                var pager_name_2 = "jqGridPagerTrigger";
                var grid_name_by_id_2 = '#'+grid_name_2;
                var pager_name_by_id_2 = '#'+pager_name_2;
                if ($(grid_name_by_id_2).length){
                    $(grid_name_by_id_2).remove();
                    $(pager_name_by_id_2).remove();
                }

                var newDiv = $(document.createElement('div'));
                var code ='<table id="'+grid_name_1+'"></table> <div id="'+pager_name_1+'"> </div>'+'<br> <div>'+"${_('Triggers for:')}"+user_name+'</div> <br>'+
                    '<table id="'+grid_name_2+'"></table> <div id="'+pager_name_2+'"> </div>'
                newDiv.html(code);
                var ntitle= "${_('Expresiones globales para la escucha')}";
                var createExpWindow = newDiv.dialog({
                    autoOpen: false,
                    title:ntitle +': '+listener_name,
                    height: winHeight - 20,
                    width: winWidth,
                    modal: true,
                    close: function () {
                    }
                });
                var grid_1 = new jQuery(grid_name_by_id_1);
                grid_1.jqGrid({
                    url: global_exp_load_url,
                    mtype: "GET",
                    datatype: "json",
                    page: 1,
                    colNames: ['Id', "${_('Listener Expressions')}",'Hidden','Hidden','Hidden','Hidden'],
                    colModel: [
                        {name: 'id',index: 'id', align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: true}},
                        {name: 'expression', index: 'expression', align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                        {name: 'expression_id', index: 'expression_id', align: 'right',hidden: true},
                        {name: 'expression_op', index: 'expression_op', align: 'right',hidden: true},
                        {name: 'expression_value', index: 'expression_value', align: 'right',hidden: true},
                        {name: 'explisteners_id', index: 'explisteners_id', align: 'right',hidden: true},
                    ],
                    viewrecords: true,
                    width: 600,
                    height: 200,
                    rowNum: 9,
                    rowList: [9, 10, 100],
                    sortname: 'id',
                    sortorder: "asc",
                    pager: pager_name_by_id_1,
                    ondblClickRow: function (rowId) {

                    },

                });
                grid_1.navGrid(pager_name_by_id_1, {
                    search: true,
                    add: false,
                    edit: false,
                    del: true,
                    refresh: true
                }, {}, {}, {url: '${h.url()}/admin/updateGlobalExp/',mtype: 'GET'}, {url: '${h.url()}/admin/updateGlobalExp/',mtype: 'GET'},{});
                //edit,add,delete,search,view

                grid_1.navButtonAdd(pager_name_by_id_1,
                {
                    buttonicon: "ui-icon-plus",
                    title: "${_('Add')}",
                    caption: "${_('Add')}",
                    position: "last",
                    onClickButton:function() { addGlobalExpression(listener_id); }
                });

                function addGlobalExpression(rowId){

                    $.ajax({
                        type: "GET",
                        url: '${h.url()}/admin/loadExpressionsFormTemplate/',
                        contentType: "application/json; charset=utf-8",
                        data: { 'id':rowId },
                        success: function(parameterdata) {
                            //Insert HTML code
                            //$( "#addAssignForm" ).html(parameterdata.expressionformtemplate);
                            var winHeight = 400; //Math.round(window.innerHeight * .50)
                            var winWidth = 600;//Math.round(window.innerWidth * .50)
                            var addGlobalExpButtons = {
                                    "${_('Add')}": function() {
                                        var expressionfield = $('#selfield option:selected').filter(':selected').text();
                                        var expressionoperation = $('#seloperation option:selected').filter(':selected').text();
                                        var expressionvalue= encodeURIComponent($('#expressionvalue').val());
                                        $.ajax({
                                                type: "GET",
                                                url:  '${h.url()}/admin/addGlobalExp'+"?id="+rowId+"&field="+expressionfield+"&operation="+expressionoperation+"&value="+expressionvalue,
                                                contentType: "application/json; charset=utf-8",
                                                data: { 'param':'gaugeParameters' },
                                                success: function(data) {
                                                    // data.value is the success return json. json string contains key value
                                                     $('#jgGridGlobalExp').trigger( 'reloadGrid' );
                                                },
                                                error: function() {
                                                     $.alert("Error accessing /admin/addGlobalExp", { autoClose:false,});
                                                    return true;
                                                },
                                                complete: function() {
                                                }
                                                });
                                            $('#globalExpForm')[0].reset();
                                            addUserTriggerDialog.dialog( "close" );


                                    },
                                    "${_('Close')}": function() {
                                        $('#globalExpForm')[0].reset();
                                        addUserTriggerDialog.dialog( "close" );
                                    }
                            };
                            if ($("#addglobalExpForm").length){
                                $("#addglobalExpForm").remove();
                            }
                            var newDiv = $(document.createElement('div'));

                            newDiv.html(parameterdata.expressionformtemplate);
                            var addUserTriggerDialog = newDiv.dialog({
                                autoOpen: false,
                                title:'Add Listener global expression',
                                height: winHeight-100,
                                width: winWidth-200,
                                modal: true,
                                buttons: addGlobalExpButtons,
                                close: function() {
                                    //$('#globalExpForm')[0].reset();
                                    //form[ 0 ].reset();
                                    //allFields.removeClass( "ui-state-error" );
                                }
                             });
                            addUserTriggerDialog.data('rowId',1);
                            addUserTriggerDialog.dialog( "open" );
                        },
                        error: function() {
                            alert("Error accessing server /admin/loadExpressionsFormTemplate")
                        },
                        complete: function() {
                        }
                    });

                }

                // Second Window

                var grid_2 = new jQuery(grid_name_by_id_2);
                grid_2.jqGrid({
                    url: trigger_user_load_url,
                    mtype: "GET",
                    datatype: "json",
                    page: 1,
                    colNames: ['Id', "${_('User Expressions')}","${_('Priority')}","${_('Sound')}"],
                    colModel: [
                        {name: 'id',index: 'id', align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: true}},
                        {name: 'expression', index: 'expression', width: 150, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                        {name: 'priority', index: 'priority', formatter:priorityFmatter, width: 15, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                        {name: 'sound', index: 'sound',  width: 15, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                    ],
                    viewrecords: true,
                    width: 600,
                    height: 200,
                    rowNum: 9,
                    rowList: [9, 10, 100],
                    sortname: 'id',
                    sortorder: "asc",
                    pager: pager_name_by_id_2,
                    ondblClickRow: function (this_row) {
                        var rowData = jQuery("#jgGridTrigger").getRowData(this_row);
                        addUserFilter(rowData["id"]);
                    },

                });
                grid_2.navGrid(pager_name_by_id_2, {
                    search: true,
                    add: false,
                    edit: false,
                    del: true,
                    refresh: true
                }, {}, {}, {url: '${h.url()}/admin/updateTriggerByUser',mtype: 'GET'}, {url: '${h.url()}/admin/updateTriggerByUser',mtype: 'GET'});
                grid_2.navButtonAdd(pager_name_by_id_2,
                {
                    buttonicon: "ui-icon-plus",
                    title: "${_('Add')}",
                    caption: "${_('Add')}",
                    position: "last",
                    onClickButton:function() { addTriggerByUser(listener_id); }
                });
                function addTriggerByUser(listener_id){
                $.ajax({
                        type: "GET",
                        url: '${h.url()}/admin/loadTriggerFormTemplate',
                        contentType: "application/json; charset=utf-8",
                        data: { 'id':listener_id },
                        success: function(parameterdata) {
                            //Insert HTML code
                            //$( "#addAssignForm" ).html(parameterdata.expressionformtemplate);

                            var winHeight = 400; //Math.round(window.innerHeight * .50)
                            var winWidth = 600;//Math.round(window.innerWidth * .50)
                            var addTriggerbyUserButtons = {
                                    "${_('Add')}": function() {
                                        var payload_exp=""
                                        var fields_selected=""
                                        var element_count = Number(parameterdata.count)
                                        var element_checked=0
                                        for (item = 1; item <= element_count; item++) {
                                            var expression_value='#id_chk'+item;
                                            if($(expression_value).is(':checked')){
                                                var names = $(expression_value).map(function(){ return this.name; });
                                                fields_selected=fields_selected+$(expression_value).val()+"|"
                                                payload_exp=payload_exp+names.get()+" and "
                                                element_checked++;
                                            }

                                        }
                                        if (element_checked>0){
                                            payload_exp=payload_exp.slice(0, - 5);
                                            fields_selected=fields_selected.slice(0, - 1);
                                            payload_exp=encodeURIComponent(payload_exp);
                                            var priority = $('#priority option:selected').filter(':selected').text();
                                            var sound = $('#sound option:selected').filter(':selected').text();
                                            $.ajax({
                                                    type: "GET",
                                                    url: '${h.url()}/admin/addUserTrigger'+"?user_id="+user_id+"&expression="+payload_exp+"&priority="+priority+"&sound="+sound+"&selectedFields="+fields_selected,
                                                    contentType: "application/json; charset=utf-8",
                                                    data: { 'param':'gaugeParameters' },
                                                    success: function(data) {
                                                        // data.value is the success return json. json string contains key value
                                                         $('#jgGridTrigger').trigger( 'reloadGrid' );
                                                    },
                                                    error: function() {
                                                         $.alert("Error accessing /admin/addGlobalExp", { autoClose:false,});
                                                        return true;
                                                    },
                                                    complete: function() {
                                                    }
                                            });
                                        }
                                        $('#triggerExpForm')[0].reset();
                                        addTriggerbyUserDialog.dialog( "close" );
                                    },
                                        "${_('Close')}": function() {
                                            $('#triggerExpForm')[0].reset();
                                            addTriggerbyUserDialog.dialog( "close" );
                                    }
                            };

                            if ($("#addTriggerForm").length){
                                $("#addTriggerForm").remove();
                            }
                            var newDiv = $(document.createElement('div'));

                            newDiv.html(parameterdata.triggerformtemplate);
                            var addTriggerbyUserDialog = newDiv.dialog({
                                autoOpen: false,
                                title: "${_('User Expressions')}",
                                height: winHeight-100,
                                width: winWidth-200,
                                modal: true,
                                buttons: addTriggerbyUserButtons,
                                close: function() {
                                    //$('#globalExpForm')[0].reset();
                                    //form[ 0 ].reset();
                                    //allFields.removeClass( "ui-state-error" );
                                }
                             });
                            addTriggerbyUserDialog.data('rowId',1);
                            addTriggerbyUserDialog.dialog( "open" );
                        },
                        error: function() {
                            alert("Error accessing server /admin/loadTriggerFormTemplate")
                        },
                        complete: function() {
                        }
                    });

                }


                createExpWindow.dialog("open");
            }

            function addUserFilter(trigger_id){
                function actionFmatter ( cellvalue, options, rowObject ){
                    html=cellvalue;
                    if ( cellvalue=="0"){html = '<center><div style="background-color:red"><div style="color:white">DISCARD</div></div></center>';}
                    if ( cellvalue=="1"){html = '<center><div style="background-color:green"><div style="color:white">KEEP</div></div></center>';}
                    return html;
                }
                function filterNameFmatter ( cellvalue, options, rowObject ){
                    html=cellvalue;
                    if ( cellvalue==1){html ='<center><div style="background-color:blue"><div style="color:white">Event Counter</div></div></center>';}
                    return html;
                }
                var winHeight=450;
                var winWidth=1000;

                var user_filter_load_url='${h.url()}/admin/loadFilterByUser?user_trigger_id='+trigger_id
                var grid_name_1 = 'jgGridUserFilter';
                var pager_name_1 = "jqGridPageUserFilter";
                var grid_name_by_id_1 = '#'+grid_name_1;
                var pager_name_by_id_1 = '#'+pager_name_1;
                if ($(grid_name_by_id_1).length){
                    $(grid_name_by_id_1).remove();
                    $(pager_name_by_id_1).remove();
                }
                var newDiv = $(document.createElement('div'));
                newDiv.html('<table id="'+grid_name_1+'"></table> <div id="'+pager_name_1+'"> </div>');

                var createExpWindow = newDiv.dialog({
                    autoOpen: false,
                    title: "${_('Filter Expressions')}",
                    height: winHeight - 20,
                    width: winWidth,
                    modal: true,
                    close: function () {
                    }
                });
                var grid_1 = new jQuery(grid_name_by_id_1);
                grid_1.jqGrid({
                    url: user_filter_load_url,
                    datatype: 'json',
                    mtype: 'GET',
                    colNames: ['id', "${_('Filter name')}", "${_('Expression')}","${_('Action')}","${_('Enviar a Venus cuando en una hora')}","${_('Counter')}"],
                    colModel: [
                        {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                        {name: 'filter_id',index: 'filter_id', width: 20, align: 'right', hidden: false, editable: true, formatter:filterNameFmatter, edittype: 'text',editrules: {required: false}},
                        {name: 'expression',index: 'expression', width: 40, align: 'right', hidden: false, editable: true, edittype: 'text',editrules: {required: false}},
                        {name: 'action', index: 'action', width: 7,align: 'right',hidden: false, editable: true, formatter:actionFmatter,edittype: 'text', editrules: {required: false}},
                        {name: 'reset_expression',index: 'reset_expression', width: 40, align: 'right', hidden: false, editable: true, edittype: 'text',editrules: {required: false}},
                        {name: 'counter',index: 'counter', width: 5, align: 'right', hidden: true, editable: true, edittype: 'text',editrules: {required: false}},
                    ],
                    pager: jQuery(pager_name_by_id_1),
                    rowNum: 10,
                    rowList: [10, 50, 100],
                    sortname: 'expression',
                    sortorder: "asc",
                    viewrecords: true,
                    width: winWidth-40,
                    height: winHeight-145,

                    ondblClickRow: function(this_row) {
                        var rowData = jQuery("#jgGridUserFilter").getRowData(this_row);
                        mapExpressions(rowId,rowData['id'],rowData['user_name']);
                        },
                    });
                grid_1.navGrid(pager_name_by_id_1, {
                    search: true,
                    add: false,
                    edit: false,
                    del: true,
                    refresh: true

                }, {}, {}, {url: '${h.url()}/admin/updateFilterByUser',mtype: 'GET'}, {multipleSearch: true,},{});

                grid_1.navButtonAdd(pager_name_by_id_1,
                {
                    buttonicon: "ui-icon-plus",
                    title: "${_('Add')}",
                    caption: "${_('Add')}",
                    position: "last",
                    onClickButton:function(this_row) {
                        var rowData = jQuery("#jqGridUser").getRowData(this_row);
                        addUserFilterWidget(trigger_id);
                    }

                });
                createExpWindow.dialog("open");
            }
            function addUserFilterWidget(trigger_id){
                $.ajax({
                    type: "GET",
                    url: '${h.url()}/admin/loadUserFilterTemplate',
                    contentType: "application/json; charset=utf-8",
                    data: { 'id':trigger_id },
                    success: function(parameterdata) {
                        //Insert HTML code
                        //$( "#addAssignForm" ).html(parameterdata.expressionformtemplate);
                        var winHeight = 400; //Math.round(window.innerHeight * .50)
                        var winWidth = 600;//Math.round(window.innerWidth * .50)
                        var addGlobalExpButtons = {
                                "${_('Add')}": function() {
                                    var filteroperation ='';//encodeURIComponent( $('#seloperation option:selected').filter(':selected').text());
                                    var fieldvalue= encodeURIComponent($('#fieldvalue').val());
                                    var action = '';//encodeURIComponent($('#action option:selected').filter(':selected').text());
                                    var resetoperation = '';//encodeURIComponent($('#resetoperation option:selected').filter(':selected').text());
                                    var resetvalue= encodeURIComponent($('#resetfieldvalue').val());

                                    $.ajax({
                                            type: "GET",
                                            url: '${h.url()}/admin/addUserTriggerFilter?id='+trigger_id+"&filteroperation="+filteroperation+"&fieldvalue="+fieldvalue+"&action="+action+"&resetoperation="+resetoperation+"&resetvalue="+resetvalue,
                                            contentType: "application/json; charset=utf-8",
                                            data: { 'param':'gaugeParameters' },
                                            success: function(data) {
                                                // data.value is the success return json. json string contains key value
                                                 $('#jgGridUserFilter').trigger( 'reloadGrid' );
                                            },
                                            error: function() {
                                                 $.alert("Error accessing /admin/addGlobalExp", { autoClose:false,});
                                                return true;
                                            },
                                            complete: function() {
                                            }
                                    });
                                         $('#triggerassignForm')[0].reset();
                                        addUserTriggerDialog.dialog( "close" );


                                },
                                "${_('Close')}": function() {
                                    $('#triggerassignForm')[0].reset();
                                    addUserTriggerDialog.dialog( "close" );
                                }
                        };
                        if ($("#usertriggerformat").length){
                            $("#usertriggerformat").remove();
                        }
                        var newDiv = $(document.createElement('div'));
                        newDiv.html(parameterdata.expressionformtemplate);
                        var addUserTriggerDialog = newDiv.dialog({
                            autoOpen: false,
                            title: "${_('User Trigger Event Filter')}",
                            height: 300,
                            width: 400,
                            modal: true,
                            buttons: addGlobalExpButtons,
                            close: function() {
                                //$('#globalExpForm')[0].reset();
                                //form[ 0 ].reset();
                                //allFields.removeClass( "ui-state-error" );
                            }
                         });
                        addUserTriggerDialog.data('rowId',1);
                        addUserTriggerDialog.dialog( "open" );
                    },
                    error: function() {
                        alert("Error accessing server /admin/loadExpressionsFormTemplate")
                    },
                    complete: function() {
                    }
                });

            }
            function listenerFieldsMapper(rowId){
                function assignFmatter ( cellvalue, options, rowObject )
                {
                    if ( cellvalue==0){html = 'NONE';}
                    if ( cellvalue==1){html = 'IMEI';}
                    if ( cellvalue==2){html = 'EVENT_ID';}
                    if ( cellvalue==3){html = 'EVENT_DESC';}
                    if ( cellvalue==4){html = 'LATITUDE';}
                    if ( cellvalue==5){html = 'LONGITUDE';}
                    if ( cellvalue==6){html = 'SPEED';}
                    if ( cellvalue==7){html = 'AZIMUTH';}
                    if ( cellvalue==8){html = 'VALID';}
                    if ( cellvalue==9){html = 'DATETIME';}
                    if ( cellvalue==10){html = 'CLIENT_ID';}
                    if ( cellvalue==11){html = 'VEHICLE';}
                    if ( cellvalue==12){html = 'VOLTAGE';}
                    if ( cellvalue==13){html = 'INTERNAL_ID';}
                    if ( cellvalue==14){html = 'MCC';}
                    if ( cellvalue==15){html = 'MNC';}
                    if ( cellvalue==16){html = 'LAC';}
                    if ( cellvalue==17){html = 'CELLID';}
                  return html;
                }
                var winHeight=490;//Math.round(window.innerHeight*.50);

                var winWidth=Math.round(window.innerWidth*.85);
                        // Event Routines
                var listener_fields_grid_name = '#jqGridListenerFields';
                var listener_fields_grid_pager= '#listFieldsTables';

                var listener_fields_load_url='${h.url()}/admin/loadListenerFieldsAdmin?id='+rowId;
                var listener_fields_update_url='${h.url()}/admin/updateListenerFieldsAdmin';
                var listener_fields_addParams = {left: 0,width: window.innerWidth-700,top: 20,height: 190,url: listener_fields_update_url,mtype: 'GET', closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
                var listener_fields_editParams = {left: 0,width: window.innerWidth-700,top: 20,height: 200,url: listener_fields_update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                    width: "500",
                    editfunc: function (rowid) {
                    alert('The "Edit" button was clicked with rowid=' + rowid);
                    }
                };
                var listener_fields_deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: listener_fields_update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
                var listener_fields_viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: listener_fields_update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
                var listener_fields_searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: listener_fields_update_url,modal: true, };
                var listener_fields_grid = jQuery(listener_fields_grid_name);
                listener_fields_grid.jqGrid({
                url: listener_fields_load_url,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['id', '${_('Field')}', '${_('Value')}','${_('Assigned')}','${_('Multiplier')}','${_('Unit')}'],
                colModel: [
                    {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: true}},
                    {name: 'field', index: 'field', width: 25,align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                    {name: 'value', index: 'value', width: 25,align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                    {name: 'assign', index: 'assign', width: 15,align: 'right',hidden: false, editable: true, edittype: 'text', formatter:assignFmatter, editrules: {required: true}},
                    {name: 'multiplier', index: 'multiplier', width: 10,align: 'right',hidden: false, editable: true, edittype: 'text',  editrules: {required: true}},
                    {name: 'unit', index: 'value', width: 10,align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                ],
                pager: jQuery(listener_fields_grid_pager),
                rowNum: 15,
                rowList: [15, 50, 100],
                sortname: 'field',
                sortorder: "asc",
                viewrecords: true,
                width: winWidth-40,
                height: winHeight-160,

                ondblClickRow: function(rowId) {
                    var rowData = jQuery(this).getRowData(rowId);
                    $.ajax({
                        type: "GET",
                        url: '${h.url()}/admin/loadAssignFormTemplate',
                        contentType: "application/json; charset=utf-8",
                        data: { 'field':rowData['field'],'value':rowData['value'],'assigned':rowData['assign'],'multiplier':rowData['multiplier'],'unit':rowData['unit'],'row':rowData['id'] },
                        success: function(parameterdata) {
                            //Insert HTML code
                            $( "#addAssignForm" ).html(parameterdata.assignformtemplate);
                        },
                        error: function() {
                            alert("Error accessing server /admin/loadAssignFormTemplate")
                        },
                        complete: function() {
                        }
                    });


                    var winHeight=Math.round(window.innerHeight*.50);
                    var winWidth=Math.round(window.innerWidth*.56);
                    var assignDialog = $( "#addAssignForm" ).dialog({
                            autoOpen: false,
                            height: winHeight,
                            width: winWidth,
                            modal: true,
                            buttons: {
                                "${_('Update')}": function() {
                                    var row = $(this).data('rowId');
                                    var assign = $(this).data('assign');
                                    var multiplier = $('#multiplier').val();
                                    var unit = $('#unit').val();
                                    var selopt=$( "#selectedassigned" ).val();
                                    $.ajax({
                                    type: "GET",
                                    url: '${h.url()}/admin/updateListenerFields'+"?record="+rowId+"&assigment="+selopt+"&multiplier="+multiplier+"&unit="+unit,
                                    contentType: "application/json; charset=utf-8",
                                    data: { 'param':'gaugeParameters' },
                                    success: function(parameterdata) {
                                        listener_fields_grid.trigger( 'reloadGrid');
                                    },
                                    error: function() {
                                        alert("Error accessing server /admin/updateListenerFields")
                                    },
                                    complete: function() {
                                    }
                                    });
                                    assignDialog.dialog( "close" );
                                },
                                Cancel: function() {
                                    assignDialog.dialog( "close" );
                                }
                            },
                            close: function() {
                                //form[ 0 ].reset();
                                //allFields.removeClass( "ui-state-error" );
                            }
                        });

                    assignDialog.dialog( "open" );
                    },
                });
                listener_fields_grid.jqGrid('navGrid',listener_fields_grid_pager,{edit:false,add:false,del:false, search:true},
                            listener_fields_editParams,
                            listener_fields_addParams,
                            listener_fields_deleteParams,
                            listener_fields_searchParams,
                            listener_fields_viewParams)
                $("#listenerFieldsGrid01").show();
                var editFieldsDialog = $( "#listenerFieldsGrid01" ).dialog({
                    autoOpen: false,
                    height: winHeight,
                    width: winWidth,
                    modal: true,
                    close: function() {
                        listener_fields_grid.jqGrid('GridUnload');
                    }
                });
                $("#listenerFieldsGrid01").trigger( 'reloadGrid', { fromServer: true, page: 1 } );
                editFieldsDialog.data('rowId',1);
                editFieldsDialog.dialog( "open" );
            }


            function changeListenerState() {
            var grid = jQuery(grid_name);
            var rowKey = grid.getGridParam("selrow");
            if (rowKey){
                $.ajax({
                    type: "GET",
                    url: '${h.url()}/admin/updateListenerState'+"?id="+rowKey+"&user=${user}",
                    contentType: "application/json; charset=utf-8",
                    data: { 'param':'gaugeParameters' },
                    success: function(data) {
                        // data.value is the success return json. json string contains key value
                        return true;
                    },
                    error: function() {
                        alert("Error accesing /admin/updatelistenerstate")
                        return true;
                    },
                    complete: function() {
                    }
                 });
                }
            else
                alert("No rows are selected");
            }

            function changeLogListenerState() {
            var grid = jQuery(grid_name);
            var rowKey = grid.getGridParam("selrow");
            if (rowKey){
                $.ajax({
                    type: "GET",
                    url: '${h.url()}/admin/updateLogListenerState'+"?id="+rowKey+"&user=${user}",
                    contentType: "application/json; charset=utf-8",
                    data: { 'param':'gaugeParameters' },
                    success: function(data) {
                        // data.value is the success return json. json string contains key value
                        return true;
                    },
                    error: function() {
                        alert("Error accesing /admin/updatelistenerstate")
                        return true;
                    },
                    complete: function() {
                    }
                 });
                }
            else
                alert("No rows are selected");
            }

            function changeListenerUserState(id,topgrid) {

                $.ajax({
                    type: "GET",
                    url: '${h.url()}/admin/updateListenerUserState'+"?id="+id,
                    contentType: "application/json; charset=utf-8",
                    data: { 'param':'gaugeParameters' },
                    success: function(data) {
                        $(" #jqGridUser").trigger( 'reloadGrid', { fromServer: true, page: 1 } );
                        return true;
                    },
                    error: function() {
                        alert("Error accesing /admin/updatelistenerstate")
                        return true;
                    },
                    complete: function() {
                    }
                });
            }

            // STOMP
            var adminlistenerclient = Stomp.client('${h.stompServer()}');
            adminlistenerclient.debug=null;
            var listener_connect_callback = function() {
                adminlistenerclient.subscribe("/topic/adminlistener", listener_subscribe_callback);
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
            // adminlistenerclient.connect('${h.whoami()}', '${h.password()}', listener_connect_callback, listener_error_callback, '/');
            var stompUser='${h.stompUser()}';
            var stompPass='${h.stompPassword()}';
            adminlistenerclient.connect(stompUser, stompPass, listener_connect_callback, listener_error_callback, '/');
            </script>
</div>
    <!-- page start-->
    <!-- Hidden POP UP Start-->
    <div id="UserGrid" class="dialog-hidden" title="${_('Listener Fields')}">
        <table style="width:100%;overflow:auto;">
        <table id="jqGridUser" class="scroll" cellpadding="0" cellspacing="0"></table>
        <div id="UserTables" class="scroll" style="text-align:center;"></div>
        <div id="UserPTables" class="scroll" style="text-align:center;"></div>
        </table>
        <br>
    </div>
    <div id="listenerFieldsGrid01" class="dialog-hidden" title="${_('Listener Fields Mapper')}">
        <table style="width:100%;overflow:auto;">
        <table id="jqGridListenerFields" class="scroll" cellpadding="0" cellspacing="0"></table>
        <div id="listFieldsTables" class="scroll" style="text-align:center;"></div>
        <div id="listPlistenerFields" class="scroll" style="text-align:center;"></div>
        </table>
        <br>
    </div>
    <div id="addAssignForm" class="dialog-hidden" title="Field Assigment">
    </div>
    <!-- Hidden POP UP End-->
    <div id="noteContent" title="${_('Basic dialog')}">
    </div>
    <!-- JQGRID table start-->
    <table style="width:100%">
    <table id="jgGridListeners" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerListeners" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsListener" class="scroll" style="text-align:center;"></div>
    </table>
    <br>

  <!-- page end-->