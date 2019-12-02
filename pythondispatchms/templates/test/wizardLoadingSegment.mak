<script type="text/javascript" src="${tg.url('/lib/tw2/dynforms.js')}" ></script>
<link rel="stylesheet" type="text/css" href="${tg.url('/lib/tw2/forms.css')}" media="all">
<script type="text/javascript">document.onkeypress = twd_suppress_enter;</script></body>
<link href="${tg.url('/lib/css/jquery.steps.css')}" rel="stylesheet">
<script src="${tg.url('/lib/jquery-validation-1.17.0/dist/jquery.validate.js')}"></script>
<script src="${tg.url('/lib/js/jquery.steps.js')}"></script>
<style type="text/css">
</style>
<script type="text/javascript">
$(document).ready(function() {

    var form = $("#wizardForm");
    form.validate({
        errorPlacement: function errorPlacement(error, element) { element.before(error); },
        rules: {
            confirm: {equalTo: "#password"},
            cname: {required: true, minlength: 2},
        },
        messages: {
            cname: {
                required: "<li>Please enter a name.</li>",
                minlength: "<li>Your name is not long enough.</li>"
            }
        }
    });
    form.steps({
        headerTag: "h3",
        bodyTag: "section",
        transitionEffect: "slideLeft",
        stepsOrientation: "vertical",
        onStepChanging: function (event, currentIndex, newIndex)
        {
                if (currentIndex === 1)
                {
                    if ($("#choose > option:selected").val() === "1")
                    {
                        form.steps("remove", 2);
                        // In this case you could also use add instead of insert
                        form.steps("insert", 2, {
                            title: "Insert Range",
                            contentMode: "async",
                            contentUrl: "https://dispatch.dudewhereismy.mx/test/asyncStep?cal=1"
                        });
                    }
                    else{
                        form.steps("remove", 2);
                        // In this case you could also use add instead of insert
                        form.steps("insert", 2, {
                            title: "Insert Calendar",
                            contentMode: "async",
                            contentUrl: "https://dispatch.dudewhereismy.mx/test/asyncStep?cal=0"
                        });
                    }
                }

            form.validate().settings.ignore = ":disabled,:hidden";
            return form.valid();
        },
        onFinishing: function (event, currentIndex)
        {
            form.validate().settings.ignore = ":disabled";
            return form.valid();
        },
        onFinished: function (event, currentIndex)
        {
            $(this).closest('.ui-dialog-content').dialog('close');
            $.ajax({
                  type: "GET",
                  url: '${h.url()}/test/saveWizard',
                  contentType: "application/json; charset=utf-8",
                  data: {'parameter1': $('#name').val(),'parameter2':$('#surname').val()},
                  success: function(parameterdata) {


                  },
                  error: function() {
                     $.alert("Error al guardar el Monitoreo Dedicado", { autoClose:false,});
                  },
                  complete: function() {
                  }
             });
        }
    });

});
</script>


<form id="wizardForm" action="#">
    <h3>TW2</h3>
    <section>
        <label for="movieform:title">Title</label>
        <input name="movieform:title" type="text" value="" id="movieform:title" class="required" minlength="2"/>
        <label for="movieform:director">Director</label>
        <input name="movieform:director" type="text" id="movieform:director" class="required" minlength="2"/>
        <label for="movieform:genres">Genres</label><br>
        <input type="checkbox" name="movieform:genres" value="1" id="movieform:genres:0"/>
        <label for="movieform:genres:0">Action</label><br>
        <input type="checkbox" name="movieform:genres" value="2" id="movieform:genres:1"/>
        <label for="movieform:genres:1">Comedy</label><br>
        <input type="checkbox" name="movieform:genres" value="3" id="movieform:genres:2"/>
        <label for="movieform:genres:2">Romance</label><br>
        <input type="checkbox" name="movieform:genres" value="4" id="movieform:genres:3"/>
        <label for="movieform:genres:3">Sci-fi</label><br>
        <table id="movieform">
            <tr class="even"  id="movieform:cast:container">
                <th><label for="cast">Cast</label></th>
                <td >
                    <table id="movieform:cast">
                        <tr>
                            <th>Character</th><th>Actor</th><th></th>
                            <td><input style="display:none" type="image" id="movieform:cast:undo" src="${tg.url('/img/undo.png')}" title="Undo" alt="Undo" onclick="twd_grow_undo(this); return false;" /></td>
                        </tr>
                        <tr style="display:none;" id="movieform:cast:0" class="odd">
                            <td id="movieform:cast:0:character:container">
                                <input name="movieform:cast:0:character" type="text" onchange="twd_grow_add(this);" id="movieform:cast:0:character"/>
                            </td>
                            <td id="movieform:cast:0:actor:container">
                                <input name="movieform:cast:0:actor" type="text" onchange="twd_grow_add(this);" id="movieform:cast:0:actor"/>
                            </td>
                            <td id="movieform:cast:0:del:container">
                                <input src="${tg.url('/img/del.png')}" style="display:none;" name="movieform:cast:0:del" value="" id="movieform:cast:0:del" onclick="twd_grow_del(this); return false;" alt="Delete row" type="image"/>
                            </td>
                        </tr>
                        <tr id="movieform:cast:1" class="even">
                            <td id="movieform:cast:1:character:container">
                                <input name="movieform:cast:1:character" type="text" onchange="twd_grow_add(this);" id="movieform:cast:1:character"/>
                            </td>
                            <td id="movieform:cast:1:actor:container">
                                <input name="movieform:cast:1:actor" type="text" onchange="twd_grow_add(this);" id="movieform:cast:1:actor"/>
                            </td>
                            <td id="movieform:cast:1:del:container">
                                <input src="${tg.url('/img/del.png')}" style="display:none;" name="movieform:cast:1:del" value="" id="movieform:cast:1:del" onclick="twd_grow_del(this); return false;" alt="Delete row" type="image"/>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </section>
    <h3>Account</h3>
    <section>
        <label for="cname">Account Name</label>
        <em>*</em><input id="cname" name="name" size="25" class="required" minlength="2" />
        <label for="password">Password *</label>
        <input id="password" name="password" type="text" class="required">
        <label for="confirm">Confirm Password *</label>
        <input id="confirm" name="confirm" type="text" class="required">
        <p>(*) Mandatory</p>
    </section>
    <h3>Profile</h3>
    <section>
        <label for="name">First name *</label>
        <input id="name" name="name" type="text" class="required">
        <label for="surname">Last name *</label>
        <input id="surname" name="surname" type="text" class="required">
        <label for="email">Email *</label>
        <input id="email" name="email" type="text" class="required email">
        <label for="address">Address</label>
        <input id="address" name="address" type="text">
        <label for="age">Age</label>
        <input id="age" name="age" type="text" class="required number">
        <label for="choose">Payment</label>
        <br>
        <select id="choose">
            <option value="0" selected="selected">Calendar</option>
            <option value="1">Date Range</option>
        </select>
        <p>(*) Mandatory</p>
    </section>
    <h3>Calendar</h3>
    <section data-mode="async" data-url="https://dispatch.dudewhereismy.mx/test/asyncStep?cal=0">
    </section>
    <h3>Finish</h3>
    <section>
        <input id="acceptTerms" name="acceptTerms" type="checkbox" class="required"> <label for="acceptTerms">I agree with the Terms and Conditions.</label>
    </section>
</form>
