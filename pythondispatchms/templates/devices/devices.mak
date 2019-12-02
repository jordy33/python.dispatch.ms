
<style type="text/css">

</style>
<script>
    function statusFmatter2 ( cellvalue, options, rowObject ){
        html=cellvalue;
        if ( cellvalue==0){html = '<center><span class="glyphicon glyphicon-remove" style="color:red"></span></center>';}
        if ( cellvalue==1){html = '<center><span class="glyphicon glyphicon-arrow-up" style="color:green"></span></center>';}
        if ( cellvalue==3){html = '<center><span class="glyphicon glyphicon-arrow-down" style="color:red"></span></center>';}
        return html;
    }

    $(document).ready(function () {


    function dateFmatter ( cellvalue, options, rowObject )
    {
        var utcDate=moment.utc(cellvalue,"YYYY-MM-DD h:mm:ss")
        var localDate=moment(utcDate).local();
        var formatdate = localDate.format("YYYY-MM-DD HH:mm:ss");
        return formatdate;
    }

    var grid_0 = '#jgGridLog';
    var grid_0_pager= '#listPagerLog';

    var load_url='${h.url()}/log/loadLog';
    var update_url='${h.url()}/log/updateLog';
    //var header_container='${_('Alerts')}';
    var addParams = {left: 0,width: window.innerWidth-700,top: 20,height: 190,url: update_url, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
    var editParams = {left: 0,width: window.innerWidth-700,top: 20,height: 200,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
            width: "500",
            editfunc: function (rowid) {
            }
        };
    var deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
    var viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
    var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url,modal: true, };
    var grid = jQuery(grid_0);
        grid.jqGrid({
        url: load_url,
        datatype: 'json',
        mtype: 'GET',
        colNames: ["${_('Hidden')}", "${_('Time Stamp')}", "${_('Listener ID')}", "${_('Mapper State')}", "${_('IMEI')}"],
        colModel: [
            {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: true}},
            {name: 'time_stamp',index: 'time_stamp', width: 14, align: 'right',hidden: false,editable: true, formatter:dateFmatter, edittype: 'text',editrules: {required: false}},
            {name: 'listener_id',index: 'listener_id',width: 25,align: 'right',hidden: false,editable: true,edittype: 'text',editrules: {required: false}},
            {name: 'mapper_state', index: 'mapper_state', width: 2,align: 'right',hidden: false, editable: true, formatter:statusFmatter2, edittype: 'text', editrules: {required: true},search:false},
            {name: 'imei',index: 'imei',width: 25,align: 'right',hidden: false,editable: true,edittype: 'text',editrules: {required: false}},
        ],
        pager: jQuery(grid_0_pager),
        rowNum: 10,
        rowList: [10, 50, 100],
        sortname: 'time_stamp',
        sortorder: "desc",
        viewrecords: true,
        autowidth: true,
        height: 250,
        ondblClickRow: function(this_row) {
            var rowData = grid.getRowData(this_row);
            showFieldsUsers(rowData['id']);
        },
        //caption: header_container,
    });
    grid.jqGrid('navGrid',grid_0_pager,{edit:false,add:false,del:true, search:true},
                    editParams,
                    addParams,
                    deleteParams,
                    searchParams,
                    viewParams);

    });
    $.extend($.jgrid.nav,{alerttop:1});
    function showFieldsUsers(rowId){
        function fieldStatusFmatter ( cellvalue, options, rowObject ){
            html=cellvalue;
            if ( cellvalue=="0"){html = '<center><span class="glyphicon glyphicon-remove" style="color:red"></span></center>';}
            if ( cellvalue=="1"){html = '<center><span class="glyphicon glyphicon-ok" style="color:green"></span></center>';}
            return html;
        }
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
        var winWidth = 1000;// Math.round(window.innerWidth * .40)

        var global_exp_load_url='${h.url()}/log/loadLogFields?id='+rowId;


        var grid_name_1 = 'jgGridLogFields';
        var pager_name_1 = "jqGridPageLogFields";
        var grid_name_by_id_1 = '#'+grid_name_1;
        var pager_name_by_id_1 = '#'+pager_name_1;
        if ($(grid_name_by_id_1).length){
            $(grid_name_by_id_1).remove();
            $(pager_name_by_id_1).remove();
        }


        var trigger_user_load_url='${h.url()}/log/loadLogUsers?id='+rowId;

        var grid_name_2 = 'jgGridLogUsers';
        var pager_name_2 = "jqGridPagerLogUsers";
        var grid_name_by_id_2 = '#'+grid_name_2;
        var pager_name_by_id_2 = '#'+pager_name_2;
        if ($(grid_name_by_id_2).length){
            $(grid_name_by_id_2).remove();
            $(pager_name_by_id_2).remove();
        }

        var newDiv = $(document.createElement('div'));
        var code ="${_('Fields')}"+'<table id="'+grid_name_1+'"></table> <div id="'+pager_name_1+'"> </div>'+'<br> <div>'+"${_('Active Users')}"+'</div> <br>'+
            '<table id="'+grid_name_2+'"></table> <div id="'+pager_name_2+'"> </div>'
        newDiv.html(code);

        var createExpWindow = newDiv.dialog({
            autoOpen: false,
            title: "${_('Log Data')}",
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
            colNames: ['Id', "${_('Field')}", "${_('Is Field Found?')}", "${_('Assigned to')}", "${_('Request Value')}", "${_('Expression')}", "${_('Exp State')}",''],
            colModel: [
                {name: 'id',index: 'id', align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: true}},
                {name: 'field', index: 'field', width: 10, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                {name: 'isfieldfound', index: 'isfieldfound', width: 10,align: 'right',hidden: false, editable: true, formatter:fieldStatusFmatter, edittype: 'text', editrules: {required: true},search:false},
                {name: 'assigned_to',index: 'assigned_to', width: 5, align: 'right', hidden: false, editable: true, edittype: 'text',editrules: {required: false}},
                {name: 'value', index: 'value', width: 10, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                {name: 'expression', index: 'expression', width: 30, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                {name: 'expression_state', index: 'expression_state', width: 10,align: 'right',hidden: false, editable: true, formatter:fieldStatusFmatter, edittype: 'text', editrules: {required: true},search:false},
                {name: 'received', index: 'received', width: 10, align: 'right',hidden: true, editable: true, edittype: 'text', editrules: {required: true}},
            ],
            viewrecords: true,
            width: 960,
            height: 200,
            rowNum: 9,
            rowList: [9, 10, 100],
            sortname: 'field',
            sortorder: "asc",
            pager: pager_name_by_id_1,
            ondblClickRow: function(this_row) {
                        var rowData = grid_1.getRowData(this_row);
                        alert(rowData['received']);

            },

        });
        grid_1.navGrid(pager_name_by_id_1, {
            search: true,
            add: false,
            edit: false,
            del: false,
            refresh: true
        }, {}, {}, {}, {},{});
        //edit,add,delete,search,view

        // Second Window
            var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: global_exp_load_url,modal: true, };
        var grid_2 = new jQuery(grid_name_by_id_2);
        grid_2.jqGrid({
            url: trigger_user_load_url,
            mtype: "GET",
            datatype: "json",
            page: 1,
            colNames: ['Id', "${_('User Name')}","${_('Trigger Exp')}","${_('State')}","${_('Filter Exp')}","${_('State')}"],
            colModel: [
                {name: 'id',index: 'id', align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: true}},
                {name: 'user_name', index: 'expression', width: 15, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                {name: 'trigger_expr', index: 'trigger_expr', width: 45, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                {name: 'trigger_expr_state', index: 'trigger_expr_state', formatter:fieldStatusFmatter, width: 5, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                {name: 'filter_expr', index: 'filter_expr', width: 45, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                {name: 'filter_expr_state', index: 'filter_expr_state', formatter:fieldStatusFmatter, width: 5, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
            ],
            viewrecords: true,
            width: 960,
            height: 200,
            rowNum: 9,
            rowList: [9, 10, 100],
            sortname: 'user_name',
            sortorder: "asc",
            pager: pager_name_by_id_2,
            ondblClickRow: function (this_row) {
            },

        });
        grid_2.navGrid(pager_name_by_id_2, {
            search: true,
            add: false,
            edit: false,
            del: false,
            refresh: true
        }, {}, {}, {}, searchParams);


        createExpWindow.dialog("open");
    }


        $("#LogGrid").show();
    // STOMP
    var bell = new Audio("${tg.url('/sounds/ding.mp3')}");
    var listenerclient = Stomp.client('${h.stompServer()}');
    listenerclient.debug=null;
    var listener_connect_callback = function() {
        listenerclient.subscribe("/topic/logListener", listener_subscribe_callback);
        // called back after the client is connected and authenticated to the STOMP server
      };
    var listener_error_callback = function(error) {
        alert(error);
    };
    var listener_subscribe_callback = function(message) {

        var msg = message.body;
        var payload = msg.split('|');
        var command = payload[0];
        var data = payload[1];
        switch (command) {
                case 'RELOAD':
                    $("#jgGridLog").trigger( 'reloadGrid' );
                    $("#jgGridLogFields").trigger( 'reloadGrid' );
                    $("#jgGridLogUsers").trigger( 'reloadGrid' );
                    break;
                case 'NEW':
                    $("#jgGridLog").trigger( 'reloadGrid' );
                    $("#jgGridLogFields").trigger( 'reloadGrid' );
                    $("#jgGridLogUsers").trigger( 'reloadGrid' );
                    $.alert("${_('Log has been trigger')}", { autoClose:true,type: 'success',});
                    bell.play();
                    break;
                case 'MSG':
                    $.alert(data, { autoClose:false,type: 'success',});
                    bell.play();
                    break;
        }
      };
    var stompUser='${h.stompUser()}';
    var stompPass='${h.stompPassword()}';
    listenerclient.connect(stompUser, stompPass, listener_connect_callback, listener_error_callback, '/');

</script>

    <!-- page start-->
    <!-- Hidden POP UP Start-->

    <!-- Hidden POP UP End-->
    <table id="jgGridLog" ></table>
    <div id="listPagerLog" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsLog" class="scroll" style="text-align:center;"></div>
    </table>
