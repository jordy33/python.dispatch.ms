<style type="text/css">
    #content {
    width: 50%;
    margin: 0 auto;
    }
</style>
<script type="text/javascript">


	var startDateTextBox = $('#date_start');
	var endDateTextBox = $('#date_end');

	$( function() {

		$('.btn').click(function() {
			var code=''
			$.ajax({
					type: "GET",
					url: '${h.url()}/traffic/getQRGraphs',
					contentType: "application/json; charset=utf-8",
					data: { 'msg':$('#msg').val(),'size':$('#size').val()},
					success: function(data) {
						// data.value is the success return json. json string contains key value
						$("#content").html(data.graph_data);
					},
					error: function() {
						//alert("#"+ckbid);
						alert("Error accessing getQRGraphs")
						},
					complete: function() {
						}
			});
		});

	  });
</script>

Message:<input id="msg" value="Hello"/>
Size   :<input id="size" value="20" type="number"/>
<button class="btn btn-primary" id="btn-test1">Get QR code</button>

<div id="content">

</div>
