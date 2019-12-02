<link href="${tg.url('/lib/css/jquery.steps.css')}" rel="stylesheet">
<script src="${tg.url('/lib/jquery-validation-1.17.0/dist/jquery.validate.js')}"></script>
<script src="${tg.url('/lib/js/jquery.steps.js')}"></script>
<style type="text/css">
</style>
<script type="text/javascript">
var imeis;
function addRoleWindow(){
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
                    title: "Doble click para seleccionar rol",
                    height: winHeight - 20,
                    width: winWidth,
                    modal: true,
                    close: function () {
                    }
                });
                var grid = new jQuery(grid_name_email_by_id);
                grid.jqGrid({
                    url: '${h.url()}/admin/getRol',
                    mtype: "GET",
                    datatype: "json",
                    page: 1,
                    colModel: [
                        {label: "Rol", name: 'rol', key: true, width: 150},
                        {label: "Users", name: 'users', width: 150},
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
                        $('#role').val(rowData['rol']);
                        //AddEmailService(rowData['application_id'],rowData['folio_sinube'],rowData['internal_id'],rowData['username']);
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
function devicesWindows(){
                var winHeight = 400; //Math.round(window.innerHeight * .50)
                var winWidth = 810;//Math.round(window.innerWidth * .50)
                var grid_name_devices = 'jgGridDevices';
                var pager_name = "jqGridPagerDevices";
                var grid_name_devices_by_id = '#'+grid_name_devices;
                var pager_name_by_id = '#'+pager_name;
                if ($(grid_name_devices_by_id).length){
                    $(grid_name_devices_by_id).remove();
                    $(pager_name_by_id).remove();
                }
                if ($("#AppForm1").length){
                    $("#AppForm1").remove();
                }
                var newDiv = $(document.createElement('div'));
                var html='<div id="AppForm1" title="Filter">'
                html=html+'<table id="'+grid_name_devices+'"></table> <div id="'+pager_name+'"> </div>'
                html=html+'</div>'
                newDiv.html(html);

                var createUsersSticky2 = newDiv.dialog({
                    autoOpen: false,
                    title: "Presione finalizar para salir",
                    height: winHeight - 20,
                    width: winWidth,
                    modal: true,
                    close: function () {
                    }
                });
                var grid = new jQuery(grid_name_devices_by_id);
                grid.jqGrid({
                    url: '${h.url()}/admin/getDevices'+'?app_id='+$('#app-id').val(),
                    mtype: "GET",
                    datatype: "json",
                    page: 1,
                    colModel: [
                        {label: "IMEI", name: 'imei', key: true, width: 150},
                        {label: "Eco", name: 'eco', width: 150,hidden:false},
                        {label: "Brand", name: 'brand', width: 150},
                        {label: "Plates", name: 'plates', width: 150,hidden:false},
                        {label: "Color", name: 'color', width: 150,hidden:false}
                    ],
                    loadonce: true,
                    viewrecords: true,
                    width: 780,
                    height: 250,
                    rowNum: 300,
                    multiselect: true,
                    pager: pager_name_by_id,
                    ondblClickRow: function (rowId) {


                        //AddEmailService(rowData['application_id'],rowData['folio_sinube'],rowData['internal_id'],rowData['username']);
                    },

                });
                grid.navGrid(pager_name_by_id, {
                    search: true,
                    add: false,
                    edit: false,
                    del: false,
                    refresh: true
                }, {}, {}, {}, {});
                grid.navButtonAdd(pager_name,
                {
                    buttonicon: "ui-icon-check",
                    title: "${_('Finalizar')}",
                    caption: "${_('Finalizar')}",
                    position: "first",
                    onClickButton: function (rowId) {
                        var rowData = jQuery(grid_name_devices_by_id).getRowData(rowId);
                        imeis = jQuery(grid_name_devices_by_id).jqGrid('getGridParam','selarrrow');
                        $('#mon_units').val(imeis.length);
                        createUsersSticky2.dialog("close");

                        //AddEmailService(rowData['application_id'],rowData['folio_sinube'],rowData['internal_id'],rowData['username']);
                    },
                });
                createUsersSticky2.dialog("open");
}

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
                    title: "Doble click para seleccionar",
                    height: winHeight - 20,
                    width: winWidth,
                    modal: true,
                    close: function () {
                    }
                });
                var grid = new jQuery(grid_name_email_by_id);
                grid.jqGrid({
                    url: '${h.url()}/admin/getClients4Dedicated',
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
                        $('#app-id').val(rowData['application_id']);
                        $('#app-name').text(rowData['username']);
                        $('#mon_units').val(0);
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
var lastsel2
function calendarWindow(){
    $.ajax({
            type: "GET",
            url: '${h.url()}/admin/createTempCalendar',
            contentType: "application/json; charset=utf-8",
            data: { 'startDate':$('#startDate').val() ,'endDate':$('#endDate').val() ,'user':'${user}'},
            success: function(data) {
                // data.value is the success return json. json string contains key value
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
                var user_fields_load_url='${h.url()}/admin/loadMonitorTempCalendars?user_name=${user}';
                var newDiv = $(document.createElement('div'));
                var html='<div id="CalForm" title="Filter">'
                html=html+'<table id="'+grid_name_email+'"></table> <div id="'+pager_name+'"> </div>'
                html=html+'</div>'
                newDiv.html(html);

                var createUsersSticky = newDiv.dialog({
                    autoOpen: false,
                    title: "Calendario",
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
                    editurl: '${h.url()}/admin/updateMonitorTempCalendars?user_name=${user}',
                    caption: "Fechas"

                });
                createUsersSticky.dialog("open");
            },
            error: function() {
                $.alert("Error accesing /admin/updateMonitorstate", { autoClose:false,type: 'danger',});
                return true;
            },
            complete: function() {
            }
    });




}

$(document).ready(function() {
    $('#startTime').timepicker();
    $('#basicExample').timepicker();
    jQuery.validator.addMethod("greaterThan",
        function(value, element, params) {

            if (!/Invalid|NaN/.test(new Date(value))) {
                return new Date(value) > new Date($(params).val());
            }

            return isNaN(value) && isNaN($(params).val())
                || (Number(value) > Number($(params).val()));
        },'Debe ser mayor que {0}.');

    var form = $("#example-form");
    form.validate({
        errorPlacement: function errorPlacement(error, element) { element.before(error); },
        rules: {
            endDate: {
                 greaterThan: "#startDate"
            }
        }
    });
    form.children("div").steps({
        headerTag: "h4",
        bodyTag: "section",
        transitionEffect: "slideLeft",
        stepsOrientation: "vertical",
        onStepChanging: function (event, currentIndex, newIndex)
        {
            form.validate().settings.ignore = ":disabled,:hidden";
            return form.valid();
        },
        onFinishing: function (event, currentIndex)
        {
            form.validate().settings.ignore = ":disabled";
            return form.valid();
        },
        onFinished: function (event, currentIndex)
        {
            $(this).closest('.ui-dialog-content').dialog('close');
            $.ajax({
                  type: "GET",
                  url: '${h.url()}/admin/saveWizardDedicate',
                  contentType: "application/json; charset=utf-8",
                  data: {'nameEvent': $('#nameEvent').val(),'startDate':$('#startDate').val() ,'endDate':$('#endDate').val(),'interval':$('#interval').val(),'app-id':$('#app-id').val(),'app-name':$('#app-name').text(),'imeis':imeis.toString(),'role':$('#role').val(),'user':'${user}'},
                  success: function(parameterdata) {


                  },
                  error: function() {
                     $.alert("Error al guardar el Monitoreo Dedicado", { autoClose:false,});
                  },
                  complete: function() {
                  }
             });
        }
    });

});

</script>

<div id="addWizardForm" title="${_('Filter')} 01">
    <form id="example-form" action="#">
        <div>
            <h4>Datos preliminares de monitoreo</h4>
            <section>
                <label for="nameEvent">Nombre del Evento *</label>
                <input id="nameEvent" name="nameEvent" type="text" class="required" maxlength="30">
                <label for="startDate">Fecha de inicio *</label>
                <input id="startDate" name="startDate" type="datetime-local" class="required" value="${current_time}">
                <label for="endDate">Fecha de fin *</label>
                <input id="endDate" name="endDate" type="datetime-local" class="required" value="${current_time}">
                <br>
                <p>Calendario: <span class="glyphicon glyphicon-calendar" id="cal2" onclick="calendarWindow()"></span></p>

                <label for="interval">Intervalo de Rastreo en Minutos*</label>
                <br>
                <select id="interval">
                    <option value="1" selected="selected">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                    <option value="10">10</option>
                    <option value="12">12</option>
                    <option value="15">15</option>
                    <option value="20">20</option>
                    <option value="30">30</option>
                    <option value="60">60</option>
                </select>
                <p>(*) Requeridos</p>
            </section>

            <h4>Cliente que Recibe Monitoreo</h4>
            <section>
                <label for="app-id">Aplicación ID (para ayuda dar click en el campo)</label>
                <input id="app-id" name="client-id" type="text" class="required" onclick="addUserWindow()">
                <label id="app-name"></label>
                <p>(*) Requeridos</p>
            </section>
            <h4>Unidades que reciben monitoreo</h4>
            <section>
                <label for="mon_units">Unidades (para ayuda dar click en el campo)</label>
                <input id="mon_units" type="number" name="mon_units" min="1" max="60" value="0" onclick="devicesWindows()">
            </section>
            <h4>Asignar Rol de los monitoristas</h4>
            <section>
                <label for="role">Rol (para ayuda dar click en el campo)</label>
                <input id="role" name="role" type="text" class="required" onclick="addRoleWindow()">
            </section>
        </div>
    </form>
</div>