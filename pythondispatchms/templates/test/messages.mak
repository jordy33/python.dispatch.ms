<style type="text/css">
</style>
<script>

            // STOMP
            var subscribe ="/topic/testlistener_"+"${user}";
            var diego_test_client = Stomp.client('${h.stompServer()}');
            diego_test_client.debug=null;
            var diego_test_connect_callback = function() {
                diego_test_client.subscribe(subscribe, diego_test_subscribe_callback);
                // called back after the client is connected and authenticated to the STOMP server
              };
            var diego_test_error_callback = function(error) {
                alert(error);
            };
            var diego_test_subscribe_callback = function(message) {

                var msg = message.body;
                var payload = msg.split('|');
                var command = payload[0];
                var data = payload[1];

                switch (command) {
                        case 'RELOAD':
                            $('#jqGridAlerts').trigger( 'reloadGrid' );
                            break;
                        case 'MSG_GREEN':
                            $.alert(data, { autoClose:false,type: 'success',});
                            break;
                        case 'MSG_RED':
                            $.alert(data, { autoClose:false,type: 'danger',});
                            break;
                        case 'MSG_YELLOW':
                            $.alert(data, { autoClose:false,type: 'warning',});
                            break;
                        case 'MSG_BLUE':
                            $.alert(data, { autoClose:false,type: 'info',});
                            break;
                        case 'MSG_BLUE_WITH_AUTOCLOSE':
                            $.alert(data, { autoClose:true,type: 'info',});
                            break;
                }
              };
            var stompUser='${h.stompUser()}';
            var stompPass='${h.stompPassword()}';
            diego_test_client.connect(stompUser, stompPass, diego_test_connect_callback, diego_test_error_callback, '/');
            function myFunction(color) {
                $.ajax({
                    type: "GET",
                    url: '${h.url()}/test/receiveMessage/',
                    contentType: "application/json; charset=utf-8",
                    data: { 'color':color},
                    success: function(data) {

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
            function myFunction2() {
            }
            </script>
</div>
    <!-- page start-->
    <!-- Hidden POP UP Start-->

    <!-- Hidden POP UP End-->
<div id="noteContent" title="${_('Basic dialog')}">
</div>
    <!-- JQGRID table start-->
<h3>Send message test</h3>

<div class="dropdown">
  <button onclick="myFunction('GREEN')" class="dropbtn">Verde</button>
  <button onclick="myFunction('RED')" class="dropbtn">Rojo</button>
  <button onclick="myFunction('YELLOW')" class="dropbtn">Amarillo</button>
   <button onclick="myFunction('BLUE')" class="dropbtn">Azul</button>
    <button onclick="myFunction('BLUE_WITH_AUTOCLOSE')" class="dropbtn">Azul Cerrando</button>
</div>
  <!-- page end-->