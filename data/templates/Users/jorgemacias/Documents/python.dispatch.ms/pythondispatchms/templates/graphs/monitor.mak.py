# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555372040.449147
_enable_loop = True
_template_filename = '/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/graphs/monitor.mak'
_template_uri = '/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/graphs/monitor.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<script type="text/javascript">\n\n\n\tvar startDateTextBox = $(\'#date_start\');\n\tvar endDateTextBox = $(\'#date_end\');\n\n\t$( function() {\n\t\tvar dateFormat = "yy-mm-dd",\n\t\t  from = startDateTextBox.datepicker({\n\t\t\t  defaultDate: "+1w",\n\t\t\t  changeMonth: true,\n\t\t\t  numberOfMonths: 3,\n\t\t\t  dateFormat:\'yy-mm-dd\'\n\t\t\t})\n\t\t\t.on( "change", function() {\n\t\t\t  to.datepicker( "option", "minDate", getDate( this ) );\n\t\t\t}),\n\t\t  to = endDateTextBox.datepicker({\n\t\t\tdefaultDate: "+1w",\n\t\t\tchangeMonth: true,\n\t\t\tnumberOfMonths: 3,\n\t\t\tdateFormat:\'yy-mm-dd\'\n\t\t  })\n\t\t  .on( "change", function() {\n\t\t\tfrom.datepicker( "option", "maxDate", getDate( this ) );\n\t\t  });\n\n\n\t\tfunction getDate( element ) {\n\t\t  var date;\n\t\t  try {\n\t\t\tdate = $.datepicker.parseDate( dateFormat, element.value );\n\t\t\t//alert(date);\n\t\t  } catch( error ) {\n\t\t\tdate = null;\n\t\t  }\n\t\t  return date;\n\t\t}\n\t\t$(\'.btn\').click(function() {\n\t\t\tvar code=\'\'\n\t\t\t$.ajax({\n\t\t\t\t\ttype: "GET",\n\t\t\t\t\turl: \'')
        __M_writer(escape(h.url()))
        __M_writer('/traffic/getMonitorGraphs\',\n\t\t\t\t\tcontentType: "application/json; charset=utf-8",\n\t\t\t\t\tdata: { \'start\':$(\'#date_start\').val(), \'end\':$(\'#date_end\').val()},\n\t\t\t\t\tsuccess: function(data) {\n\t\t\t\t\t\t// data.value is the success return json. json string contains key value\n                        alert(data.graph_data[0]);\n\t\t\t\t\t\t$(\'#g0\').attr(\'src\', data.graph_data[0]);\n\t\t\t\t\t\t$(\'#g1\').attr(\'src\', data.graph_data[1]);\n\t\t\t\t\t\t$(\'#g2\').attr(\'src\', data.graph_data[2]);\n\t\t\t\t\t\t$(\'#g3\').attr(\'src\', data.graph_data[4]);\n\t\t\t\t\t\t$(\'#g4\').attr(\'src\', data.graph_data[4]);\n\t\t\t\t\t\t$(\'#g5\').attr(\'src\', data.graph_data[5]);\n\t\t\t\t\t\t$(\'#g6\').attr(\'src\', data.graph_data[6]);\n\t\t\t\t\t},\n\t\t\t\t\terror: function() {\n\t\t\t\t\t\t//alert("#"+ckbid);\n\t\t\t\t\t\talert("Error accessing server notification/badge")\n\t\t\t\t\t\t},\n\t\t\t\t\tcomplete: function() {\n\t\t\t\t\t\t}\n\t\t\t});\n\t\t});\n\n\t  });\n</script>\n\nInicio:<input id="date_start"/> Fin:<input id="date_end"/>\n<button class="btn btn-primary" id="btn-test1">Obtener gráfica</button>\n<div class="container" align="left">\n\t<embed id="g0" type="image/svg+xml" src=\'\' style=\'height:500px\'/>\n\t<embed id="g1" type="image/svg+xml" src=\'\' style=\'height:500px\'/>\n\t<embed id="g2" type="image/svg+xml" src=\'\' style=\'height:500px\'/>\n\t<embed id="g3" type="image/svg+xml" src=\'\' style=\'height:500px\'/>\n\t<embed id="g4" type="image/svg+xml" src=\'\' style=\'height:500px\'/>\n\t<embed id="g5" type="image/svg+xml" src=\'\' style=\'height:500px\'/>\n\t<embed id="g6" type="image/svg+xml" src=\'\' style=\'height:500px\'/>\n\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"24": 43, "17": 0, "31": 25, "25": 43, "23": 1}, "uri": "/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/graphs/monitor.mak", "filename": "/Users/jorgemacias/Documents/python.dispatch.ms/pythondispatchms/templates/graphs/monitor.mak"}
__M_END_METADATA
"""
