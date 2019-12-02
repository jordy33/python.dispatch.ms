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