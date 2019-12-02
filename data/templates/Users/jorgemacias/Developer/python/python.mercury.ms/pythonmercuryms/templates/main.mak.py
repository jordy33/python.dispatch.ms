# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528992869.974034
_enable_loop = True
_template_filename = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/main.mak'
_template_uri = '/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/main.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n\n<html lang="en">\n<head>\n    <link rel="icon" type="image/x-icon" href="')
        __M_writer(escape(tg.url('/img/ico/sun.png')))
        __M_writer('"/>\n    <link href="')
        __M_writer(escape(tg.url('/css/bootstrap.min.css')))
        __M_writer('" rel="stylesheet">\n\n    <style type="text/css">\n          /* NOTE: The styles were added inline because Prefixfree needs access to your styles and they must be inlined if they are on local disk! */\n      @import url(')
        __M_writer(escape(tg.url('/css/gfonts.css')))
        __M_writer(');\n\nbody {\n  background: #999;\n  padding: 40px;\n  font-family: "Open Sans Condensed", sans-serif;\n}\nh1 {\n  color: white;\n}\n#bg {\n  position: fixed;\n  left: 0;\n  top: 0;\n  width: 100%;\n  height: 100%;\n  background: url(')
        __M_writer(escape(tg.url('/img/matrix.jpg')))
        __M_writer(') no-repeat center center fixed;\n  background-size: cover;\n  -webkit-filter: blur(0px);\n}\n\nform {\n  position: relative;\n  width: 250px;\n  margin: 0 auto;\n  background: rgba(130,130,130,.3);\n  padding: 20px 22px;\n  border: 1px solid;\n  border-top-color: rgba(255,255,255,.4);\n  border-left-color: rgba(255,255,255,.4);\n  border-bottom-color: rgba(60,60,60,.4);\n  border-right-color: rgba(60,60,60,.4);\n}\n\nform input, form button {\n  width: 212px;\n  border: 1px solid;\n  border-bottom-color: rgba(255,255,255,.5);\n  border-right-color: rgba(60,60,60,.35);\n  border-top-color: rgba(60,60,60,.35);\n  border-left-color: rgba(80,80,80,.45);\n  background-color: rgba(0,0,0,1); /* antes .2 */\n  background-repeat: no-repeat;\n  padding: 8px 24px 8px 10px;\n  font: bold .875em/1.25em "Open Sans Condensed", sans-serif;\n  letter-spacing: .075em;\n  color: #fff;\n  text-shadow: 0 1px 0 rgba(0,0,0,.1);\n  margin-bottom: 19px;\n}\n\nform input:focus { background-color: rgba(0,0,0,.4); }\n\nform input.email {\n  background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAMCAYAAAC9QufkAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyJpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYxIDY0LjE0MDk0OSwgMjAxMC8xMi8wNy0xMDo1NzowMSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNS4xIFdpbmRvd3MiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6M0YwNDIzMTQ3QzIzMTFFMjg3Q0VFQzhDNTgxMTRCRTQiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6M0YwNDIzMTU3QzIzMTFFMjg3Q0VFQzhDNTgxMTRCRTQiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDozRjA0MjMxMjdDMjMxMUUyODdDRUVDOEM1ODExNEJFNCIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDozRjA0MjMxMzdDMjMxMUUyODdDRUVDOEM1ODExNEJFNCIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PsOChsgAAADUSURBVHjaYvz///9JBgYGMwbSwSkGoOafQPwKiAOBmIEIHAXED0H6QJwPQGwAxE+AOJOAxnwgvgfEKiB9MM0gWg6IbwNxIw6NXUB8HogloHwUzSAsBAoDIJ4DxMxQMRA9H4gPADE/kloMzSCsBcR/gHgj1LAt0HBRR1P3gQktBA2AeBcQZwHxCyB+AsT3gTgFKq6FohrJZnssoW6AxPaDBqoZurP9oBrtCYS2ExA/h9JgzX+gAsZExrMZVP0fmGZ1IjWiBCoL0NsXgPgGGcnzLECAAQD5y8iZ2Z69IwAAAABJRU5ErkJggg==);\n  background-position: 220px 10px;\n}\n\nform input.pass {\n  background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAQCAYAAADNo/U5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyJpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYxIDY0LjE0MDk0OSwgMjAxMC8xMi8wNy0xMDo1NzowMSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNS4xIFdpbmRvd3MiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6NTVFMDg1QzU3QzIzMTFFMjgwQThGODZFM0EwQUZFQ0YiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6NTVFMDg1QzY3QzIzMTFFMjgwQThGODZFM0EwQUZFQ0YiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDo1NUUwODVDMzdDMjMxMUUyODBBOEY4NkUzQTBBRkVDRiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDo1NUUwODVDNDdDMjMxMUUyODBBOEY4NkUzQTBBRkVDRiIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Pv2NSIIAAADYSURBVHjanJAxCsJAEEXXaBMQtvIMqTxDKjtPELC1svMoOYM2WlqIhVcQFMVgG7ATAoIggfGPjrLIrBo/vCzZ+Z+dGUNExiECI7Clhw5gAtqur8YfUQxm4AzGIAMRSIAFXbC8OyUdghwsgH173cp9Lr5XqAeOSsANcj3h/8BpbQ4Ko6uQOvtMQy6noG4+iz3XZ4iHbIEQ9L8EeUlN3t5etvSrMg6RqajAc78BQ7BTq6QrllV3tKLvpZOclyrt/TWTlTP0zVQqba/BAKyUWsmh1BPUxL70JsAABHkyyK1uocIAAAAASUVORK5CYII=);\n  background-position: 223px 8px\n}\n\n::-webkit-input-placeholder { color: #ccc; text-transform: uppercase; }\n::-moz-placeholder { color: #ccc; text-transform: uppercase; }\n:-ms-input-placeholder { color: #ccc; text-transform: uppercase; }\n\nform button[type=submit] {\n  width: 210px;\n  margin-bottom: 0;\n  color: #3f898a;\n  letter-spacing: .05em;\n  text-shadow: 0 1px 0 #133d3e;\n  text-transform: uppercase;\n  background: #225556;\n  border-top-color: #9fb5b5;\n  border-left-color: #608586;\n  border-bottom-color: #1b4849;\n  border-right-color: #1e4d4e;\n  cursor: pointer;\n}\n    </style>\n    <script type="text/javascript">\n\n    function logout() {\n          var i = document.childNodes.length - 1;\n          while (i >= 0) {\n            console.log(document.childNodes[i]);\n            document.removeChild(document.childNodes[i--]);\n          }\n          jQuery.ajax({\n                  type: "GET",\n                  url: "/validate/telefonica",\n                  async: false,\n                  username: "logmeout",\n                  password: "123456",\n                  headers: { "Authorization": "Basic xxx" }\n          })\n          .done(function(){\n              // If we don\'t get an error, we actually got an error as we expect an 401!\n          })\n          .fail(function(){\n              // We expect to get an 401 Unauthorized error! In this case we are successfully\n                  // logged out and we redirect the user.\n              window.location = "/";\n          });\n        return false;\n    }\n    </script>\n</head>\n<body>\n  <div id="bg"></div>\n  <br>\n  <1\n  <br><br><br><br><br><br><br>\n\n<form action="')
        __M_writer(escape(tg.url('/secc')))
        __M_writer('" method="post" accept-charset="UTF-8">\n\n<h1><center>dispatch</center></h1>\n<br>\n  <br>\n\n  <button id="enterButton" type="submit">Enter</button>\n\n</form>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/main.mak", "filename": "/Users/jorgemacias/Developer/python/python.dispatch.ms/pythondispatchms/templates/main.mak", "source_encoding": "utf-8", "line_map": {"32": 126, "33": 126, "39": 33, "17": 0, "23": 1, "24": 5, "25": 5, "26": 6, "27": 6, "28": 10, "29": 10, "30": 26, "31": 26}}
__M_END_METADATA
"""
