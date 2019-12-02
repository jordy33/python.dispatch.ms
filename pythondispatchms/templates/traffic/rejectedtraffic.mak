

<style type="text/css">

    .ui-timepicker-div .ui-widget-header { margin-bottom: 8px; }
    .ui-timepicker-div dl { text-align: left; }
    .ui-timepicker-div dl dt { float: left; clear:left; padding: 0 0 0 5px; }
    .ui-timepicker-div dl dd { margin: 0 10px 10px 40%; }
    .ui-timepicker-div td { font-size: 90%; }
    .ui-tpicker-grid-label { background: none; border: none; margin: 0; padding: 0; }
    .ui-timepicker-div .ui_tpicker_unit_hide{ display: none; }

    .ui-timepicker-div .ui_tpicker_time .ui_tpicker_time_input { background: none; color: inherit; border: none; outline: none; border-bottom: solid 1px #555; width: 95%; }
    .ui-timepicker-div .ui_tpicker_time .ui_tpicker_time_input:focus { border-bottom-color: #aaa; }

    .ui-timepicker-rtl{ direction: rtl; }
    .ui-timepicker-rtl dl { text-align: right; padding: 0 5px 0 0; }
    .ui-timepicker-rtl dl dt{ float: right; clear: right; }
    .ui-timepicker-rtl dl dd { margin: 0 40% 10px 10px; }

    /* Shortened version style */
    .ui-timepicker-div.ui-timepicker-oneLine { padding-right: 2px; }
    .ui-timepicker-div.ui-timepicker-oneLine .ui_tpicker_time,
    .ui-timepicker-div.ui-timepicker-oneLine dt { display: none; }
    .ui-timepicker-div.ui-timepicker-oneLine .ui_tpicker_time_label { display: block; padding-top: 2px; }
    .ui-timepicker-div.ui-timepicker-oneLine dl { text-align: right; }
    .ui-timepicker-div.ui-timepicker-oneLine dl dd,
    .ui-timepicker-div.ui-timepicker-oneLine dl dd > div { display:inline-block; margin:0; }
    .ui-timepicker-div.ui-timepicker-oneLine dl dd.ui_tpicker_minute:before,
    .ui-timepicker-div.ui-timepicker-oneLine dl dd.ui_tpicker_second:before { content:':'; display:inline-block; }
    .ui-timepicker-div.ui-timepicker-oneLine dl dd.ui_tpicker_millisec:before,
    .ui-timepicker-div.ui-timepicker-oneLine dl dd.ui_tpicker_microsec:before { content:'.'; display:inline-block; }
    .ui-timepicker-div.ui-timepicker-oneLine .ui_tpicker_unit_hide,
    .ui-timepicker-div.ui-timepicker-oneLine .ui_tpicker_unit_hide:before{ display: none; }
    link { color: #0000EE; }

    .text{
        position:relative;
        left:190px;
        top:0px;
        width:290px;
        font-size:14px;
        color:black;

    }
    .imgContainer{
        float:left;
    }

    .azimuthimage {
        position: relative;
    }

    .azimuthimage .base {
       position: absolute;
       top: 0;
       left: 0;

       z-index : 0;
        width: 300px;
       height: 221px;
    }

    .azimuthimage .overlay{
       position: absolute;
       top: 55px;
       left:    81px;
       width: 105px;
       height: 105px;
    }

    div.dialog-hidden { display:none}
    div.redsquare    { border: solid 10px red; width: 67px; height: 10px; }
    div.orangesquare { border: solid 10px orange; width: 67px; height: 10px;}
    div.yellowsquare { border: solid 10px yellow; width: 67px; height: 10px;}
    div.greensquare  { border: solid 10px green; width: 67px; height: 10px; }
    div.bluesquare   { border: solid 10px blue; width: 67px; height: 10px; }
</style>
<script>
function rejectedTraffic(){
    var bell = new Audio("${tg.url('/sounds/ding.mp3')}");
    var icc='';

    function rejecteddateFmatter ( cellvalue, options, rowObject )
    {
        var utcDate=moment.utc(cellvalue,"YYYY-MM-DD h:mm:ss")
        var localDate=moment(utcDate).local();
        var formatdate = localDate.format("YYYY-MM-DD HH:mm:ss");
        html = '<center><div style="background-color:yellow" style="text-align:center">'+formatdate+'</div></center>';
        return formatdate;
    }
    function rpriorityFmatter ( cellvalue, options, rowObject )
        {
            html=cellvalue;
            if ( cellvalue==1){html = '<center><div style="background-color:red"><div style="color:white">1</div></div></center>';}
            if ( cellvalue==2){html = '<center><div style="background-color:orange" style="text-align:center">2</div></center>';}
            if ( cellvalue==3){html = '<center><div style="background-color:yellow" style="text-align:center">3</div></center>';}
            if ( cellvalue==4){html = '<center><div style="background-color:green"><div style="color:white">4</div></div></center>';}
            if ( cellvalue==5){html = '<center><div style="background-color:blue"><div style="color:white">5</div></div></center>';}
            return html;
        }

    function rstatusFmatter ( cellvalue, options, rowObject ){
        html=cellvalue;
        if ( cellvalue=="R"){html = '<center><span class="glyphicon glyphicon-warning-sign" style="color:orange"></span></center>';}


        return html;
    }

    var c5Plates=''
    var grid_name = '#jqGridRejected';
    var grid_pager= '#rejectedPagerAlerts';
    var update_url='${h.url()}/traffic/updateTraffic?group=${group}';
    var load_url  ='${h.url()}/traffic/loadrejectedTraffic?group=${group}';

    var addParams = {left: 0,width: window.innerWidth-700,top: 20,height: 190,url: update_url,mtype: 'GET', closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
    var editParams = {left: 0,width: window.innerWidth-700,top: 20,height: 200,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
            width: "500",
            editfunc: function (rowid) {
            }
        };
    var deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
    var viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
    var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url,modal: true, };
    var grid = jQuery(grid_name);

            $(document).ready(function () {

                var username = 'dispatch';
                var password = 'managepass';

                function rmake_base_auth(user, password) {
                    var tok = user + ':' + password;
                    var hash = btoa(tok);
                    return "Basic " + hash;
                }
                $.ajaxSetup({
                    beforeSend: function (xhr)
                    {
                    xhr.setRequestHeader("Content-Type","application/json");
                    xhr.setRequestHeader("Accept","application/json");
                    xhr.setRequestHeader( "Authorization", rmake_base_auth(username,password));
                    }
                });
                grid.jqGrid({
                url: load_url,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['${_('Hidden')}', '${_('Status')}', '${_('Priority')}', '${_('Client')}', '${_('Event')}', '${_('Event Description')}','${_('Vehicle')}','${_('Date')}','Hidden','Hidden','Hidden','Hidden','Hidden','Hidden','Hidden','Hidden','Hidden','Listener','User'],
                colModel: [
                    {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: true}},
                    {name: 'attended_state', index: 'attended_state', width: 5,align: 'right',hidden: false, editable: true, edittype: 'text', formatter:rstatusFmatter, editrules: {required: true},search:false},
                    {name: 'priority', index: 'priority', width: 7,align: 'right',hidden: false, editable: true, edittype: 'text', formatter:rpriorityFmatter, editrules: {required: true},search:false},
                    {name: 'user_name',index: 'user_name',width: 25,align: 'right',hidden: false,editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'event_id',index: 'event_id',width: 5,align: 'right',hidden: false,editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'event_desc',index: 'event_desc', width: 25, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'vehicle',index: 'vehicle',width: 25,align: 'right',editable: true,edittype: 'text',editrules: {required: true}},
                    {name: 'time_stamp',index: 'time_stamp', width: 14, align: 'right',hidden: false,editable: true, edittype: 'text', formatter:rejecteddateFmatter,editrules: {required: false}},
                    {name: 'attended_time',index: 'attended_time', width: 30, align: 'right',hidden: true,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'pending_time',index: 'pending_time', width: 30, align: 'right',hidden: true,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'closed_time',index: 'closed_time', width: 30, align: 'right',hidden: true,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'user_id',index: 'user_id', width: 5, align: 'right', hidden: true, editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'imei',index: 'imei', width: 5, align: 'right', hidden: true, editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'latitude',index: 'latitude',width: 5, align: 'right',hidden: true, editable: true, edittype: 'text', editrules: {required: false}},
                    {name: 'longitude',index: 'longitude',width: 5,align: 'right', hidden: true, editable: true,edittype: 'text', editrules: {required: false}},
                    {name: 'speed',index: 'speed',width: 5,align: 'right', hidden: true, editable: true,edittype: 'text', editrules: {required: false}},
                    {name: 'azimuth',index: 'azimuth',width: 5,align: 'right', hidden: true, editable: true,edittype: 'text', editrules: {required: false}},
                    {name: 'listener',index: 'listener',width: 5,align: 'right', hidden: true, editable: true,edittype: 'text', editrules: {required: false}},
                    {name: 'user',index: 'user',width: 5,align: 'right', hidden: true, editable: true,edittype: 'text', editrules: {required: false}},
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
                    rdoDoubleClick(rowId)
                },
                //caption: header_container,
            });
            grid.jqGrid('navGrid',grid_pager,{edit:false,add:false,del:false, search:true},
                            editParams,
                            addParams,
                            deleteParams,
                            searchParams,
                            viewParams);
            // add custom button
            grid.navButtonAdd(grid_pager,
                {
                    buttonicon: "ui-icon-plus",
                    title: "${_('Add')}",
                    caption: "${_('Add')}",
                    position: "first",
                    onClickButton: AddCallerEvent
                });


            });
            $.extend($.jgrid.nav,{alerttop:1});
            function rdoDoubleClick(rowId){
                var rowData = jQuery('#jqGridRejected').getRowData(rowId);
                var listenerNumber=rowData['listener'];
                var attendedState=rowData['attended_state'];

                var winHeight=Math.round(window.innerHeight*.77)
                var winWidth=Math.round(window.innerWidth*.86)
                var SplitText = "${_('Title')}"
                var $dialog = $('<div></div>') /* Dialog for Instalation Report*/
                    .html(SplitText )
                    .dialog({
                        autoOpen: false,
                        modal: true,
                        height: winHeight-50,
                        width:  winWidth-100,
                        close: function(event,ui){
                            $dialog.hide();
                            $(this).hide();
                        },
                        title: 'Installation Report:'}
                        );
                function rupdateState(rowId,state){
                    $.ajax({
                        type: "GET",
                        url: '${h.url()}/traffic/updateTrafficStatus?record='+rowId+"&group=${group}"+"&state="+state+"&comment="+$("#comment").val()+"&false_alarm="+$('#alarmcheck').is(':checked'),
                        contentType: "application/json; charset=utf-8",
                        data: { 'param':'gaugeParameters' },
                        success: function(data) {
                            // data.value is the success return json. json string contains key value
                            //{'user': 'dispatch', 'toattend_statistic': 0, 'score_statistic': 99.99450277609807, 'attended_statistic': 1, 'closed_statistic': 18190}
                            var res=$("#comment").val();
                            var st=$('#alarmcheck').is(':checked');
                            $('#jqGridRejected').trigger( 'reloadGrid' );
                            ractivateTab('eventData');
                            $('#rcommentForm')[0].reset();
                            return true;
                        },
                        error: function() {
                        //alert("#"+ckbid);
                             $.alert("Error accessing /traffic/updateTrafficStatus", { autoClose:false,});
                            return true;
                        },
                        complete: function() {
                        }
                        });
                    return true;

                }
                function PoP() {
                                var row = $(this).data('rowId');
                                var putpendigDialog = $( "#putpendingForm" ).dialog({
                                        autoOpen: false,
                                        height: winHeight-100,
                                        width: winWidth-200,
                                        modal: true,
                                        buttons: {
                                            Submit: function() { //submit
                                                function SpellChecker3(parameter) {
                                                   var isSuccess = false;
                                                   $.ajax({ url: '${h.url()}/traffic/spellChecker?text='+parameter,
                                                            data: {},
                                                            async: false,
                                                            success:
                                                                function(parameterdata) {
                                                                     if (parameterdata.error=="ok"){
                                                                                isSuccess=true
                                                                            }
                                                                            else{
                                                                                isSuccess=false;
                                                                            }
                                                   }
                                                          });
                                                    return isSuccess;
                                                }
                                                jQuery.validator.addMethod("wordCountPending", function(value, element, params){
                                                    return (SpellChecker3(value));
                                                }, "A minimum of 10 words are required");
                                                //add the custom validation method

                                                $( "#pendingForm" ).validate({
                                                                  rules: {
                                                                       pendingcomment:{required:true, wordCountPending: ['10']},
                                                                      }
                                                                });
                                                if($("#pendingForm").valid()){   // test for validity
                                                  var row = $(this).data('rowId');
                                                  rupdateState(row,"P");
                                                  $( this ).dialog( "close" );
                                                  var pc = $('#pendingcomment').val();
                                                  $.ajax({
                                                                type: "GET",
                                                                url: '${h.url()}/traffic/addPending?id='+row+"&comment="+pc+"&group=${group}",
                                                                contentType: "application/json; charset=utf-8",
                                                                data: { 'param':'gaugeParameters' },
                                                                success: function(data) {
                                                                // data.value is the success return json. json string contains key value
                                                                    $.alert("Pendiente Exitoso", { autoClose:true,type: 'success',});
                                                                    $('#pendingForm')[0].reset();
                                                                },
                                                                error: function() {
                                                                $.alert("Error accessing traffic/addPending", { autoClose:false,});
                                                                return true;
                                                                },
                                                                complete: function() {

                                                                }
                                                  });
                                                  trafficDialog.dialog( "close" );
                                                  $( this ).dialog( "close" );
                                                }
                                            },
                                            Cancel: function() { //cancel
                                                $('#pendingForm')[0].reset();
                                                $( this ).dialog( "close" );
                                            }
                                        }
                                        ,
                                        close: function() {
                                            $('#rcommentForm')[0].reset();
                                            //form[ 0 ].reset();
                                            //allFields.removeClass( "ui-state-error" );
                                        }
                                 });
                                putpendigDialog.data("rowId",row);
                                putpendigDialog.dialog( "open" );
                                //trafficDialog.dialog( "close" );
                            };
                function ractivateTab(tab){
                    $('.nav-tabs a[href="#' + tab + '"]').tab('show');
                };
                function rejectedinitMap(latitude,longitude,cell_lat,cell_lon){
                    var myLatLng = {lat: latitude, lng: longitude};
                   // var myLatLng = new google.maps.LatLng(latitude, longitude);
                    map = new google.maps.Map(document.getElementById("rmap_canvas"), {
                      zoom: 12,
                      center: myLatLng
                    });
                     var marker = new google.maps.Marker({
                              position: myLatLng,
                              map: map
                            });

                    marker.setMap(map);
                    console.log(typeof cell_lon);
                    if ( cell_lon!=0 && cell_lat!=0){
                        var CellIdLatLng = {lat: cell_lat, lng: cell_lon};
                        var marker2 = new google.maps.Marker({
                        position: CellIdLatLng,
                        map: map,
                        icon: "${h.url()}/img/yellow-dot.png"
                    });

                    }

                    google.maps.event.trigger(map, 'resize');
                    $("#rmap_canvas").css("width", Math.round(window.innerHeight*.40)).css("height", Math.round(window.innerHeight*.40));

                    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
                      var target = $(e.target).attr("href") // activated tab

                        if (target==='#rlocationMap'){
                            google.maps.event.trigger(map, 'resize');
                            map.setCenter(marker.getPosition());
                        }

                    });
                }

                var trafficDialog = $( "#retrafficForm" ).dialog({
                        autoOpen: false,
                        height: winHeight,
                        width: winWidth,
                        modal: true,
                        closeOnEscape:false,
                        close: function() {
                            //form[ 0 ].reset();
                            //allFields.removeClass( "ui-state-error" );
                        },


                    });
                var finalizeButtons = {
                            "${_('Exit')}": function() {
                                $('#rcommentForm')[0].reset();
                                finalizeDialog.dialog( "close" );
                            }
                };
                var submitFinalizeButtons = {
                            "${_('Submit')}": function() {
                            function SpellChecker(parameter) {
                               var isSuccess = false;
                               $.ajax({ url:  '${h.url()}/traffic/spellChecker?text='+parameter,
                                        data: {},
                                        async: false,
                                        success:
                                            function(parameterdata) {
                                                 if (parameterdata.error=="ok"){
                                                            isSuccess=true
                                                        }
                                                        else{
                                                            $.alert(parameterdata.error)
                                                            isSuccess=false;
                                                        }
                               }
                                      });
                                return isSuccess;
                            }
                            jQuery.validator.addMethod("wordCount", function(value, element, params){
                                return (SpellChecker(value));
                            }, "A minimum of 10 words are required");
                            //add the custom validation method
                            $( "#rcommentForm" ).validate({
                                              rules: {
                                                   comment:{required:true, wordCount: ['10']},
                                                  }
                                            });
                            if($("#rcommentForm").valid()){   // test for validity
                             var row = $(this).data('rowId');
                             rupdateState(row,'C');
                             finalizeDialog.dialog( "close" );
                             trafficDialog.dialog( "close" );
                                }
                            },
                            "${_('Exit')}": function() {
                                $('#rcommentForm')[0].reset();
                                finalizeDialog.dialog( "close" );
                                }
                            };
                var finalizeDialog = $( "#rfinalizeForm" ).dialog({
                        autoOpen: false,
                        height: winHeight-100,
                        width: winWidth-200,
                        modal: true,
                        buttons: finalizeButtons,
                        close: function() {
                            $('#rcommentForm')[0].reset();
                            //form[ 0 ].reset();
                            //allFields.removeClass( "ui-state-error" );
                        }
                 });

                $("#helpComment").change(function(){
                  var id = $(this).find("option:selected").attr("value");
                  $("#comment").val(id);
                });
                $("#helpComment2").change(function(){
                  var id = $(this).find("option:selected").attr("value");
                  $("#pendingcomment").val(id);
                });


                var rowData = jQuery('#jqGridRejected').getRowData(rowId);
                var atst=rowData['attended_state'];
                var azimuth=rowData['azimuth'];
                var degrees=parseInt(azimuth);
                var eventdescript=rowData['event_desc'];
                var vehicledescript=rowData['vehicle'];
                var eventtime=rowData['time_stamp'];
                $("#compassNeedle").rotate(degrees);
                $("#reventHeading").text(eventdescript);
                $("#vehicleDescription").text(vehicledescript);
                $("#eventTime").text(eventtime);
                $("#degreesAzimuth").html('<p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp'+degrees+String.fromCharCode(176)+'</p>');
                var urlinstall='';
                $.ajax({
                type: "GET",

                url: '${h.url()}/traffic/getRecord?record='+rowId+"&user=${user}"+"&group=${group}"+"&tz=${tz}",
                contentType: "application/json; charset=utf-8",
                data: { 'param':'gaugeParameters' },
                success: function(parameterdata) {
                    function rejecteddateFmatter ( cellvalue, options, rowObject )
                    {
                        var utcDate=moment.utc(cellvalue,"YYYY-MM-DD h:mm:ss")
                        var localDate=moment(utcDate).local();
                        var formatdate = localDate.format("YYYY-MM-DD HH:mm:ss");
                        return formatdate;
                    }
                    //Insert HTML code
                    //alert(parameterdata.vehicle);
                    $("#raccount").html(parameterdata.account);
                    $("#revent").html(parameterdata.event);
                    $("#rvehicle").html(parameterdata.vehicle);
                    $("#rcallerList").html(parameterdata.rcallerList);
                    $("#raccountHistory").html(parameterdata.accounthistory);
                    $("#comment").val(parameterdata.comment);
                    $("#alarmcheck").val(parameterdata.false_alarm);
                    $("#eventLink").html(parameterdata.platform);
                    $("#rimages").html(parameterdata.images);
                    // Render time in local
                    $('#ts').text(rejecteddateFmatter(parameterdata.ts));
                    $('#et').text(rejecteddateFmatter(parameterdata.et));
                    $('#jqGridRejected').trigger( 'reloadGrid' );
                    $("#retrafficForm").show();
                    $("#dialog").dialog();
                    c5plates=parameterdata.plates;
                    urlinstall=parameterdata.link;
                    icc=parameterdata.icc;
                    rejectedinitMap(parameterdata.latitude, parameterdata.longitude,parameterdata.cell_lat,parameterdata.cell_lon);
                    ractivateTab('raccount');
                    trafficDialog.data("rowId",rowId);
                    trafficDialog.data("state",atst);
                    trafficDialog.data("ces",parameterdata.callerEventState);
                    trafficDialog.dialog( "open" );

                },
                error: function (xhr, ajaxOptions, thrownError) {
                    if (xhr.status==503){
                        $.alert("Servicio no disponible en pluton", { autoClose:false,});
                    }
                    else{
                         $.alert(xhr.status, { autoClose:false,});
                          $.alert(thrownError, { autoClose:false,});
                    }
                  },
                complete: function() {
                    $('#button').on('click', function(e){
                        if(urlinstall!='dontHave'){
                            $dialog.dialog('open');
                            $dialog.html("<iframe width='100%' height='100%' src='"+urlinstall+"' frameborder='0' border='none'></iframe>");
                        }else{

                            $.alert("Pluton no tiene la liga");
                        }

                        });
                }
                });
            }
            function AddCallerEvent() {
                var winHeight=Math.round(window.innerHeight*.75);
                var winWidth=Math.round(window.innerWidth*.85);
                            // Event Routines
                var event_grid_name = '#jqGridRejected';

                var event_grid_pager= '#rejectedPagerTables';
                var event_update_url='${h.url()}/traffic/updateCallerEvent';
                var event_load_url='${h.url()}/traffic/loadCallerEvent/';
                var event_header_container='Evento por llamada';
                var event_addParams = {left: 0,width: window.innerWidth-700,top: 20,height: 190,url: event_update_url, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
                var event_editParams = {left: 0,width: window.innerWidth-700,top: 20,height: 200,url: event_update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                        width: "500",
                        editfunc: function (rowid) {
                        $.alert('The "Edit" button was clicked with rowid=' + rowid, { autoClose:false,});
                        }
                    };
                var event_deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: event_update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
                var event_viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: event_update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
                var event_searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: event_update_url,modal: true, };
                var event_grid = jQuery(event_grid_name);
                event_grid.jqGrid({
                    url: event_load_url,
                    datatype: 'json',
                    mtype: 'GET',
                    colNames: ['id', 'St', 'imei','ccid','Phone','L.Report','Device','Eco','Brand','Model','Year','Color','Plates','VIN','User','Password','Client ID','Server','Internal Id'],
                    colModel: [
                        {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: true}},
                        {name: 'status', index: 'status', width: 5,align: 'right',hidden: true, editable: true, edittype: 'text', editrules: {required: true}},
                        {name: 'imei', index: 'imei', width:18,align: 'right',hidden: true, editable: true, edittype: 'text', editrules: {required: true}},
                        {name: 'ccid', index: 'ccid', width: 15,align: 'right',hidden: true, editable: true, edittype: 'text', editrules: {required: true}},
                        {name: 'phone', index: 'phone', width: 10,align: 'right',hidden: true, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'last_report', index: 'last_report', width: 10,align: 'right',hidden: true, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'device', index: 'device', width: 10,align: 'right',hidden: true, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'eco', index: 'eco', width: 10,align: 'right',hidden: false, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'brand', index: 'brand', width: 10,align: 'right',hidden: false, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'model', index: 'model', width: 10,align: 'right',hidden: false, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'year', index: 'year', width: 10,align: 'right',hidden: true, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'color', index: 'color', width: 10,align: 'right',hidden: true, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'plates', index: 'plates', width: 10,align: 'right',hidden: false, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'vin', index: 'vin', width: 10,align: 'right',hidden: true, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'user', index: 'user', width: 10,align: 'right',hidden: false, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'password', index: 'password', width: 10,align: 'right',hidden: true, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'client_id', index: 'client_id', width: 10,align: 'right',hidden: true, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'server', index: 'server', width: 10,align: 'right',hidden: true, editable: true, edittype: 'text',  editrules: {required: true}},
                        {name: 'internal_id', index: 'internal_id', width: 10,align: 'right',hidden: true, editable: true, edittype: 'text',  editrules: {required: true}},

                    ],
                    pager: jQuery(event_grid_pager),
                    rowNum: 10,
                    rowList: [10, 50, 100],
                    sortname: 'id',
                    sortorder: "asc",
                    viewrecords: true,
                    width: winWidth-40,
                    height: winHeight-160,

                    ondblClickRow: function(rowId) {
                        var rowData = jQuery(this).getRowData(rowId);
                        var im=rowData['imei'];
                        var ve=rowData['brand']+rowData['model'];
                        var ci=rowData['client_id'];
                        //load form
                        $.ajax({
                        type: "GET",
                        url: '${h.url()}/traffic/getDynamicTemplate/'+"?listener="+$( "input:checked" ).val()  ,
                        contentType: "application/json; charset=utf-8",
                        data: { 'param':'gaugeParameters' },
                        success: function(parameterdata) {
                            //Insert HTML code
                            $( "#rejectedForm" ).html(parameterdata.eventtemplate);
                        },
                        error: function() {
                            $.alert("Error accessing server /alerts/getRecord", { autoClose:false,});
                        },
                        complete: function() {

                            var winHeight=Math.round(window.innerHeight*.75);
                            var winWidth=Math.round(window.innerWidth*.75);
                            var assignDialog = $( "#rejectedForm" ).dialog({
                                autoOpen: false,
                                height: winHeight,
                                width: winWidth,
                                modal: true,
                                buttons: {
                                    "${_('Crear Evento')}": function() {
                                            var sp = $('#selectedpriority').val();
                                            var ev = $('#event_id').val();
                                            var cm = $('#callercomment').val();
                                            var un ="${group}";

                                            function EventSpellChecker(parameter) {
                                               var isEventSuccess = false;
                                               $.ajax({ url: '${h.url()}/traffic/spellChecker?text='+parameter,
                                                        data: {},
                                                        async: false,
                                                        success:
                                                            function(parameterdata) {
                                                                 if (parameterdata.error=="ok"){
                                                                            isEventSuccess=true
                                                                        }
                                                                        else{
                                                                            $.alert(parameterdata.error);
                                                                            isEventSuccess=false;
                                                                        }
                                               }
                                                      });
                                                return isEventSuccess;
                                            }
                                            jQuery.validator.addMethod("EventwordCount", function(value, element, params){
                                                return (EventSpellChecker(value));
                                            }, "A minimum of 10 words are required");
                                            $( "#eventsForm" ).validate({
                                              rules: {
                                                   callercomment:{required:true,EventwordCount: ['10']},
                                                  }
                                            });

                                            if($("#eventsForm").valid()){   // test for validity
                                             $.ajax({
                                                    type: "GET",

                                                    url: '${h.url()}/traffic/addTraffic/'+"?priority="+sp+"&event_id="+ev+"&user_name="+un+"&imei="+im+"&vehicle="+ve+"&comment="+cm+"&client_id="+ci+'&group='+"${group}",
                                                    contentType: "application/json; charset=utf-8",
                                                    data: { 'param':'gaugeParameters' },
                                                    success: function(data) {
                                                    // data.value is the success return json. json string contains key value
                                                        $('#jqGridRejected').trigger( 'reloadGrid' );
                                                        rdoDoubleClick(data.id);
                                                        $('#eventsForm')[0].reset();
                                                    },
                                                    error: function() {
                                                    $.alert("Error accessing tables/addPriority", { autoClose:false,});
                                                    return true;
                                                    },
                                                    complete: function() {

                                                    }
                                                 });
                                             }

                                    },
                                    Cancel: function() {
                                        assignDialog.dialog( "close" );
                                        addCallerEventDialog.dialog( "close" );
                                    }
                                },

                                close: function() {
                                    //form[ 0 ].reset();
                                    //allFields.removeClass( "ui-state-error" );
                                }
                            });
                            assignDialog.data("rowId",rowId);

                            assignDialog.dialog( "open" );
                        }
                        });



                    },
                });
                event_grid.jqGrid('filterToolbar', {stringResult: true, searchOnEnter: false, defaultSearch : "cn"});

                event_grid.jqGrid('navGrid',event_grid_pager,{edit:false,add:false,del:false, search:true},
                                event_editParams,
                                event_addParams,
                                event_deleteParams,
                                event_searchParams,
                                event_viewParams)

                $("#rejectedEventGrid").show();
                var addCallerEventDialog = $( "#rejectedEventGrid" ).dialog({
                        autoOpen: false,
                        height: winHeight,
                        width: winWidth,
                        modal: true,
                        close: function() {
                            //$('#filter01Form')[0].reset();
                            //form[ 0 ].reset();
                            //allFields.removeClass( "ui-state-error" );
                        }
                 });

                addCallerEventDialog.data('rowId',1);
                addCallerEventDialog.dialog( "open" );
            }
            // STOMP
            var subscribe ="/topic/rejectedlistener_"+"${group}";
            var traffic_client = Stomp.client('${h.stompServer()}');
            traffic_client.debug=null;
            var traffic_connect_callback = function() {
                traffic_client.subscribe(subscribe, traffic_subscribe_callback);
                // called back after the client is connected and authenticated to the STOMP server
              };
            var traffic_error_callback = function(error) {
                 $.alert("error", { autoClose:false,});
            };
            var traffic_subscribe_callback = function(message) {

                var msg = message.body;
                var payload = msg.split('|');
                var command = payload[0];
                var data = payload[1];

                switch (command) {
                        case 'RELOAD':
                            $('#jqGridRejected').trigger( 'reloadGrid' );
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
            traffic_client.connect(stompUser, stompPass, traffic_connect_callback, traffic_error_callback, '/');
}
$( document ).ready(function() {
    rejectedTraffic();
});

            </script>
</div>
    <!-- page start-->


    <!-- Hidden POP UP start-->
     <div id="rejectedimagesForm" class="dialog-hidden" title="${_('Upload Image')}">
        <form action="${h.url()}/traffic/uploadImage" name= "imagesForm" id="imagesForm" method="POST" enctype="multipart/form-data">
        <input type="hidden" name="pagename" py:attrs="value=pagename"/>
        <label for="upload_file">${_('Filename')}:</label>
            <br>
            <p>${_('Upload Image')}:  ${_('Only')} (jpeg,bmp and png)</p>
            <br>
        <input type="file" name="file" id="file" accept="image/vnd-wap-wbmp,image/png, image/jpeg" required/>  <br/>
        <input type="submit" name="submit_upload" value="Upload"/>
        </form>
    </div>
    <div id="retrafficForm" class="dialog-hidden" title="${_('Traffic')}">
        <ul class="nav nav-tabs">
          <li><a data-toggle="tab" href="#raccount" >${_('Account')}</a></li>
          <li><a data-toggle="tab" href="#revent" >${_('Event')}</a></li>
          <li><a data-toggle="tab" href="#rvehicle" >${_('Vehicle')}</a></li>
          <li><a data-toggle="tab" href="#rcallerList" >${_('Caller List')}</a></li>
          <li><a data-toggle="tab" href="#raccountHistory">${_('Account History')}</a></li>
          <li><a data-toggle="tab" href="#rimages">${_('Images')}</a></li>
          <li><a data-toggle="tab" href="#rinstallationReport">${_('Installation Report')}</a></li>
          <li><a data-toggle="tab" href="#rlocationMap" data-toggle="tab">${_('Map')}</a></li>
        </ul>

        <div class="tab-content">
          <div id="raccount" class="tab-pane fade in active">
          </div>
          <div id="revent" class="tab-pane fade in active">
          </div>
          <div id="rvehicle" class="tab-pane fade in active">
          </div>
          <div id="rcallerList" class="tab-pane fade">
          </div>
          <div id="raccountHistory" class="tab-pane fade">
          </div>
          <div id="rimages" class="tab-pane fade">


          </div>
          <div id="rinstallationReport" class="tab-pane fade">
              <br>
              <button id="button" type="button" class="btn btn-default" data-toggle="button">${_('Print')}</button>
          </div>


          <div id="rlocationMap" class="tab-pane fade">

              <br>

              <h4 id="reventHeading">${_('Event')}</h4>
              <div class="image123">
                    <div class="imgContainer">
                        <div id="rmap_canvas"></div>
                    </div>

                    <div class="imgContainer">
                        <div class="azimuthimage">
                           <img src="${h.url()}/img/noneedlecompass.png" class="base"/>
                           <img src="${h.url()}/img/needle.png" id="compassNeedle" class="overlay" style="z-index: 1" />
                        </div>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <p id="degreesAzimuth">${_('Degress')}</p>
                    </div>
                    <div class="imgContainer">
                        <span class="text" id="vehicleDescription">${_('Vehicle')}</span></div><br>
                        <span class="text" id="eventTime">${_('Event Time')}</span></div>
                        <span class="text" id="eventLink">${_('Link')}</span></div>
                    </div>

              </div>
          </div>
        </div>
    </div>
    <div id="rfinalizeForm" class="dialog-hidden" title="${_('Finalize')}">
      <form id="rcommentForm">
        <fieldset>
            <select id="helpComment" name="helpComment">
                % for item in list:
                    <option id="${item['id']}" value="${item['hcomment']}">${item['hcomment']}</option>
                % endfor
            </select>
            <br>
            <label for="comment">${_('Comment')}:</label>
            <textarea class="form-control" rows="8" id="comment" name="comment" required onpaste="return false;" onCopy="return false" onCut="return false"></textarea>
            <div class="checkbox">
              <label><input type="checkbox" id="alarmcheck" value="">${_('False Alarm')}</label>
            </div>
        </fieldset>
      </form>
    </div>
    <div id="putpendingForm" class="dialog-hidden" title="${_('Pending Comment')}">
      <form id="pendingForm">
        <fieldset>
            <select id="helpComment2" name="helpComment">
                % for item in list:
                    <option id="${item['id']}" value="${item['hcomment']}">${item['hcomment']}</option>
                % endfor
            </select>
            <br>
            <label for="pendingcomment">${_('Comment')}:</label>
            <textarea class="form-control" rows="7" id="pendingcomment" name="pendingcomment" required onpaste="return false;" onCopy="return false" onCut="return false"></textarea>
        </fieldset>
      </form>
    </div>
    <div id="createTicketForm" class="dialog-hidden" title="${_('Create Ticket')}">
      <form id="ticketForm">
        <fieldset>
            <label for="ticket">${_('Comment')}:</label>
            <textarea class="form-control" rows="12" id="ticket" name="ticket" required onpaste="return false;" onCopy="return false" onCut="return false"></textarea>
            <br>
            <!-- <label for="lastReport">${_('Last Report')}:</label>
            <input type="text" name="lastReport" id="lastReport" value="" required> End-->
        </fieldset>
      </form>
    </div>
    <div id="createC5Form" class="dialog-hidden" title="${_('Datos para enviar al C5')}">
        <h3>Campos:</h3>
        <dl class="dl-horizontal">
            <dt>Vehiculo:</dt>
            <dd id="C5Vehicle"></dd>
            <dt>IMEI:</dt>
            <dd id="C5Imei"></dd>
            <dt>Placas:</dt>
            <dd id="C5Plates"></dd>
            <dt>Latitud:</dt>
            <dd id="C5Latitude"></dd>
            <dt>Longitud:</dt>
            <dd id="C5Longitude"></dd>
            <dt>Velocidad:</dt>
            <dd id="C5Speed"></dd>
            <dt>Direccion:</dt>
            <dd id="C5Heading"></dd>
            <dt>Valido:</dt>
            <dd>1</dd>
            <dt>Estado:</dt>
            <dd>1</dd>
        </dl>
    </div>
    <!-- Hidden POP UP End-->
<div id="noteContent" title="${_('Basic dialog')}">
</div>
    <!-- JQGRID table start-->
    <table style="width:100%">
    <table id="jqGridRejected" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="rejectedPagerAlerts" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcols" class="scroll" style="text-align:center;"></div>
    </table>
    <br>
    <!-- Gauge Meters-->
    <div class="row">
      <div class="col-lg-3">
          <section class="panel">
              <div class="panel-body"><div id="attendedGauge" class="30x30px"></div></div>
          </section>
      </div>
      <div class="col-lg-3">
          <section class="panel">
              <div class="panel-body"><div id="toAttendGauge" class="30x30px"></div></div>
          </section>
      </div>
      <div class="col-lg-3">
          <section class="panel">
              <div class="panel-body"><div id="closedGauge" class="30x30px"></div></div>
          </section>
      </div>
      <div class="col-lg-3">
          <section class="panel">
              <div class="panel-body"><div id="scoreGauge" class="30x30px"></div></div>
          </section>
      </div>
    </div>
  <!-- page end-->