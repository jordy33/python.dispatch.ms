<script type="text/javascript">


	var startDateTextBox = $('#date_start');
	var endDateTextBox = $('#date_end');

	$( function() {
		var dateFormat = "yy-mm-dd",
		  from = startDateTextBox.datepicker({
			  defaultDate: "+1w",
			  changeMonth: true,
			  numberOfMonths: 3,
			  dateFormat:'yy-mm-dd'
			})
			.on( "change", function() {
			  to.datepicker( "option", "minDate", getDate( this ) );
			}),
		  to = endDateTextBox.datepicker({
			defaultDate: "+1w",
			changeMonth: true,
			numberOfMonths: 3,
			dateFormat:'yy-mm-dd'
		  })
		  .on( "change", function() {
			from.datepicker( "option", "maxDate", getDate( this ) );
		  });


		function getDate( element ) {
		  var date;
		  try {
			date = $.datepicker.parseDate( dateFormat, element.value );
			//alert(date);
		  } catch( error ) {
			date = null;
		  }
		  return date;
		}
		$('.btn').click(function() {
			var code=''
			$.ajax({
					type: "GET",
					url: '${h.url()}/traffic/getMonitorGraphs',
					contentType: "application/json; charset=utf-8",
					data: { 'start':$('#date_start').val(), 'end':$('#date_end').val()},
					success: function(data) {
						// data.value is the success return json. json string contains key value
                        alert(data.graph_data[0]);
						$('#g0').attr('src', data.graph_data[0]);
						$('#g1').attr('src', data.graph_data[1]);
						$('#g2').attr('src', data.graph_data[2]);
						$('#g3').attr('src', data.graph_data[4]);
						$('#g4').attr('src', data.graph_data[4]);
						$('#g5').attr('src', data.graph_data[5]);
						$('#g6').attr('src', data.graph_data[6]);
					},
					error: function() {
						//alert("#"+ckbid);
						alert("Error accessing server notification/badge")
						},
					complete: function() {
						}
			});
		});

	  });
</script>

Inicio:<input id="date_start"/> Fin:<input id="date_end"/>
<button class="btn btn-primary" id="btn-test1">Obtener gráfica</button>
<div class="container" align="left">
	<embed id="g0" type="image/svg+xml" src='' style='height:500px'/>
	<embed id="g1" type="image/svg+xml" src='' style='height:500px'/>
	<embed id="g2" type="image/svg+xml" src='' style='height:500px'/>
	<embed id="g3" type="image/svg+xml" src='' style='height:500px'/>
	<embed id="g4" type="image/svg+xml" src='' style='height:500px'/>
	<embed id="g5" type="image/svg+xml" src='' style='height:500px'/>
	<embed id="g6" type="image/svg+xml" src='' style='height:500px'/>

</div>
