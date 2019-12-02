# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528997895.415313
_enable_loop = True
_template_filename = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/websockets.mak'
_template_uri = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/websockets.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        id = context.get('id', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('  <style>\n      .box {\n          width: 440px;\n          float: left;\n          margin: 0 20px 0 20px;\n      }\n\n      .box div, .box input {\n          border: 1px solid;\n          -moz-border-radius: 4px;\n          border-radius: 4px;\n          width: 100%;\n          padding: 5px;\n          margin: 3px 0 10px 0;\n      }\n\n      .box div {\n          border-color: grey;\n          height: 300px;\n          overflow: auto;\n      }\n\n      div code {\n          display: block;\n      }\n\n      #first')
        __M_writer(escape(id))
        __M_writer(' div code {\n          -moz-border-radius: 2px;\n          border-radius: 2px;\n          border: 1px solid #eee;\n          margin-bottom: 5px;\n      }\n\n      #second')
        __M_writer(escape(id))
        __M_writer(' div {\n          font-size: 0.8em;\n      }\n  </style>\n  <title>RabbitMQ Web STOMP Examples : Echo Server</title>\n  <link href="main.css" rel="stylesheet" type="text/css"/>\n</head><body lang="en">\n    <h3>Rabbit MQ Stomp User:')
        __M_writer(escape(user))
        __M_writer(' Channel:')
        __M_writer(escape(id))
        __M_writer('</h3>\n\n    <div id="first')
        __M_writer(escape(id))
        __M_writer('" class="box">\n      <h3>Received</h3>\n      <div></div>\n      <form><input autocomplete="off" value="Type here..."></input></form>\n    </div>\n\n    <div id="second')
        __M_writer(escape(id))
        __M_writer('" class="box">\n      <h3>Logs</h3>\n      <div></div>\n    </div>\n\n    <script>\n\n        var channel')
        __M_writer(escape(id))
        __M_writer(' ="')
        __M_writer(escape(id))
        __M_writer('";\n        var has_had_focus')
        __M_writer(escape(id))
        __M_writer(' = false;\n        var pipe = function(el_name, send) {\n            var div  = $(el_name + \' div\');\n            var inp  = $(el_name + \' input\');\n            var form = $(el_name + \' form\');\n\n            var print = function(m, p) {\n                p = (p === undefined) ? \'\' : JSON.stringify(p);\n                div.append($("<code>").text(m + \' \' + p));\n                div.scrollTop(div.scrollTop() + 10000);\n            };\n\n            if (send) {\n                form.submit(function() {\n                    send(inp.val());\n                    inp.val(\'\');\n                    return false;\n                });\n            }\n            return print;\n        };\n\n      // Stomp.js boilerplate\n      //var client')
        __M_writer(escape(id))
        __M_writer(" = Stomp.client('ws://test.dwim.mx:15674/ws');\n      var client")
        __M_writer(escape(id))
        __M_writer(" = Stomp.client('")
        __M_writer(escape(h.stompServer()))
        __M_writer("');\n      client")
        __M_writer(escape(id))
        __M_writer(".debug = pipe('#second")
        __M_writer(escape(id))
        __M_writer("');\n\n      var print_first")
        __M_writer(escape(id))
        __M_writer(" = pipe('#first")
        __M_writer(escape(id))
        __M_writer("', function(data) {\n          client")
        __M_writer(escape(id))
        __M_writer(".send('/topic/'+channel")
        __M_writer(escape(id))
        __M_writer(', {"content-type":"text/plain"}, data);\n      });\n      var on_connect')
        __M_writer(escape(id))
        __M_writer(' = function(x) {\n          id = client')
        __M_writer(escape(id))
        __M_writer('.subscribe("/topic/"+channel')
        __M_writer(escape(id))
        __M_writer(', function(d) {\n               print_first')
        __M_writer(escape(id))
        __M_writer('(d.body);\n          });\n      };\n      var on_error')
        __M_writer(escape(id))
        __M_writer(" =  function() {\n        console.log('error');\n      };\n      client")
        __M_writer(escape(id))
        __M_writer(".connect('dwim', 'gpscontrol1', on_connect")
        __M_writer(escape(id))
        __M_writer(', on_error')
        __M_writer(escape(id))
        __M_writer(", '/');\n\n      $('#first")
        __M_writer(escape(id))
        __M_writer(" input').focus(function() {\n          if (!has_had_focus")
        __M_writer(escape(id))
        __M_writer(') {\n              has_had_focus')
        __M_writer(escape(id))
        __M_writer(' = true;\n              $(this).val("");\n          }\n      });\n    </script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"17": 0, "25": 1, "26": 27, "27": 27, "28": 34, "29": 34, "30": 41, "31": 41, "32": 41, "33": 41, "34": 43, "35": 43, "36": 49, "37": 49, "38": 56, "39": 56, "40": 56, "41": 56, "42": 57, "43": 57, "44": 80, "45": 80, "46": 81, "47": 81, "48": 81, "49": 81, "50": 82, "51": 82, "52": 82, "53": 82, "54": 84, "55": 84, "56": 84, "57": 84, "58": 85, "59": 85, "60": 85, "61": 85, "62": 87, "63": 87, "64": 88, "65": 88, "66": 88, "67": 88, "68": 89, "69": 89, "70": 92, "71": 92, "72": 95, "73": 95, "74": 95, "75": 95, "76": 95, "77": 95, "78": 97, "79": 97, "80": 98, "81": 98, "82": 99, "83": 99, "89": 83}, "uri": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/websockets.mak", "filename": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/test/websockets.mak", "source_encoding": "utf-8"}
__M_END_METADATA
"""
