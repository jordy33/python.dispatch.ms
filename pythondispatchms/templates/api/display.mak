<!DOCTYPE html>

<html lang="en">

<head>
    <!-- The jQuery library is a prerequisite for all jqSuite products -->
    <script type="text/ecmascript" src="${tg.url('/lib/js//jquery-1.11.0.js')}"></script>
    <!-- We support more than 40 localizations -->
    <script type="text/ecmascript" src="${tg.url('/lib/js/grid.locale-en.js')}"></script>
    <!-- This is the Javascript file of jqGrid -->
    <script type="text/ecmascript" src="${tg.url('/lib/js/jquery.jqgrid.src.js')}"></script>
    <script type="text/ecmascript" src="${tg.url('/lib/js/jquery-ui.min.js')}"></script>
    <!-- This is the localization file of the grid controlling messages, labels, etc.
    <!-- A link to a jQuery UI ThemeRoller theme, more than 22 built-in and many more custom -->
    <link rel="stylesheet" type="text/css" media="screen" href="${tg.url('/lib/css/jquery-ui.css')}" />
    <!-- The link to the CSS that the grid needs -->
    <link rel="stylesheet" type="text/css" media="screen" href="${tg.url('/lib/css/ui.jqgrid.css')}"  />
    <link href="${tg.url('/new/font-awesome.min.css')}" rel="stylesheet" />
    <meta charset="utf-8" />
    <title>jqGrid Loading Data - Million Rows from a REST service</title>
</head>
<body>

<div id="Display">
<button id="prev">Prev</button>
<button id="next">Next</button>
    <br>
    <img id="image" src="data:image/png;base64, ${jobimage}" alt="Red dot" />
</div>

    <script type="text/javascript">
        $(document).ready(function () {
            function putImage(job,id){
                $.ajax({
                    url: "https://dispatch.dudewhereismy.mx/api/getimage?job="+job+"&id="+id,
                    type: "GET",
                }).done(function( data, textStatus, jqXHR ) {
                    $("#image").attr('src', 'data:image/jpeg;base64, ' + data.image);
                }).fail(function( jqXHR, textStatus, errorThrown ) {
                    alert("fail: " + errorThrown);
            });
            }
            var job="${currentjob}";
            var elements='${elements}';
            var items=elements.split(",");
            var i=0;
            var tot=items.length;
            $('#prev').click(function(){
                if (i>0 ){
                    i--;
                    putImage(job,items[i])
                }
            });

            $('#next').click(function(){
                if (i<tot-1){
                    i++;
                    putImage(job,items[i])
                }
            });
        });

   </script>


</body>
</html>