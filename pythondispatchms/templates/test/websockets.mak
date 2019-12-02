  <style>
      .box {
          width: 440px;
          float: left;
          margin: 0 20px 0 20px;
      }

      .box div, .box input {
          border: 1px solid;
          -moz-border-radius: 4px;
          border-radius: 4px;
          width: 100%;
          padding: 5px;
          margin: 3px 0 10px 0;
      }

      .box div {
          border-color: grey;
          height: 300px;
          overflow: auto;
      }

      div code {
          display: block;
      }

      #first${id} div code {
          -moz-border-radius: 2px;
          border-radius: 2px;
          border: 1px solid #eee;
          margin-bottom: 5px;
      }

      #second${id} div {
          font-size: 0.8em;
      }
  </style>
  <title>RabbitMQ Web STOMP Examples : Echo Server</title>
  <link href="main.css" rel="stylesheet" type="text/css"/>
</head><body lang="en">
    <h3>Rabbit MQ Stomp User:${user} Channel:${id}</h3>

    <div id="first${id}" class="box">
      <h3>Received</h3>
      <div></div>
      <form><input autocomplete="off" value="Type here..."></input></form>
    </div>

    <div id="second${id}" class="box">
      <h3>Logs</h3>
      <div></div>
    </div>

    <script>

        var channel${id} ="${id}";
        var has_had_focus${id} = false;
        var pipe = function(el_name, send) {
            var div  = $(el_name + ' div');
            var inp  = $(el_name + ' input');
            var form = $(el_name + ' form');

            var print = function(m, p) {
                p = (p === undefined) ? '' : JSON.stringify(p);
                div.append($("<code>").text(m + ' ' + p));
                div.scrollTop(div.scrollTop() + 10000);
            };

            if (send) {
                form.submit(function() {
                    send(inp.val());
                    inp.val('');
                    return false;
                });
            }
            return print;
        };

      // Stomp.js boilerplate
      //var client${id} = Stomp.client('ws://test.dwim.mx:15674/ws');
      var client${id} = Stomp.client('${h.stompServer()}');
      client${id}.debug = pipe('#second${id}');

      var print_first${id} = pipe('#first${id}', function(data) {
          client${id}.send('/topic/'+channel${id}, {"content-type":"text/plain"}, data);
      });
      var on_connect${id} = function(x) {
          id = client${id}.subscribe("/topic/"+channel${id}, function(d) {
               print_first${id}(d.body);
          });
      };
      var on_error${id} =  function() {
        console.log('error');
      };
      client${id}.connect('dwim', 'gpscontrol1', on_connect${id}, on_error${id}, '/');

      $('#first${id} input').focus(function() {
          if (!has_had_focus${id}) {
              has_had_focus${id} = true;
              $(this).val("");
          }
      });
    </script>

