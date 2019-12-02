<style type="text/css">
</style>
<script type="text/javascript">
    function openWizardWindow(){
                $.ajax({
                          type: "GET",
                          url: '${h.url()}/admin/loadWizard',
                          contentType: "application/json; charset=utf-8",
                          data: { 'name':'pythondispatchms.templates.test.wizardLoadingSegment','user':'${user}' },
                          success: function(parameterdata) {
                              //Insert HTML code
                              //$( "#addAssignForm" ).html(parameterdata.expressionformtemplate);

                              var winHeight = 750; //Math.round(window.innerHeight * .50)
                              var winWidth = 1200;//Math.round(window.innerWidth * .50)

                              if ($("#wizardForm").length){
                                  $("#wizardForm").remove();
                              }
                              var newDiv = $(document.createElement('div'));

                              newDiv.html(parameterdata.dedwizardtemplate);
                              var DedicatedWizardDialog = newDiv.dialog({
                                  autoOpen: false,
                                  title: "${_('Wizard Example')}",
                                  height: winHeight,
                                  width: winWidth,
                                  modal: true,
                                  close: function() {
                                      //$('#globalExpForm')[0].reset();
                                      //form[ 0 ].reset();
                                      //allFields.removeClass( "ui-state-error" );
                                  }
                               });
                              DedicatedWizardDialog.data('rowId',1);
                              DedicatedWizardDialog.dialog( "open" );
                          },
                          error: function() {
                              alert("Error loaging Wizard")
                          },
                          complete: function() {
                          }
                     });
            }
</script>

<input id="clickMe" type="button" value="clickme" onclick="openWizardWindow();" />


