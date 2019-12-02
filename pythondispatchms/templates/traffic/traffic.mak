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
function trafficSegment(){
var ding = new Audio("${tg.url('/sounds/ding.mp3')}");
var bell = new Audio("${tg.url('/sounds/bell.mp3')}");
var buzzer = new Audio("${tg.url('/sounds/buzzer.mp3')}");
var claxon = new Audio("${tg.url('/sounds/claxon.mp3')}");
var alarm = new Audio("${tg.url('/sounds/alarm.mp3')}");
var icc='';
var attendedGage= new JustGage({
    id: "attendedGauge",
    value: ${attended_statistic},
    min: 0,
    max: 100,
    title: "${_('Attended')}"
});
var toAttendGage = new JustGage({
    id: "toAttendGauge",
    value: ${toattend_statistic},
    min: 0,
    max: 100,
    title: "${_('To Attend')}"
});
var closedGage = new JustGage({
    id: "closedGauge",
    value: ${closed_statistic},
    min: 0,
    max: 100,
    title: "${_('Closed')}"
});
var scoreGage = new JustGage({
    id: "scoreGauge",
    value: ${score_statistic},
    min: 0,
    max: 100,
    levelColors : [ 	"#FF0000","#c18c05", "#98C105" ],
    title: "${_('Score')}"
});
function dateFmatter ( cellvalue, options, rowObject )
{
    var utcDate=moment.utc(cellvalue,"YYYY-MM-DD h:mm:ss")
    var localDate=moment(utcDate).local();
    var formatdate = localDate.format("YYYY-MM-DD HH:mm:ss");
    return formatdate;
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
function statusFmatter ( cellvalue, options, rowObject ){
    html=cellvalue;
    if ( cellvalue=="A"){html = '<center><span class="glyphicon glyphicon-search" style="color:blue"></span></center>';}
    if ( cellvalue=="N"){html = '<center><span class="glyphicon glyphicon-remove" style="color:red"></span></center>';}
    if ( cellvalue=="C"){html = '<center><span class="glyphicon glyphicon-ok" style="color:green"></span></center>';}
    if ( cellvalue=="P"){html = '<center><span class="glyphicon glyphicon-time" style="color:sandybrown"></span></center>';}
    return html;
}

var c5Plates=''
var image_counter=0;
var grid_name = '#jqGridAlerts';
var grid_pager= '#listPagerAlerts';
var update_url='${h.url()}/traffic/updateTraffic?group=${group}';
var load_url  ='${h.url()}/traffic/loadTraffic?group=${group}';

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
            grid.jqGrid({
            url: load_url,
            datatype: 'json',
            mtype: 'GET',
            colNames: ['${_('Hidden')}', '${_('Status')}', '${_('Priority')}', '${_('Client')}', '${_('Event')}', '${_('Event Description')}','${_('Vehicle')}','${_('Date')}','Hidden','Hidden','Hidden','Hidden','Hidden','Hidden','Hidden','Hidden','Hidden','Listener','User'],
            colModel: [
                {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: true}},
                {name: 'attended_state', index: 'attended_state', width: 5,align: 'right',hidden: false, editable: true, edittype: 'text', formatter:statusFmatter, editrules: {required: true},search:false},
                {name: 'priority', index: 'priority', width: 7,align: 'right',hidden: false, editable: true, edittype: 'text', formatter:priorityFmatter, editrules: {required: true},search:false},
                {name: 'user_name',index: 'user_name',width: 25,align: 'right',hidden: false,editable: true,edittype: 'text',editrules: {required: false}},
                {name: 'event_id',index: 'event_id',width: 5,align: 'right',hidden: false,editable: true,edittype: 'text',editrules: {required: false}},
                {name: 'event_desc',index: 'event_desc', width: 25, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                {name: 'vehicle',index: 'vehicle',width: 25,align: 'right',editable: true,edittype: 'text',editrules: {required: true}},
                {name: 'time_stamp',index: 'time_stamp', width: 14, align: 'right',hidden: false,editable: true, edittype: 'text', formatter:dateFmatter,editrules: {required: false}},
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
                $.ajax({
                            type: "GET",
                            url: '${h.url()}/traffic/checkTraffic?traffic_id='+rowId+"&user=${user}"+"&group=${group}",
                            contentType: "application/json; charset=utf-8",
                            data: { 'icc':icc },
                            success: function(data) {


                                if (data.status==0){
                                    doDoubleClick(rowId)
                                }
                                if (data.status==1){
                                    doDoubleClick(rowId)
                                }
                                if (data.status==2){
                                    $.alert("No esta autorizado para abrir el dedicado", { autoClose:false,});
                                }

                            },
                            error: function() {
                            $.alert("Error accediendo operators log", { autoClose:false,});
                            return true;
                            },
                            complete: function() {

                            }
                        });
                //doDoubleClick(rowId)
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
        function doDoubleClick(rowId){
            var rowData = jQuery('#jqGridAlerts').getRowData(rowId);
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
            function updateState(rowId,state){
                $.ajax({
                    type: "GET",
                    url: '${h.url()}/traffic/updateTrafficStatus?traffic_id='+rowId+"&user=${user}"+"&group=${group}"+"&state="+state+"&comment="+$("#comment").val()+"&false_alarm="+$('#alarmcheck').is(':checked'),
                    contentType: "application/json; charset=utf-8",
                    data: { 'param':'gaugeParameters' },
                    success: function(data) {
                        // data.value is the success return json. json string contains key value
                        //{'user': 'dispatch', 'toattend_statistic': 0, 'score_statistic': 99.99450277609807, 'attended_statistic': 1, 'closed_statistic': 18190}
                        attendedGage.refresh(data.attended_statistic);
                        toAttendGage.refresh(data.toattend_statistic);
                        closedGage.refresh(data.closed_statistic);
                        scoreGage.refresh(data.score_statistic);
                        var res=$("#comment").val();
                        var st=$('#alarmcheck').is(':checked');
                        $('#jqGridAlerts').trigger( 'reloadGrid' );
                        activateTab('eventData');
                        $('#commentForm')[0].reset();
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
                                              updateState(row,"P");
                                              $( this ).dialog( "close" );
                                              var pc = $('#pendingcomment').val();
                                              $.ajax({
                                                            type: "GET",
                                                            url: '${h.url()}/traffic/addPending?traffic_id='+row+"&user=${user}"+"&group=${group}"+"&comment="+pc,
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
                                        $('#commentForm')[0].reset();
                                        //form[ 0 ].reset();
                                        //allFields.removeClass( "ui-state-error" );
                                    }
                             });
                            putpendigDialog.data("rowId",row);
                            putpendigDialog.dialog( "open" );
                            //trafficDialog.dialog( "close" );
                        };
            function activateTab(tab){
                $('.nav-tabs a[href="#' + tab + '"]').tab('show');
            };
            function initMap(latitude,longitude,cell_lat,cell_lon){
                var myLatLng = {lat: latitude, lng: longitude};
               // var myLatLng = new google.maps.LatLng(latitude, longitude);
                map = new google.maps.Map(document.getElementById("map_canvas"), {
                  zoom: 12,
                  center: myLatLng
                });
                 var marker = new google.maps.Marker({
                          position: myLatLng,
                          map: map
                        });

                marker.setMap(map);

                if ( cell_lon!=0 && cell_lat!=0){
                    var CellIdLatLng = {lat: cell_lat, lng: cell_lon};
                    var marker2 = new google.maps.Marker({
                    position: CellIdLatLng,
                    map: map,
                    icon: "${h.url()}/img/yellow-dot.png"
                });

                }

                google.maps.event.trigger(map, 'resize');
                $("#map_canvas").css("width", Math.round(window.innerHeight*.40)).css("height", Math.round(window.innerHeight*.40));

                $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
                  var target = $(e.target).attr("href") // activated tab

                    if (target==='#locationMap'){
                        google.maps.event.trigger(map, 'resize');
                        map.setCenter(marker.getPosition());
                    }

                });
            }
            var buttons = {
            };
            buttons["${_('Bitácora')}"]=  function() {
                $.ajax({
                            type: "GET",
                            url: '${h.url()}/traffic/getOperatorLog?traffic_id='+rowId+"&user=${user}"+"&group=${group}"+"&tz=${tz}",
                            contentType: "application/json; charset=utf-8",
                            data: { 'icc':icc },
                            success: function(data) {
                                var array=data.operatorlog;
                                var winHeight = 400; //Math.round(window.innerHeight * .50)
                                var winWidth = 810;//Math.round(window.innerWidth * .50)
                                var newDiv = $(document.createElement('div'));
                                html='<br>' +
                                    '<h5>Listado de Operaciones</h5>' +
                                    '<ul>'
                                for(var i = 0; i < array.length; i++){
                                      html=html+'<li>'+array[i]+'</li>';    //no .value here
                                   }

                                html=html+'</ul>'
                                newDiv.html(html);
                                var createUsersSticky = newDiv.dialog({
                                                    autoOpen: false,
                                                    title: "Bitácora",
                                                    height: winHeight - 20,
                                                    width: winWidth,
                                                    modal: true,
                                                    close: function () {
                                                    }
                                                });

                                createUsersSticky.dialog("open");
                                //alert(data.operatorlog);
                            },
                            error: function() {
                            $.alert("Error accediendo operators log", { autoClose:false,});
                            return true;
                            },
                            complete: function() {

                            }
                        });

            }
            buttons["${_('Posicion Telefonica')}"]=  function() {
                $.ajax({
                            type: "GET",
                            url: '${h.url()}/traffic/getTelefonicaPosition?traffic_id='+rowId+"&user=${user}"+"&group=${group}",
                            contentType: "application/json; charset=utf-8",
                            data: { 'icc':icc },
                            success: function(data) {
                                if (data.error=="ok"){
                                     $.alert("Punto Agregado:"+data.latitude+","+data.longitude, { autoClose:true,type: 'success',});
                                     console.log(typeof data.latitude)
                                    var HomeLatLng = {lat: data.latitude, lng: data.longitude};
                                    var marker3 = new google.maps.Marker({
                                        position: HomeLatLng,
                                        map: map,
                                        icon: "${h.url()}/img/blue-dot.png"
                                    });
                                }
                                else {
                                    $.alert("Error:"+data.error, { autoClose:false,});
                                }

                            },
                            error: function() {
                            $.alert("Error accediendo telefonica posicion", { autoClose:false,});
                            return true;
                            },
                            complete: function() {

                            }
                        });

            }
            buttons["${_('Posicion Plataforma')}"]=  function() {
                image_counter=image_counter+1;
                if (image_counter>10){
                     $.alert("Error: Mas de diez puntos", { autoClose:false,});
                }
                else
                {
                var imagename = image_counter.toString();
                $.ajax({
                            type: "GET",
                            url: '${h.url()}/traffic/getPlataformPosition?traffic_id='+rowId+"&user=${user}"+"&group=${group}",
                            contentType: "application/json; charset=utf-8",
                            data: { 'icc':icc },
                            success: function(data) {
                                if (data.error=="ok"){
                                     $.alert("Punto Agregado:"+data.latitude+","+data.longitude, { autoClose:true,type: 'success',});
                                     console.log(typeof data.latitude)
                                    var HomeLatLng = {lat: data.latitude, lng: data.longitude};
                                    var marker3 = new google.maps.Marker({
                                        position: HomeLatLng,
                                        map: map,
                                        icon: "${h.url()}/img/"+imagename+".png"
                                    });
                                }
                                else {
                                    $.alert("Error:"+data.error, { autoClose:false,});
                                }

                            },
                            error: function() {
                            $.alert("Error accediendo telefonica posicion", { autoClose:false,});
                            return true;
                            },
                            complete: function() {

                            }
                        });


                }
            }
            buttons["${_('Alarma C5')}"]=  function() {
                        var rowData = jQuery('#jqGridAlerts').getRowData(rowId);
                        var c5_vehicle=rowData['vehicle'];
                        var c5_imei=rowData['imei'];
                        var c5_latitude=rowData['latitude'];
                        var c5_longitude=rowData['longitude'];
                        var c5_speed=rowData['speed'];
                        var c5_heading=rowData['azimuth'];
                        var c5_plates=c5plates;

                        $('#C5Vehicle').text(c5_vehicle);
                        $('#C5Imei').text(c5_imei);
                        $('#C5Plates').text(c5_plates);
                        $('#C5Latitude').text(c5_latitude);
                        $('#C5Longitude').text(c5_longitude);
                        $('#C5Speed').text(c5_speed);
                        $('#C5Heading').text(c5_heading);

                        var createC5Dialog = $( "#createC5Form" ).dialog({
                                autoOpen: false,
                                height: winHeight-20,
                                width: winWidth,
                                modal: true,
                                buttons: {
                                    Cancel: function() {
                                    createC5Dialog.dialog( "close" );
                                    },
                                    "${_('Enviar Alerta')}": function() {
                                        if (confirm('Esta seguro de enviar la alerta al C5 ?')) {
                                            $.ajax({
                                                type: "GET",
                                                url: '${h.url()}/traffic/send2C5?traffic_id='+rowId+"&user=${user}"+"&group=${group}"+"&vehicle="+c5_vehicle+"&imei="+c5_imei+"&plates="+c5_plates+"&latitude="+c5_latitude+"&longitude="+c5_longitude+"&speed="+c5_speed+"&heading="+c5_heading,
                                                contentType: "application/json; charset=utf-8",
                                                data: { 'param':'gaugeParameters' },
                                                success: function(data) {
                                                    $.alert("Ticket de Respuesta:"+data.Ticket, { autoClose:false,type: 'success'});
                                                    $('#ticketForm')[0].reset();
                                                },
                                                error: function() {
                                                $.alert("Error accediendo alerta/enviar al c5", { autoClose:false,});
                                                return true;
                                                },
                                                complete: function() {

                                                }
                                             });
                                        } else {
                                            // Do nothing!
                                        }

                                        createC5Dialog.dialog( "close" );
                                    }
                                },

                                close: function() {
                                    //form[ 0 ].reset();
                                    //allFields.removeClass( "ui-state-error" );
                                }
                        });
                        createC5Dialog.data("rowId",rowId);
                        createC5Dialog.data("state",atst);
                        createC5Dialog.dialog( "open" );
                        //trafficDialog.dialog( "close" );
                    };
            buttons["${_('Add Image')}"]=  function() {
                            var rowData = jQuery('#jqGridAlerts').getRowData(rowId);
                            var traffic_id=rowData['id'];
                            var addGlobalExpButtons = {
                                    "${_('Add')}": function() {
                                        var input = document.querySelector('input[type=file]')
                                        var currentUser="${user}";
                                        var currentGroup="${group}"
                                        file = input.files[0];
                                        var formData = new FormData();
                                        formData.append("userfile", file);
                                        formData.append("traffic_id", traffic_id);
                                        formData.append("user", currentUser);
                                        formData.append("group", currentGroup);
                                        var request = new XMLHttpRequest();
                                        request.open("POST", '${h.url()}/traffic/uploadImage');
                                        request.send(formData);
                                        createExpWindow.dialog( "close" );
                                        trafficDialog.dialog( "close" );
                                    },
                                    "${_('Close')}": function() {
                                        $('#jgGridMS03Trackers').trigger( 'reloadGrid' );
                                        createExpWindow.dialog( "close" );
                                    }
                            };
                            var winHeight=250;
                            var winWidth=500;
                            if ($("#MS03UsesrForm").length){
                                $("#MS03UsesrForm").remove();
                            }

                            var createExpWindow = $("#addImageForm").dialog({
                                autoOpen: false,
                                title: "CSV Upload",
                                height: winHeight - 20,
                                width: winWidth,
                                modal: true,
                                buttons: addGlobalExpButtons,
                                close: function () {
                                },

                            });
                        createExpWindow.dialog("open");
                        };

            buttons["${_('Put on Pending')}"]=  PoP;


            //if(listenerNumber==4) {
            buttons["${_('Create Ticket')}"]=  function() {
                            var row = $(this).data('rowId');
                            $('#lastReport').datetimepicker({
                                dateFormat: 'yy/mm/dd',
                            timeFormat: "hh:mm:ss"});
                            var createTicketDialog = $( "#createTicketForm" ).dialog({
                                    autoOpen: false,
                                    height: winHeight-20,
                                    width: winWidth,
                                    modal: true,
                                    buttons: {
                                        Cancel: function() {
                                        createTicketDialog.dialog( "close" );
                                        },
                                        "${_('Create Ticket')}": function() {
                                                function SpellChecker2(parameter) {
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
                                                jQuery.validator.addMethod("wordCount2", function(value, element, params){
                                                    return (SpellChecker2(value));
                                                }, "A minimum of 10 words are required");
                                                //add the custom validation method

                                                $( "#ticketForm" ).validate({
                                                  rules: {
                                                       ticket:{required:true,
                                                           wordCount2: ['10']
                                                       },
                                                      }
                                                });

                                                if($("#ticketForm").valid()) {
                                                    var rowData = jQuery('#jqGridAlerts').getRowData(rowId);
                                                    var recordId=rowData['id'];
                                                    var ticketComment = $('#ticket').val();
                                                    var lastReport=$('#lastReport').val();
                                                    $.ajax({
                                                            type: "GET",
                                                            url: '${h.url()}/traffic/addTicket?traffic_id='+recordId+"&user=${user}"+"&group=${group}"+"&comment="+ticketComment+"&lastReport="+lastReport,
                                                            contentType: "application/json; charset=utf-8",
                                                            data: { 'param':'gaugeParameters' },
                                                            success: function(data) {
                                                            // data.value is the success return json. json string contains key value

                                                                $.alert("Ticket "+data.Ticket+" created sucessfully", { autoClose:false,});
                                                                $('#ticketForm')[0].reset();
                                                            },
                                                            error: function() {
                                                            $.alert("Error accediendo a Venus no se puede crear ticket", { autoClose:false,});
                                                            return true;
                                                            },
                                                            complete: function() {

                                                            }
                                                         });
                                                    createTicketDialog.dialog( "close" );
                                                }
                                        }
                                    },

                                    close: function() {
                                        //form[ 0 ].reset();
                                        //allFields.removeClass( "ui-state-error" );
                                    }
                            });
                            createTicketDialog.data("rowId",rowId);
                            createTicketDialog.data("state",atst);
                            createTicketDialog.dialog( "open" );
                            //trafficDialog.dialog( "close" );
                        };
            //}
            buttons["${_('Finalize')}"]=  function() {
                            var callerEventState = $(this).data('ces');
                            if (callerEventState=="N"){
                                $.alert("You are not authorized to finalize", { autoClose:false,});
                            }
                            else{
                                $('#finalizeForm').dialog('option', 'buttons', submitFinalizeButtons);
                                var row = $(this).data('rowId');
                                finalizeDialog.data('rowId',row);
                                finalizeDialog.dialog( "open" );
                            }

                        };

            var trafficDialog = $( "#trafficForm" ).dialog({
                    autoOpen: false,
                    height: winHeight,
                    width: winWidth,
                    modal: true,
                    buttons: buttons,
                    closeOnEscape:false,
                    close: function() {
                        //form[ 0 ].reset();
                        //allFields.removeClass( "ui-state-error" );
                    },


                });
            var finalizeButtons = {
                        "${_('Exit')}": function() {
                            $('#commentForm')[0].reset();
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
                        $( "#commentForm" ).validate({
                                          rules: {
                                               comment:{required:true, wordCount: ['10']},
                                              }
                                        });
                        if($("#commentForm").valid()){   // test for validity
                         var row = $(this).data('rowId');
                         updateState(row,'C');
                         finalizeDialog.dialog( "close" );
                         trafficDialog.dialog( "close" );
                            }
                        },
                        "${_('Exit')}": function() {
                            $('#commentForm')[0].reset();
                            finalizeDialog.dialog( "close" );
                            }
                        };
            var finalizeDialog = $( "#finalizeForm" ).dialog({
                    autoOpen: false,
                    height: winHeight-100,
                    width: winWidth-200,
                    modal: true,
                    buttons: finalizeButtons,
                    close: function() {
                        $('#commentForm')[0].reset();
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


            var rowData = jQuery('#jqGridAlerts').getRowData(rowId);
            var atst=rowData['attended_state'];
            var azimuth=rowData['azimuth'];
            var degrees=parseInt(azimuth);
            var eventdescript=rowData['event_desc'];
            var vehicledescript=rowData['vehicle'];
            var eventtime=rowData['time_stamp'];
            $("#compassNeedle").rotate(degrees);
            $("#eventHeading").text(eventdescript);
            $("#vehicleDescription").text(vehicledescript);
            $("#eventTime").text(eventtime);
            $("#degreesAzimuth").html('<p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp'+degrees+String.fromCharCode(176)+'</p>');
            var urlinstall='';
            $.ajax({
            type: "GET",

            url: '${h.url()}/traffic/getRecord?record='+rowId+"&user=${user}"+"&group=${group}"+"&state=open"+"&tz=${tz}",
            contentType: "application/json; charset=utf-8",
            data: { 'param':'gaugeParameters' },
            success: function(parameterdata) {
                function dateFmatter ( cellvalue, options, rowObject )
                {
                    var utcDate=moment.utc(cellvalue,"YYYY-MM-DD h:mm:ss")
                    var localDate=moment(utcDate).local();
                    var formatdate = localDate.format("YYYY-MM-DD HH:mm:ss");
                    return formatdate;
                }
                //Insert HTML code

                $("#account").html(parameterdata.account);
                $("#event").html(parameterdata.event);
                $("#vehicle").html(parameterdata.vehicle);
                $("#callerList").html(parameterdata.callerlist);
                $("#accountHistory").html(parameterdata.accounthistory);
                $("#comment").val(parameterdata.comment);
                $("#alarmcheck").val(parameterdata.false_alarm);
                $("#eventLink").html(parameterdata.platform);
                $("#images").html(parameterdata.images);
                // Render time in local
                $('#ts').text(dateFmatter(parameterdata.ts));
                $('#et').text(dateFmatter(parameterdata.et));
                $('#jqGridAlerts').trigger( 'reloadGrid' );
                $("#trafficForm").show();
                $("#dialog").dialog();
                c5plates=parameterdata.plates;
                urlinstall=parameterdata.link;
                icc=parameterdata.icc;
                initMap(parameterdata.latitude, parameterdata.longitude,parameterdata.cell_lat,parameterdata.cell_lon);
                activateTab('account');
                if (parameterdata.attended_state=="C"){
                    $('#finalizeForm').dialog('option', 'buttons', finalizeButtons);
                    finalizeDialog.dialog( "open" );
                }
                else{
                    if(parameterdata.attended_state=="N"){
                        updateState(rowId,"A");
                    }
                //get other data

                trafficDialog.data("rowId",rowId);
                trafficDialog.data("state",atst);
                trafficDialog.data("ces",parameterdata.callerEventState);
                trafficDialog.dialog( "open" );
                }
            },
            error: function (xhr, ajaxOptions, thrownError) {
                if (xhr.status==503){
                    $.alert("Servicio no disponible en pluton", { autoClose:false,});

                }
                else{
                    $.alert(xhr.status, { autoClose:false,});

                }
              },
            complete: function() {
                $('#button').on('click', function(e){
                    if(urlinstall!='dontHave'){
                        //$dialog.dialog('open');
                        //alert(urlinstall);
                        //$dialog.html("<iframe width='100%' height='100%' src='"+urlinstall+"' frameborder='0' border='none'></iframe>");
                        window.open(urlinstall, '_blank');
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
            var event_grid_name = '#jqGridCallerEvent';

            var event_grid_pager= '#listPagerTables';
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
                    var ve=rowData['brand']+' '+rowData['model']+' '+rowData['year']+' '+rowData['color'];
                    var ci=rowData['client_id'];
                    //load form
                    $.ajax({
                    type: "GET",
                    url: '${h.url()}/traffic/getDynamicTemplate/'+"?listener="+$( "input:checked" ).val()  ,
                    contentType: "application/json; charset=utf-8",
                    data: { 'param':'gaugeParameters' },
                    success: function(parameterdata) {
                        //Insert HTML code
                        $( "#callerEventForm01" ).html(parameterdata.eventtemplate);
                    },
                    error: function() {
                        $.alert("Error accessing server /alerts/getRecord", { autoClose:false,});

                    },
                    complete: function() {

                        var winHeight=Math.round(window.innerHeight*.75);
                        var winWidth=Math.round(window.innerWidth*.75);
                        var assignDialog = $( "#callerEventForm01" ).dialog({
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
                                                    $('#jqGridAlerts').trigger( 'reloadGrid' );
                                                    doDoubleClick(data.id);
                                                    $('#eventsForm')[0].reset();
                                                    assignDialog.dialog( "close" );
                                                    addCallerEventDialog.dialog( "close" );
                                                },
                                                error: function() {
                                                $.alert("Error accessing tables/addPriority", { autoClose:false,});
                                                assignDialog.dialog( "close" );
                                                addCallerEventDialog.dialog( "close" );
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

            $("#callerEventGrid01").show();
            var addCallerEventDialog = $( "#callerEventGrid01" ).dialog({
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

        var traffic_client = Stomp.client('${h.stompServer()}');
        traffic_client.debug=null;
        var traffic_connect_callback = function() {
            var group_str='${group}';
            var group_list=group_str.split(",");
            var i;
            for (i = 0; i < group_list.length; i++) {
                //alert(group_list[i]);
                traffic_client.subscribe("/topic/trafficlistener_"+group_list[i], traffic_subscribe_callback);
            }

            // called back after the client is connected and authenticated to the STOMP server
          };
        var traffic_error_callback = function(error) {
            $.alert(error, { autoClose:false,});
        };
        var traffic_subscribe_callback = function(message) {

            var msg = message.body;
            //var subscription = message.headers.subscription ;
            var payload = msg.split('|');
            var command = payload[0];
            var action = payload[1];

            switch (command) {
                    case 'REPAINT':
                        $('#jqGridAlerts').trigger( 'reloadGrid' );
                        $.ajax({
                        type: "GET",
                        url: '${h.url()}/traffic/getGauges?group=' +"${group}",
                        contentType: "application/json; charset=utf-8",
                        data: { 'param':'gaugeParameters' },
                        success: function(data) {
                            $('#jqGridAlerts').trigger( 'reloadGrid' );
                            attendedGage.refresh(data.attended_statistic);
                            toAttendGage.refresh(data.toattend_statistic);
                            closedGage.refresh(data.closed_statistic);
                            scoreGage.refresh(data.score_statistic);

                        },
                        error: function() {
                        //alert("#"+ckbid);
                            $.alert("Error accessing /getUser", { autoClose:false,});

                            return true;
                        },
                        complete: function() {
                        }
                        });
                        break;
                    case 'RELOAD':

                        $.ajax({
                        type: "GET",
                        url: '${h.url()}/traffic/getGauges?group=' +"${group}",
                        contentType: "application/json; charset=utf-8",
                        data: { 'param':'gaugeParameters' },
                        success: function(data) {
                                                    if(action=="1"){
                            ding.play();
                        }
                        if(action=="2"){
                            claxon.play();
                        }
                        if(action=="3"){
                            bell.play();
                        }
                        if(action=="4"){
                            buzzer.play();
                        }
                        if(action=="5"){
                            alarm.play();
                        }
                        $('#jqGridAlerts').trigger( 'reloadGrid' );
                            $('#jqGridAlerts').trigger( 'reloadGrid' );
                            attendedGage.refresh(data.attended_statistic);
                            toAttendGage.refresh(data.toattend_statistic);
                            closedGage.refresh(data.closed_statistic);
                            scoreGage.refresh(data.score_statistic);
                        //console.log("Action:"+action);
                        //alert("action:"+action);


                        },
                        error: function() {
                        //alert("#"+ckbid);
                            $.alert("Error accessing /getUser", { autoClose:false,});
                            return true;
                        },
                        complete: function() {
                        }
                        });


                        break;
                    case 'MSG':
                        $.alert(action, { autoClose:false,type: 'success',});
                        bell.play();
                        break;
                    case 'GAU':
                        $.ajax({
                        type: "GET",
                        url: '${h.url()}/traffic/getGauges?group='+"${group}",
                        contentType: "application/json; charset=utf-8",
                        data: { 'param':'gaugeParameters' },
                        success: function(data) {
                            $('#jqGridAlerts').trigger( 'reloadGrid' );
                            attendedGage.refresh(data.attended_statistic);
                            toAttendGage.refresh(data.toattend_statistic);
                            closedGage.refresh(data.closed_statistic);
                            scoreGage.refresh(data.score_statistic);

                        },
                        error: function() {
                        //alert("#"+ckbid);
                            $.alert("Error accessing /getUser", { autoClose:false,});

                            return true;
                        },
                        complete: function() {
                        }
                        });
                        break;
            }
          };
        var stompUser='${h.stompUser()}';
        var stompPass='${h.stompPassword()}';
        traffic_client.connect(stompUser, stompPass, traffic_connect_callback, traffic_error_callback, '/');
}
$( document ).ready(function() {
    trafficSegment();
});
</script>
</div>
    <!-- page start-->
    <div id="callerEventForm01"  class="dialog-hidden" title="${_('Traffic')}">
    </div>
    <div id="callerEventGrid01" class="dialog-hidden" title="${_('Evento por llamada')}">
        <table style="width:100%;overflow:auto;">
        <table id="jqGridCallerEvent" class="scroll" cellpadding="0" cellspacing="0"></table>
        <div id="listPagerTables" class="scroll" style="text-align:center;"></div>
        <div id="listPsetcolsEvent" class="scroll" style="text-align:center;"></div>
        </table>
        <br>
    </div>

    <!-- Hidden POP UP start-->
     <div id="addImageForm" class="dialog-hidden" title="${_('Upload Image')}">
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
    <div id="trafficForm" class="dialog-hidden" title="${_('Traffic')}">
        <ul class="nav nav-tabs">
          <li><a data-toggle="tab" href="#account" >${_('Account')}</a></li>
          <li><a data-toggle="tab" href="#event" >${_('Event')}</a></li>
          <li><a data-toggle="tab" href="#vehicle" >${_('Vehicle')}</a></li>
          <li><a data-toggle="tab" href="#callerList" >${_('Caller List')}</a></li>
          <li><a data-toggle="tab" href="#accountHistory">${_('Account History')}</a></li>
          <li><a data-toggle="tab" href="#images">${_('Images')}</a></li>
          <li><a data-toggle="tab" href="#installationReport">${_('Installation Report')}</a></li>
          <li><a data-toggle="tab" href="#locationMap" data-toggle="tab">${_('Map')}</a></li>
        </ul>

        <div class="tab-content">
          <div id="account" class="tab-pane fade in active">
          </div>
          <div id="event" class="tab-pane fade in active">
          </div>
          <div id="vehicle" class="tab-pane fade in active">
          </div>
          <div id="callerList" class="tab-pane fade">
          </div>
          <div id="accountHistory" class="tab-pane fade">
          </div>
          <div id="images" class="tab-pane fade">


          </div>
          <div id="installationReport" class="tab-pane fade">
              <br>
              <button id="button" type="button" class="btn btn-default" data-toggle="button">${_('Print')}</button>
          </div>


          <div id="locationMap" class="tab-pane fade">

              <br>

              <h4 id="eventHeading">${_('Event')}</h4>
              <div class="image123">
                    <div class="imgContainer">
                        <div id="map_canvas"></div>
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
    <div id="finalizeForm" class="dialog-hidden" title="${_('Finalize')}">
      <form id="commentForm">
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
    <table id="jqGridAlerts" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerAlerts" class="scroll" style="text-align:center;"></div>
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


<p>Groups:${group}</p>
  <!-- page end-->