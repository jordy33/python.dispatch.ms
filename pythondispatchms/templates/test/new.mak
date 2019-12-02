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

<div id="Ecran">
	<table id="jqGrid"></table>
	<div id="jqGridPager"></div>
</div>

    <script type="text/javascript">
        $(document).ready(function () {
           $.jgrid.jqModal = $.jgrid.jqModal || {};
$.extend(true, $.jgrid.jqModal, {toTop: true});

$("#Ecran").dialog({
    //dialogClass: 'Ecran',
    autoOpen: false,
    width: 560,
    height: 370,
    modal: true,
    open: function (event, ui) {
        $("#jqGrid").jqGrid({
            url: 'http://trirand.com/blog/phpjqgrid/examples/jsonp/getjsonp.php?callback=?&qwery=longorders',
            mtype: "GET",
            datatype: "jsonp",
            colModel: [
                { label: 'OrderID', name: 'OrderID', key: true, width: 75 },
                { label: 'Customer ID', name: 'CustomerID', width: 150 },
                { label: 'Order Date', name: 'OrderDate', width: 150 },
                { label: 'Freight', name: 'Freight', width: 150 },
                { label:'Ship Name', name: 'ShipName', width: 150 }
            ],
            cmTemplate: { width: 80, autoResizable: true },
            autoResizing: { compact: true },
            autoresizeOnLoad: true,
            height: "auto",
            viewrecords: true,
            //width: 480,
            height: "auto",
            rowNum: 10,
            pager: "#jqGridPager"
        }).jqGrid("navGrid", { del: true, add: false, edit: false });
    },
    close:function () {}
});
$("#Ecran").dialog("open");

        });

   </script>


</body>
</html>