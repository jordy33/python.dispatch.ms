
<style type="text/css">
</style>
<script>

            function dateFmatter ( cellvalue, options, rowObject )
            {
                var utcDate=moment.utc(cellvalue,"YYYY-MM-DD h:mm:ss")
                var localDate=moment(utcDate).local();
                var formatdate = localDate.format("YYYY-MM-DD HH:mm:ss");
                return formatdate;
            }
            function statusFmatter ( cellvalue, options, rowObject ){
                html=cellvalue;
                switch (cellvalue){
                    case cellvalue="A":
                        html = '<center><span class="glyphicon glyphicon-search" style="color:blue"></span></center>';
                        break;
                    case cellvalue="N":
                        html = '<center><span class="glyphicon glyphicon-remove" style="color:red"></span></center>';
                        break;
                    case cellvalue="C":
                        html = '<center><span class="glyphicon glyphicon-ok" style="color:green"></span></center>';
                        break;
                    case cellvalue="P":
                        html = '<center><span class="glyphicon glyphicon-time" style="color:sandybrown"></span></center>';
                        break;
                }
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
            var grid_name = '#jgGridListeners';
            var grid_pager= '#listPagerListeners';
            var update_url='/traffic/updateTraffic/?user=${user}';
            var load_url='/traffic/loadTraffic/?user=${user}';
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
            var grid = jQuery(grid_name);

            $(document).ready(function () {
                grid.jqGrid({
                url: load_url,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['${_('Hidden')}', '${_('Status')}', '${_('Priority')}', '${_('Client')}', '${_('Event')}', '${_('Event Description')}','${_('Vehicle')}','${_('Date')}','Hidden','Hidden','Hidden','Hidden','Hidden','Hidden','Hidden','Hidden','Hidden','Listener','User'],
                colModel: [
                    {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: true}},
                    {name: 'attended_state', index: 'attended_state', width: 2,align: 'right',hidden: false, editable: true, edittype: 'text', formatter:statusFmatter, editrules: {required: true},search:false},
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
                    doDoubleClick(rowId)
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

            }
            function AddCallerEvent() {
            }
            </script>
</div>
    <!-- page start-->
    <!-- Hidden POP UP Start-->

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