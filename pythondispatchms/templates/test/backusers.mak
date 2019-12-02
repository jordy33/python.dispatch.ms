<style type="text/css">
</style>
<script type="text/javascript">



$(document).ready(function () {
userWindow();

function userWindow(){
        var winHeight = Math.round(window.innerHeight * .50)
        var winWidth = Math.round(window.innerWidth * .50)
        var grid_name = '#jgGrid4Users';
        var pager_name = "#jqGridPager4Users";
        var newDiv = $(document.createElement('div'));
        var grid_name_html= grid_name.substr(1);
        var pager_name_html=pager_name.substr(1);
        if ($(grid_name).length){
          $(grid_name).remove();
          $(pager_name).remove();
        }
        var newDiv = $(document.createElement('div'));
        newDiv.html('<table id="'+grid_name_html+'"></table> <div id="'+pager_name_html+'"> </div>');
        var createUsersSticky = newDiv.dialog({
            autoOpen: false,
            height: winHeight - 20,
            width: winWidth,
            modal: true,
            close: function () {
                //form[ 0 ].reset();
                //allFields.removeClass( "ui-state-error" );
            }
        });
        var grid = jQuery(grid_name);
        grid.jqGrid({
            url: 'test/getUsers',
            mtype: "GET",
            datatype: "json",
            page: 1,
            colModel: [
                {label: "User Name", name: 'username', key: true, width: 150},
                {label: "Email", name: 'email', width: 150}
            ],
            loadonce: true,
            viewrecords: true,
            width: 780,
            height: 250,
            rowNum: 10,
            pager: pager_name,
            ondblClickRow: function (rowId) {
                doDoubleClick(rowId)
            },

        });
        grid.navGrid(pager_name, {
            search: true,
            add: false,
            edit: false,
            del: false,
            refresh: true
        }, {}, {}, {}, {multipleSearch: true,});

        function doDoubleClick(rowId) {
            var rowData = jQuery('#jgGrid4Users').getRowData(rowId);
            alert(rowData['username']);

            createUsersSticky.dialog("close");
        }
        createUsersSticky.dialog("open");
}


    });

</script>


  <!-- page end-->