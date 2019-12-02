<link href="${tg.url('/lib/css/jquery.steps.css')}" rel="stylesheet">
<script src="${tg.url('/lib/jquery-validation-1.17.0/dist/jquery.validate.js')}"></script>
<script src="${tg.url('/lib/js/jquery.steps.js')}"></script>
<style type="text/css">
</style>
<script type="text/javascript">
var users;
function addGroupWindow(){
    var winHeight = 400; //Math.round(window.innerHeight * .50)
    var winWidth = 810;//Math.round(window.innerWidth * .50)
    var grid_name_email = 'jgGrid4Group';
    var pager_name = "jqGridPager4Group";
    var grid_name_email_by_id = '#'+grid_name_email;
    var pager_name_by_id = '#'+pager_name;
    if ($(grid_name_email_by_id).length){
        $(grid_name_email_by_id).remove();
        $(pager_name_by_id).remove();
    }
    if ($("#GroupForm").length){
        $("#GroupForm").remove();
    }
    var newDiv = $(document.createElement('div'));
    var html='<div id="GroupForm" title="Filter">'
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
        url: '${h.url()}/admin/getGroups4Roles',
        mtype: "GET",
        datatype: "json",
        page: 1,
        colModel: [
            {label: "Grupo", name: 'groupname', key: true, width: 150},
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
            $('#group-name').val(rowData['groupname']);
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
function addUsers2Rol(){
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
                    title: "Presione finalizar para salir",
                    height: winHeight - 20,
                    width: winWidth,
                    modal: true,
                    close: function () {
                    }
                });
                var grid = new jQuery(grid_name_users_by_id);
                grid.jqGrid({
                    url: '${h.url()}/admin/getUsersFromGroup'+'?group='+$('#group-name').val(),
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
                        var rowData = jQuery(grid_name_users_by_id).getRowData(rowId);
                        users = jQuery(grid_name_users_by_id).jqGrid('getGridParam','selarrrow');
                        $('#rolUsersCount').val(users.length);
                        createUsersSticky2.dialog("close");
                    },
                });
                createUsersSticky2.dialog("open");
}


$(document).ready(function() {
    var form = $("#roles-form");
    form.validate({
        errorPlacement: function errorPlacement(error, element) { element.before(error); },
        rules: {
            endDate: {
                 greaterThan: "#startDate"
            }
        }
    });
    form.children("div").steps({
        headerTag: "h3",
        bodyTag: "section",
        transitionEffect: "slideLeft",
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
                  url: '${h.url()}/admin/saveWizardRoles',
                  contentType: "application/json; charset=utf-8",
                  data: { 'rolname':$('#rolname').val() ,'group-name':$('#group-name').val(),'users':users.toString()},
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
    <form id="roles-form" action="#">
        <div>
            <h3>Datos preliminares del Rol</h3>
            <section>
                <label for="rolname">Nombre del Rol *</label>
                <input id="rolname" name="rolname" type="text" class="required" maxlength="30">
                <p>(*) Requeridos</p>
            </section>
            <h3>Seleccionar Grupo</h3>
            <section>
                <label for="group-name">Grupo (para ayuda dar click en el campo)</label>
                <input id="group-name" name="client-id" type="text" class="required" onclick="addGroupWindow()">
                <p>(*) Requeridos</p>
            </section>
            <h3>Asignar Usuarios</h3>
            <section>
                <label for="rolUsersCount">Usuarios (para ayuda dar click en el campo)</label>
                <input id="rolUsersCount" type="number" name="rolUsersCount" min="1" max="60" value="0" onclick="addUsers2Rol()">
            </section>
        </div>
    </form>
</div>