<style type="text/css">
</style>
<script type="text/javascript">



$(document).ready(function () {
alternative()
function alternative(){
    $.jgrid.jqModal = $.jgrid.jqModal || {};

    $.extend(true, $.jgrid.jqModal, {toTop: true});
    var winWidth = 810;//Math.round(window.innerWidth * .50)
    var winHeight = 400; //Math.round(window.innerHeight * .50)
    var grid_name = '#jgGrid';
    var pager_name = "#jqGridPager";
    $.extend($.jgrid.nav,{alerttop:1});
        var grid_name_html= grid_name.substr(1);
        var pager_name_html=pager_name.substr(1);
        if ($(grid_name).length){
          $(grid_name).remove();
          $(pager_name).remove();
        }
        var newDiv = $(document.createElement('div'));
        newDiv.html('<table id="'+grid_name_html+'"></table> <div id="'+pager_name_html+'"> </div>');
        //newDiv.html('<p>Hola</p>');
        var createUsersSticky = newDiv.dialog({
            autoOpen: false,
            height: winHeight - 20,
            width: winWidth,
            modal: true,
            close: function () {
                //form[ 0 ].reset();
                //allFields.removeClass( "ui-state-error" );
            }
        });
   $(document).ready(function () {

        $(grid_name ).jqGrid({
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
        $(grid_name ).navGrid( pager_name, {
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
         createUsersSticky.dialog("open");
    });


}


    });

</script>


  <!-- page end-->