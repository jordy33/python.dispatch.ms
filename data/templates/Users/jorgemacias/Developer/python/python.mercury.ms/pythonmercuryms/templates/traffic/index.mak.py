# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1526655994.927074
_enable_loop = True
_template_filename = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/traffic/index.mak'
_template_uri = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/traffic/index.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('    <script src="')
        __M_writer(escape(tg.url('/justgage/raphael-2.1.4.min.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/justgage/justgage.js')))
        __M_writer('"></script>\n<script>\n            var attendedGage= new JustGage({\n                id: "attendedGauge",\n                value: 0,\n                min: 0,\n                max: 100,\n                title: "')
        __M_writer(escape(_('Attended')))
        __M_writer('"\n            });\n            var toAttendGage = new JustGage({\n                id: "toAttendGauge",\n                value: 0,\n                min: 0,\n                max: 100,\n                title: "')
        __M_writer(escape(_('To Attend')))
        __M_writer('"\n            });\n            var closedGage = new JustGage({\n                id: "closedGauge",\n                value: 0,\n                min: 0,\n                max: 100,\n                title: "')
        __M_writer(escape(_('Closed')))
        __M_writer('"\n            });\n            var scoreGage = new JustGage({\n                id: "scoreGauge",\n                value: 0,\n                min: 0,\n                max: 100,\n                levelColors : [ \t"#FF0000","#c18c05", "#98C105" ],\n                title: "')
        __M_writer(escape(_('Score')))
        __M_writer('"\n            });\n            $(document).ready(\n            function () {\n            function dateFmatter ( cellvalue, options, rowObject )\n            {\n\n            }\n            function statusFmatter ( cellvalue, options, rowObject ){\n\n            }\n            function priorityFmatter ( cellvalue, options, rowObject )\n            {\n\n            }\n            function AddCallerEvent() {\n\n            }\n            var grid_name = \'#jqGridAlerts\';\n            var grid_pager= \'#listPagerAlerts\';\n            var update_url=\'/traffic/updateTraffic\';\n            var load_url=\'/traffic/loadTraffic\';\n            var header_container=\'')
        __M_writer(escape(_('Alerts')))
        __M_writer('\';\n            var addParams = {left: 0,width: window.innerWidth-700,top: 20,height: 190,url: update_url, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var editParams = {left: 0,width: window.innerWidth-700,top: 20,height: 200,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,\n                    width: "500",\n                    editfunc: function (rowid) {\n                    }\n                };\n            var deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url,modal: true, };\n            var grid = jQuery(grid_name);\n            grid.jqGrid({\n                url: load_url,\n                datatype: \'json\',\n                mtype: \'GET\',\n                colNames: [\'')
        __M_writer(escape(_('Hidden')))
        __M_writer("', '")
        __M_writer(escape(_('Status')))
        __M_writer("', '")
        __M_writer(escape(_('Priority')))
        __M_writer("', '")
        __M_writer(escape(_('Client')))
        __M_writer("', '")
        __M_writer(escape(_('Event')))
        __M_writer("', '")
        __M_writer(escape(_('Event Description')))
        __M_writer("','")
        __M_writer(escape(_('Vehicle')))
        __M_writer("','")
        __M_writer(escape(_('Date')))
        __M_writer('\',\'Hidden\',\'Hidden\',\'Hidden\',\'Hidden\',\'Hidden\',\'Hidden\',\'Hidden\',\'Hidden\',\'Hidden\',\'Listener\'],\n                colModel: [\n                    {name: \'id\',index: \'id\', width: 5,align: \'left\',key:true,hidden: true, editable: true,edittype: \'text\',editrules: {required: true}},\n                    {name: \'attended_state\', index: \'attended_state\', width: 2,align: \'right\',hidden: false, editable: true, edittype: \'text\', formatter:statusFmatter, editrules: {required: true},search:false},\n                    {name: \'priority\', index: \'priority\', width: 7,align: \'right\',hidden: false, editable: true, edittype: \'text\', formatter:priorityFmatter, editrules: {required: true},search:false},\n                    {name: \'user_name\',index: \'user_name\',width: 25,align: \'right\',hidden: false,editable: true,edittype: \'text\',editrules: {required: false}},\n                    {name: \'event_id\',index: \'event_id\',width: 5,align: \'right\',hidden: false,editable: true,edittype: \'text\',editrules: {required: false}},\n                    {name: \'event_desc\',index: \'event_desc\', width: 25, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'vehicle\',index: \'vehicle\',width: 25,align: \'right\',editable: true,edittype: \'text\',editrules: {required: true}},\n                    {name: \'time_stamp\',index: \'time_stamp\', width: 14, align: \'right\',hidden: false,editable: true, edittype: \'text\', formatter:dateFmatter,editrules: {required: false}},\n                    {name: \'attended_time\',index: \'attended_time\', width: 30, align: \'right\',hidden: true,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'pending_time\',index: \'pending_time\', width: 30, align: \'right\',hidden: true,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'closed_time\',index: \'closed_time\', width: 30, align: \'right\',hidden: true,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'user_id\',index: \'user_id\', width: 5, align: \'right\', hidden: true, editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'imei\',index: \'imei\', width: 5, align: \'right\', hidden: true, editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'latitude\',index: \'latitude\',width: 5, align: \'right\',hidden: true, editable: true, edittype: \'text\', editrules: {required: false}},\n                    {name: \'longitude\',index: \'longitude\',width: 5,align: \'right\', hidden: true, editable: true,edittype: \'text\', editrules: {required: false}},\n                    {name: \'speed\',index: \'speed\',width: 5,align: \'right\', hidden: true, editable: true,edittype: \'text\', editrules: {required: false}},\n                    {name: \'azimuth\',index: \'azimuth\',width: 5,align: \'right\', hidden: true, editable: true,edittype: \'text\', editrules: {required: false}},\n                    {name: \'listener\',index: \'listener\',width: 5,align: \'right\', hidden: true, editable: true,edittype: \'text\', editrules: {required: false}},\n                ],\n                pager: jQuery(grid_pager),\n                rowNum: 10,\n                rowList: [10, 50, 100],\n                sortname: \'time_stamp\',\n                sortorder: "desc",\n                viewrecords: true,\n                autowidth: true,\n                height: 250,\n                ondblClickRow: function(rowId) {\n                    doDoubleClick(rowId)\n                },\n                //caption: header_container,\n            });\n            grid.jqGrid(\'navGrid\',grid_pager,{edit:false,add:false,del:false, search:true},\n                            editParams,\n                            addParams,\n                            deleteParams,\n                            searchParams,\n                            viewParams);\n            // add custom button\n            grid.navButtonAdd(grid_pager,\n                {\n                    buttonicon: "ui-icon-plus",\n                    title: "')
        __M_writer(escape(_('Add')))
        __M_writer('",\n                    caption: "')
        __M_writer(escape(_('Add')))
        __M_writer('",\n                    position: "first",\n                    onClickButton: AddCallerEvent\n                });\n\n\n            });\n\n            </script>\n</div>\n    <!-- JQGRID table start-->\n    <table style="width:100%">\n    <table id="jqGridAlerts" class="scroll" cellpadding="0" cellspacing="0"></table>\n    <div id="listPagerAlerts" class="scroll" style="text-align:center;"></div>\n    <div id="listPsetcols" class="scroll" style="text-align:center;"></div>\n    </table>\n    <br>\n    <!-- Gauge Meters-->\n    <div class="row">\n      <div class="col-lg-3">\n          <section class="panel">\n              <div class="panel-body"><div id="attendedGauge" class="30x30px"></div></div>\n          </section>\n      </div>\n      <div class="col-lg-3">\n          <section class="panel">\n              <div class="panel-body"><div id="toAttendGauge" class="30x30px"></div></div>\n          </section>\n      </div>\n      <div class="col-lg-3">\n          <section class="panel">\n              <div class="panel-body"><div id="closedGauge" class="30x30px"></div></div>\n          </section>\n      </div>\n      <div class="col-lg-3">\n          <section class="panel">\n              <div class="panel-body"><div id="scoreGauge" class="30x30px"></div></div>\n          </section>\n      </div>\n    </div>\n  <!-- page end-->')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 58, "17": 0, "24": 1, "25": 1, "26": 1, "27": 2, "28": 2, "29": 9, "30": 9, "31": 16, "32": 16, "33": 23, "34": 23, "35": 31, "36": 31, "37": 53, "38": 53, "39": 68, "40": 68, "41": 68, "42": 68, "43": 68, "44": 68, "45": 68, "46": 68, "47": 68, "48": 68, "49": 68, "50": 68, "51": 68, "52": 68, "53": 68, "54": 68, "55": 112, "56": 112, "57": 113, "58": 113}, "uri": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/traffic/index.mak", "filename": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/traffic/index.mak", "source_encoding": "utf-8"}
__M_END_METADATA
"""
