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
    function buttonFmatter (cellvalue, options, rowObject) {
        return '<span class="ui-icon ui-icon-folder-open" title="click to open" onclick="clickme('+options.rowId+');"></span>';
    }

    function sendMsg(){
        alert("msg");
    }
    var grid_0 = '#jgGridSmartphones';
    var grid_0_pager= '#listPagerLog';

    var load_url='${h.url()}/api/loadSmartphones?user=${user}';
    var update_url='${h.url()}/api/updateSmartphones?user=${user}';
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

    var grid_d = new jQuery(grid_0);

    grid_d.jqGrid({
        url: load_url,
        datatype: 'json',
        mtype: 'GET',
        colNames: ["${_('Hidden')}", "${_('IMEI')}", "${_('Creation Date')}", "${_('Last Update')}", "${_('Type')}" , "${_('User')}" , "${_('Password')}","${_('App')}","${_('Hidden')}","${_('Hidden')}","${_('Uninstall')}"],
        colModel: [
            {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: true}},
            {name: 'imei',index: 'imei',width: 20,align: 'right',hidden: false,editable: true,edittype: 'text',editrules: {required: false}},
            {name: 'creation_date',index: 'creation_date', width: 14, align: 'right',hidden: false,editable: true, formatter:dateFmatter, edittype: 'text',editrules: {required: false}},
            {name: 'last_update',index: 'last_update', width: 14, align: 'right',hidden: false,editable: true, formatter:dateFmatter, edittype: 'text',editrules: {required: false}},
            {name: 'platform',index: 'platform',width: 5,align: 'right',hidden: false,editable: true,edittype: 'text',editrules: {required: false}},
            {name: 'gate_user', index: 'gate_password', width: 12,align: 'right',hidden: false, editable: true,  edittype: 'text', editrules: {required: true},search:true},
            {name: 'gate_password', index: 'gate_password', width: 12,align: 'right',hidden: false, editable: true,  edittype: 'text', editrules: {required: true},search:true},
            {name: 'gate_app', index: 'gate_app', width: 5,align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true},search:true},
            {name: 'latitude', index: 'latitude', width: 5,align: 'right',hidden: true, editable: true, edittype: 'text', editrules: {required: true},search:false},
            {name: 'longitude', index: 'longitude', width: 5,align: 'right',hidden: true, editable: true, edittype: 'text', editrules: {required: true},search:false},
            {name: 'password', index: 'password', width: 5,align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true},search:false},

        ],
        pager: jQuery(grid_0_pager),
        rowNum: 10,
        rowList: [10, 50, 100],
        sortname: 'imei',
        sortorder: "desc",
        viewrecords: true,
        autowidth: true,
        height: 250,
        ondblClickRow: function(this_row) {
            var rowData = grid_d.getRowData(this_row);
            showJobs(rowData['gate_user']);
        },
        //caption: header_container,
    });

    grid_d.jqGrid('navGrid',grid_0_pager,{edit:false,add:false,del:true, search:true},
                    editParams,
                    addParams,
                    deleteParams,
                    searchParams,
                    viewParams);
        grid_d.navButtonAdd(grid_0_pager,
                {
                    buttonicon: "ui-icon-mail-closed",
                    title: "${_('Msg')}",
                    caption: "${_('Msg')}",
                    position: "first",
                    onClickButton: function(rowId) {
                         var rowKey = grid_d.getGridParam("selrow");
                         if (rowKey){
                             var rowData = grid_d.getRowData(rowKey);
                             var currentImei=rowData['imei']
                              //$.alert("Success adding user "+rowData['imei'], { autoClose:true,type: 'success'});
                              var winHeight = 390; // Math.round(window.innerHeight * .78)
                              var winWidth = 500;// Math.round(window.innerWidth * .40)
                              var newDivMsg = $(document.createElement('div'));
                              var codeMsg =' <br>Title:<br> <input type="text" id="titulo" name="title" value=""> <br>Subtitle:<br> <input id="subtitulo" type="text" name="subtitle" value=""> <br><br> <button onclick="sendMsg2Smart('+currentImei+')">Send</button>'
                                newDivMsg.html(codeMsg);
                                var createExpWindowMsg = newDivMsg.dialog({
                                    autoOpen: false,
                                    title: "${_('Send Message')}",
                                    height: winHeight - 20,
                                    width: winWidth,
                                    modal: true,
                                    close: function () {
                                    }
                                });
                                createExpWindowMsg.dialog("open");
                         }
                        else{
                            $.alert("Select a row", { autoClose:false,});
                            }

                        },
                }
            );
    });

    $.extend($.jgrid.nav,{alerttop:1});


    $("#LogGrid").show();
    function sendMsg2Smart(imei){
        var title = $("#titulo").val();
        var subtitle = $("#subtitulo").val();
         //$.alert("sendMS:"+title+":"+subtitle, { autoClose:false,});
         $.ajax({
            type: "GET",
            url: '${h.url()}/api/sendMsg?title='+title+"&subtitle="+subtitle+"&imei="+imei,
            contentType: "application/json; charset=utf-8",
            data: { 'param':'gaugeParameters' },
            success: function(data) {

                $.alert("Success sending Message:"+data.Error, { autoClose:true,type: 'success'});

            },
            error: function() {
            $.alert("Error accessing /api/sendMsg", { autoClose:false,});
            return true;
            },
            complete: function() {

            }
         });
    }

    function showJobs(rowId){
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
        var winHeight = 390; // Math.round(window.innerHeight * .78)
        var winWidth = 1000;// Math.round(window.innerWidth * .40)

        var global_exp_load_url='${h.url()}/api/loadJobs?gate_user='+rowId;

        var grid_name_1 = 'jgGridJobsFields';
        var pager_name_1 = "jqGridPageJobsFields";
        var grid_name_by_id_1 = '#'+grid_name_1;
        var pager_name_by_id_1 = '#'+pager_name_1;
        if ($(grid_name_by_id_1).length){
            $(grid_name_by_id_1).remove();
            $(pager_name_by_id_1).remove();
        }

        var newDiv = $(document.createElement('div'));
        var code ="${_('Jobs')}"+'<table id="'+grid_name_1+'"></table> <div id="'+pager_name_1+'"> </div>'
        newDiv.html(code);

        var createExpWindow = newDiv.dialog({
            autoOpen: false,
            title: "${_('Jobs Data')}",
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
            colNames: ['Id', "${_('Job Id')}", "${_('Job Date')}", "${_('Description')}", "${_('State')}", "${_('Comment')}", "${_('Latitude')}",'Longitude'],
            colModel: [
                {name: 'id',index: 'id', align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: true}},
                {name: 'job_id', index: 'job_id', width: 12, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                {name: 'job_date', index: 'job_date', width: 12,align: 'right',hidden: false, editable: true, formatter:fieldStatusFmatter, edittype: 'text', editrules: {required: true},search:false},
                {name: 'job_description',index: 'job_description', width: 15, align: 'right', hidden: false, editable: true, edittype: 'text',editrules: {required: false}},
                {name: 'job_state', index: 'job_state', width: 10, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                {name: 'comment', index: 'comment', width: 30, align: 'right',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                {name: 'latitude', index: 'longitude', width: 10,align: 'right',hidden: true, editable: true, formatter:fieldStatusFmatter, edittype: 'text', editrules: {required: true},search:false},
                {name: 'longitude', index: 'longitude', width: 10, align: 'right',hidden: true, editable: true, edittype: 'text', editrules: {required: true}},
            ],
            viewrecords: true,
            width: 960,
            height: 200,
            rowNum: 9,
            rowList: [9, 10, 100],
            sortname: 'job_date',
            sortorder: "asc",
            pager: pager_name_by_id_1,
            ondblClickRow: function(this_row) {
                        var rowData = grid_1.getRowData(this_row);
                        showImages(rowData['job_id']);

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
       $.extend($.jgrid.nav,{alerttop:1});
        createExpWindow.dialog("open");
    }

    function showImages(jobId){
        var grid_nameResImages = '#jqGridResImagesVenus';
        var grid_pagerResImages= '#listPagerResImagesVenus';
        var update_urlResImages='${h.url()}/api/update_i?job_id='+jobId;
        var load_urlResImages  ='${h.url()}/api/load_i?&job_id='+jobId;
        var addParamsResImages = {left: 0,width: window.innerWidth-700,top: 20,height: 190,url: update_urlResImages,mtype: 'GET', closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true};
        var editParamsResImages = {left: 0,width: window.innerWidth-700,top: 20,height: 200,url: update_urlResImages,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true, width: "500",editfunc: function (rowid) {} };
        var deleteParamsResImages = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_urlResImages,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true};
        var viewParamsResImages = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_urlResImages,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true};
        var searchParamsResImages = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_urlResImages,modal: true};
        function formatImage(cellValue, options, rowObject) {
                var imageHtml = "<img src='images/" + cellValue + "' originalValue='" + cellValue + "' />";
                var imageHtml = '<img src="data:image/png;base64,'+cellValue+'" width="150" height="50" />';
                return imageHtml;
            }

        if ($(grid_nameResImages).length){
            $(grid_nameResImages).remove();
            $(grid_pagerResImages).remove();
        }

        var newImageDiv = $(document.createElement('div'));
        var imagecode ="${_('Images')}"+'<table id="'+"jqGridResImagesVenus"+'"></table> <div id="'+"listPagerResImagesVenus"+'"> </div>'
        newImageDiv.html(imagecode);
        var winHeight = 390; // Math.round(window.innerHeight * .78)
        var winWidth = 900;// Math.round(window.innerWidth * .40)
        var createImageWindow = newImageDiv.dialog({
            autoOpen: false,
            title: "${_('Image Data')}",
            height: winHeight - 20,
            width: winWidth,
            modal: true,
            close: function () {
            }
        });
        var gridResImages = jQuery(grid_nameResImages);

        gridResImages.jqGrid({
            url: load_urlResImages,
            datatype: 'json',
            mtype: 'GET',
            colNames: ['${_('ID')}', '${_('Image')}','${_('Image')}', '${_('Date')}', '${_('Extra')}','${_('ID')}'],
            colModel: [
                {name: 'id',index: 'id', align: 'center',key:true,hidden: true,width:20, editable: false,edittype: 'text',editrules: {required: true},search:false},
                {name: 'image',index: 'image', align: 'left',hidden:true ,width:200,editable: true, edittype: 'string',editrules: {required: false}},
                {name: 'image2',index: 'image2', formatter: formatImage,align: 'left',hidden:false ,width:200,editable: true, edittype: 'string',editrules: {required: false}},
                {name: 'Date', index: 'Date',align: 'left',hidden: false, editable: true, edittype: 'text', editrules: {required: true}},
                {name: 'extra',index: 'extra', align: 'left',hidden: true,width:50,editable: true, edittype: 'text',editrules: {required: true}},
                {name: 'job_id',index: 'job_id', align: 'left',hidden: true,width:50,editable: true, edittype: 'text',editrules: {required: true}},
            ],
            pager: jQuery(grid_pagerResImages),
            rowNum: 16,
            rowList: [16, 50, 100],
            sortname: 'id',
            sortorder: "asc",
            viewrecords: true,
            width: 850,
            height: 200,
            ondblClickRow: function(this_row) {
                var rowData = gridResImages.getRowData(this_row);
                showDetailImages(rowData['image']);

            }
            //caption: header_container,
        });
        gridResImages.jqGrid('navGrid',grid_pagerResImages,{edit:false,add:false,del:true,delcaption:'${_('Delete')}',deltitle:'${_('Delete')}', search:true},
                        editParamsResImages,
                        addParamsResImages,
                        deleteParamsResImages,
                        searchParamsResImages,
                        viewParamsResImages);


        $.extend($.jgrid.nav,{alerttop:1});

        createImageWindow.dialog("open");
    }
    function showDetailImages(dataimage){
        console.log(dataimage);
        var newShowImageDiv = $(document.createElement('div'));
        var imagecode ='<div><img src="data:image/png;base64, '+dataimage+'" alt="Image" /></div>';
        newShowImageDiv.html(imagecode);
        var winHeight = 1280; // Math.round(window.innerHeight * .78)
        var winWidth = 920;// Math.round(window.innerWidth * .40)
        var createShowImageWindow = newShowImageDiv.dialog({
            autoOpen: false,
            title: "${_('Detail Image')}",
            height: winHeight - 20,
            width: winWidth,
            modal: true,
            close: function () {
            }
        });
        createShowImageWindow.dialog("open");
    }
    // STOMP
    var bell = new Audio("${tg.url('/sounds/ding.mp3')}");
    var listenerclient = Stomp.client('${h.stompServer()}');
    listenerclient.debug=false;
    var listener_connect_callback = function() {
        listenerclient.subscribe("/topic/Smartphonesfrom", listener_subscribe_callback);
        // called back after the client is connected and authenticated to the STOMP server
      };
    var listener_error_callback = function(error) {
        $.alert("Error:"+error, { autoClose:false,});
        //alert(error);
    };
    var listener_subscribe_callback = function(message) {

        var msg = message.body;
        var payload = msg.split('|');
        var command = payload[0];
        var data = payload[1];
        switch (command) {
                case 'RELOAD':
                    $("#jgGridSmartphones").trigger( 'reloadGrid' );
                    $("#jgGridJobsFields").trigger( 'reloadGrid' );
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
    <table id="jgGridSmartphones" ></table>
    <div id="listPagerLog" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsLog" class="scroll" style="text-align:center;"></div>
    </table>
