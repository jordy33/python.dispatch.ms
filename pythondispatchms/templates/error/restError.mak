<%inherit file="local:templates.master"/>
<%def name="title()">
  Welcome to Telefonica
</%def>
<%def name="head_content()">

   <style type="text/css">
   </style>

   <script type="text/javascript">
   </script>

</%def>
<!--main content start-->
<section id="main-content">

      <!-- page start-->
 <div class="col-sm-9 col-sm-offset-3 col-lg-12 col-lg-offset-0 main">
		<div class="row">
			<ol class="breadcrumb">
				<li><a href="#">
					<em class="fa fa-times-circle"></em>
				</a></li>
				<li class="active">Error</li>
			</ol>
		</div><!--/.row-->
        <br>

    <h1>Internal Error</h1>

    <h3>${error}</h3>
    <h3>${descript}</h3>


              <!-- page end-->
</div>
      <!-- page end-->
</div>
  </section>
</section>

<%def name="bottom_scripts()">
</%def>