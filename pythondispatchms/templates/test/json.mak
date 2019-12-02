<style type="text/css">

    /* set the size of the datepicker search control for Order Date*/
    #ui-datepicker-div { font-size:11px; }
    .ui-datepicker { z-index: 2000 }

    /* set the size of the autocomplete search control*/
    .ui-menu-item {
        font-size: 11px;
    }

     .ui-autocomplete {
        z-index: 2000;
        font-size: 11px;
    }

</style>
<script type="text/javascript">

    $(document).ready(function () {
        $("#jqGrid").jqGrid({
            url: 'test/data',
            mtype: "GET",
            datatype: "json",
            page: 1,
            colModel: [
                {label:"Order ID",sorttype: 'integer',name: 'OrderID',key: true,	width: 75,	searchrules : {	"required": true,"number" : true,"minValue": 10200}},
                {label:"Customer ID",name: 'CustomerID',width: 150},
                {label: "Order Date",name: 'OrderDate',width: 150,sorttype:'date',
                    searchoptions: {// dataInit is the client-side event that fires upon initializing the toolbar search field for a column
                                    // use it to place a third party control to customize the toolbar
                                    dataInit: function (element) {
                            $(element).datepicker({
                                id: 'orderDate_datePicker',
                                dateFormat: 'yy-mm-dd',
                                //minDate: new Date(2010, 0, 1),
                                maxDate: new Date(2020, 0, 1),
                                showOn: 'focus'
                            });
                        }
                    }
                },
                {label : "Ship Name",name: 'ShipName',width: 150,searchoptions: {
                        // dataInit is the client-side event that fires upon initializing the toolbar search field for a column
                        // use it to place a third party control to customize the toolbar
                        dataInit: function (element) {
                            $(element).autocomplete({
                                id: 'AutoComplete',
                                source: function(request, response){
                                    this.xhr = $.ajax({
                                        url: 'http://trirand.com/blog/phpjqgrid/examples/jsonp/autocompletep.php?callback=?&acelem=ShipName',
                                        data: request,
                                        dataType: "jsonp",
                                        success: function( data ) {
                                            response( data );
                                        },
                                        error: function(model, response, options) {
                                            response([]);
                                        }
                                    });
                                },
                                autoFocus: true
                            });
                        }
                    }
                },
                {label: "Freight",sorttype: 'number',name: 'Freight', width: 150 }
            ],
            loadonce: true,
            viewrecords: true,
            width: 780,
            height: 250,
            rowNum: 10,
            pager: "#jqGridPager"
        });
        // activate the build in search with multiple option
        $('#jqGrid').navGrid("#jqGridPager", {
            search: true, // show search button on the toolbar
            add: false,
            edit: false,
            del: false,
            refresh: true
        },
        {}, // edit options
        {}, // add options
        {}, // delete options
        {
            multipleSearch: true,


        } // search options - define multiple search
        );
    });

</script>

</div>
    <!-- page start-->
    <!-- Hidden POP UP Start-->

    <!-- Hidden POP UP End-->
<div id="noteContent" title="${_('Basic dialog')}">
</div>
<table id="jqGrid"></table>
<div id="jqGridPager"></div>

  <!-- page end-->